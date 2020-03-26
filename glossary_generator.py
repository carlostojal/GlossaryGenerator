
#
# Copyright (c) Carlos Tojal 2020
# GlossaryGenerator
# glossary_generator.py
#

from docx import Document
import requests
import json
from io import BytesIO

print("\n** GlossaryGenerator **")
print("Developed by Carlos Tojal\n")

# loads configuration from file "config.json"
print("Loading configuration...")
f = open("config.json", "r")
config = json.loads(f.read())
f.close()
print("Loaded configuration.\n")

print("Generating glossary...\n")

document = Document()

# adds title do document
document.add_heading(config['title'], level = 0)

document.add_paragraph() # blank line

print("Searching for terms...")

for term in config['terms']:
    print("\nSearching for term \"" + term + "\"...")
    response = requests.get("https://api.duckduckgo.com/?q=" + term + "&format=json&pretty=1") # request DuckDuckGo API to get term definition
    search = json.loads(response.text)
    text = search['AbstractText']
    if config['single_phrase']:
        text = text.split(".")[0] + "."
    p = document.add_paragraph(style = "List Bullet")
    r = p.add_run(term + ": ")
    r.bold = True # term is bold in document
    if text != "": # if text was returned
        print("Found.")
        r = p.add_run(text)
        if config['insert_term_image']: # if the user chose to insert term image
            if search['Image'] != "": # if an image is available
                # get image from URL and insert to document
                response1 = requests.get(search['Image'])
                image = BytesIO(response1.content)
                document.add_picture(image)
    else:
        print("Not found.")
        r = p.add_run("Not found.")

print("\nGenerated glossary.")

print("\nWriting header...")
# writes header loaded from configuration
header = document.sections[0].header
p = header.paragraphs[0]
p.text = config['header_text']
print("Written header.")

print("\nWriting footer...")
# writes footer loaded from configuration
footer = document.sections[0].footer
p = footer.paragraphs[0]
p.text = config['footer_text']
print("Written footer.")
    
if config['credits']: # append credits to footer if user chose that option
    footer = document.sections[0].footer
    p = footer.paragraphs[0]
    p.text += "\n\nGenerated using GlossaryGenerator\n(https://github.com/carlostojal/GlossaryGenerator)"

# saves document
print("\nSaving document...")
document.save(config['document_name'])
print("Saved document (" + config['document_name'] + ").")