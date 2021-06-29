# Python CBC Bundling Script

This project bundles cbz files into one big cbc file for easier reading on your eReader device of choice.
CBC Files are compatabile with [calibre](https://calibre-ebook.com/) via drag and drop.

## What is a CBC file?

> A comic book collection is a .cbc file. A .cbc file is a ZIP file that contains other CBZ/CBR files. In addition the .cbc file must contain a simple text file called comics.txt, encoded in UTF-8. The comics.txt file must contain a list of the comics files inside the .cbc file, in the form filename:title

[Source](https://manual.calibre-ebook.com/de/conversion.html)


## Motivation

I found only broken code on github, so here is my attempt

## Requirements

Uses pathlib to be os independent and thus requires:

+ [Python 3](https://www.python.org/)

## Usage

```bash
#!/bin/bash

python cbc.py -d ./ -o "myoutputfile.cbc"
```
