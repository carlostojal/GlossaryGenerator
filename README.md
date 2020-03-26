# GlossaryGenerator
Glossary Generator that uses the DuckDuckGo Instant Answer API

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
| ```terms``` | Array containing all terms to include in the glossary. |

## Screenshots

![Generated document](https://raw.githubusercontent.com/carlostojal/GlossaryGenerator/master/img/document.png)

![Program](https://raw.githubusercontent.com/carlostojal/GlossaryGenerator/master/img/program.png)