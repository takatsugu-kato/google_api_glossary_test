from google.cloud import translate_v3beta1 as translate
client = translate.TranslationServiceClient()

project_id = 'automl-translation-216000'
glossary_id = 'test-glossary-1'
location = 'us-central1'  # The location of the glossary

name = client.glossary_path(
    project_id,
    location,
    glossary_id)

language_codes_set = translate.types.Glossary.LanguageCodesSet(
    language_codes=['en', 'ja'])

gcs_source = translate.types.GcsSource(
    input_uri='gs://glossary/glossary.csv')

input_config = translate.types.GlossaryInputConfig(
    gcs_source=gcs_source)

glossary = translate.types.Glossary(
    name=name,
    language_codes_set=language_codes_set,
    input_config=input_config)

parent = client.location_path(project_id, location)

operation = client.create_glossary(parent=parent, glossary=glossary)

result = operation.result(timeout=90)
print('Created: {}'.format(result.name))
print('Input Uri: {}'.format(result.input_config.gcs_source.input_uri))
