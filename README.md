# GlossaryGenerator
Glossary Generator that uses the DuckDuckGo Instant Answer API to generate a DOCX glossary.

## How to use
* Make sure you have Python 3.x installed.
* Make sure you have an Internet connection.
* Run ```setup.sh```. This will install all required modules. This is only needed once.
* Write all terms in the file ```terms.txt```. Feel free to write your own script to populate this file.
* Run the script ```glossary_generator.py```.
* That's it! By default the glossary will be in the document ```glossary.docx``` in the same directory as the script. You can change this in the configuration file. Configuration documentation below.

## Configuration
All configuration is maintained in the file ```config.json```.

| Key | Description |
| --- | ----------- |
| ```title``` | Document title. (**Default:** Sample Glossary) |
| ```header_text``` | Header text. (**Default:** Sample Header) |
| ```footer_text``` | Footer text. (**Default:** Sample Footer) |
| ```single_phrase``` | If ```true``` only the first phrase of the search result will be inserted. (**Default:** ```true```) |
| ```insert_term_image``` | if ```true``` a descriptive image of the term will be inserted. (**Default:** ```true```) |
| ```credits``` | If ```true``` credits will be added to document footer. (**Default:** ```true```) |
| ```document_name``` | Is the name of the file that will be generated. (**Default:** ```glossary.docx```) |
