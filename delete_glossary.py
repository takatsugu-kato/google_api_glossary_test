from google.cloud import translate_v3beta1 as translate
client = translate.TranslationServiceClient()

project_id = 'automl-translation-216000'
glossary_id = 'test-glossary-1'

parent = client.glossary_path(
    project_id,
    'us-central1',  # The location of the glossary
    glossary_id)

operation = client.delete_glossary(parent)
result = operation.result(timeout=90)
print('Deleted: {}'.format(result.name))
