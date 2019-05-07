from google.cloud import translate_v3beta1 as translate
client = translate.TranslationServiceClient()

project_id = 'automl-translation-216000'
glossary_id = 'test-glossary-1_es'

parent = client.glossary_path(
    project_id,
    'us-central1',  # The location of the glossary
    glossary_id)

response = client.get_glossary(parent)
print('Name: {}'.format(response.name))
print('Language Pair:')
print('\tSource Language Code: {}'.format(
    response.language_pair.source_language_code))
print('\tTarget Language Code: {}'.format(
    response.language_pair.target_language_code))
print('Input Uri: {}'.format(
    response.input_config.gcs_source.input_uri))
