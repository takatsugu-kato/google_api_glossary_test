from google.cloud import translate_v3beta1 as translate
client = translate.TranslationServiceClient()

project_id = 'automl-translation-216000'
location = 'us-central1'  # The location of the glossary

parent = client.location_path(project_id, location)

for glossary in client.list_glossaries(parent):
    print('Name: {}'.format(glossary.name))
    print('Entry count: {}'.format(glossary.entry_count))
    print('Input uri: {}'.format(
        glossary.input_config.gcs_source.input_uri))
    for language_code in glossary.language_codes_set.language_codes:
        print('Language code: {}'.format(language_code))
