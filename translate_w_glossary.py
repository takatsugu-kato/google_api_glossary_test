from google.cloud import translate_v3beta1 as translate
client = translate.TranslationServiceClient()

project_id = 'automl-translation-216000'
glossary_id = 'test-glossary-1'
text = 'If the Import Wizard does not list your other browser, you can still import bookmarks from another browser but you will need to first export and save those bookmarks as an HTML file.'
location = 'us-central1'  # The location of the glossary

glossary = client.glossary_path(
    project_id,
    'us-central1',  # The location of the glossary
    glossary_id)

glossary_config = translate.types.TranslateTextGlossaryConfig(
    glossary=glossary)

parent = client.location_path(project_id, location)

result = client.translate_text(
    parent=parent,
    contents=[text],
    mime_type='text/html',  # mime types: text/plain, text/html
    source_language_code='en',
    target_language_code='ja',
    glossary_config=glossary_config)

print(result.translations[0].translated_text)
print(result.glossary_translations[0].translated_text)
