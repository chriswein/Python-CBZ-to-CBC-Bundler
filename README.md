# Python CBC Bundling Script

This project bundles cbz files into one big cbc file for easier reading on your eReader device of choice.
CBC Files are compatabile with [calibre](https://calibre-ebook.com/) via drag and drop.

## Features

It only does this:


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
