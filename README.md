# GlossaryGenerator
Glossary Generator that uses the DuckDuckGo Instant Answer API to generate a glossary in formats such as DOCX, JSON, CSV and TXT.

## How to use
* Make sure you have Python 3.x installed.
* Make sure you have an Internet connection.
* Run ```setup.sh```. This will install all required modules. This is only needed once.
* Write all terms in the file ```terms.txt```. Feel free to write your own script to populate this file.
* Run the script ```glossary_generator.py```.
* That's it! By default the glossary will be in the files in the folder ```output``` inside the script directory. You can change this in the configuration file. Configuration documentation below.

## Configuration
All configuration is maintained in the file ```config.json```.

| Key | Description |
| --- | ----------- |
| ```title``` | Document title. (**Default:** Sample Glossary) |
| ```header_text``` | Header text. (**Default:** Sample Header) |
| ```footer_text``` | Footer text. (**Default:** Sample Footer) |
| ```n_phrases``` | Number of phrases from the search to be inserted. (**Default:** ```1```) |
| ```insert_term_image``` | if ```true``` a descriptive image of the term will be inserted (when available). (**Default:** ```true```) |
| ```credits``` | If ```true``` credits will be added to document footer. (**Default:** ```true```) |
| ```output_path``` | Is the path of the file that will be generated. (**Default:** ```output```) |
| ```filename``` | Is the name of the file(s) that will be generated. (**Default:** ```glossary```) |
| ```docx``` | If ```true``` a ```.docx``` file will be generated. (**Default:** ```true```) |
| ```json``` | If ```true``` a ```.json``` file will be generated. (**Default:** ```true```) |
| ```csv``` | If ```true``` a ```.csv``` file will be generated. (**Default:** ```true```) |
| ```txt``` | If ```true``` a ```.txt``` file will be generated. (**Default:** ```true```) |

## Screenshots

* Generated DOCX
![Generated document](https://raw.githubusercontent.com/carlostojal/GlossaryGenerator/master/img/docx.png)

* Generated JSON
![Generated document](https://raw.githubusercontent.com/carlostojal/GlossaryGenerator/master/img/json.png)

* Generated CSV
![Generated document](https://raw.githubusercontent.com/carlostojal/GlossaryGenerator/master/img/csv.png)

* Generated TXT
![Generated document](https://raw.githubusercontent.com/carlostojal/GlossaryGenerator/master/img/txt.png)

* Terms file
![Terms file](https://raw.githubusercontent.com/carlostojal/GlossaryGenerator/master/img/terms.png)

* Script running
![Script running](https://raw.githubusercontent.com/carlostojal/GlossaryGenerator/master/img/script.png)
