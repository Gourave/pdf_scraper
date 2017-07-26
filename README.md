# PDF Scraper

This script was inspired by the fact that the author did not want to click and download each pdf from a given website manually. He thought there was a better way and so he made this.

This is a python script designed to download all the pdfs from a website. It goes through all the links in a website and then filters through them to see which links are pointing to a pdf file. It will then proceed to download the files to either a default location specified in the script `~/Desktop/pdfs` or a location specified through the command line.

Note: This project is no where near being full proof. It will only download pdfs if the link to it ends with `.pdf`.

## Instructions

If running the script from the command line with no arguments, the script will point to the default directory specified and download the pdfs from the default website specified.

Command line arguments can be given. The first argument must be the url of the website that you wish to download the pdfs from and the second must be the directory you wish to save it to.

Example: 
~~~~
python scraper.py https://uwaterloo.ca/scholar/ahilal/classes/ece-457a-cooperative-and-adaptive-algorithms/materials/schedule ~/Desktop/test/
~~~~
