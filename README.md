# Python CBC Bundling Script

This project bundles cbz files into one big cbc file for easier reading on your eReader device of choice.
CBC Files are compatabile with [calibre](https://calibre-ebook.com/) via drag and drop.

## What is a CBC file?

> A comic book collection is a .cbc file. A .cbc file is a ZIP file that contains other CBZ/CBR files. In addition the .cbc file must contain a simple text file called comics.txt, encoded in UTF-8. The comics.txt file must contain a list of the comics files inside the .cbc file, in the form filename:title

[Source](https://manual.calibre-ebook.com/de/conversion.html)

## Usage

Assuming you have a directionary like:
```powershell
PS C:\Users\MangaAficionado> ls 'Documents\Mangas\Kimetsu no Yaiba\'

    Directory: C:\Users\MangaAficionado\Documents\Mangas\Kimetsu no Yaiba

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          27.06.2021    00:33       11384173 Ch.001 - Cruelty.cbz
-a---          27.06.2021    00:34        5485649 Ch.002 - Someone Unknown.cbz
...
```

You can type:

```powershell
PS C:\Users\MangaAficionado> python cbc.py -d 'C:\Users\MangaAficionado\Documents\Mangas\Kimetsu no Yaiba' -o "KimetsuNoYaiba.cbc"
``` 
And the file gets created in the same directory. 
```powershell
PS C:\Users\MangaAficionado> ls 'Documents\Mangas\Kimetsu no Yaiba\'

    Directory: C:\Users\MangaAficionado\Documents\Mangas\Kimetsu no Yaiba

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          27.06.2021    00:33       11384173 Ch.001 - Cruelty.cbz
-a---          27.06.2021    00:34        5485649 Ch.002 - Someone Unknown.cbz
...
-a---          29.06.2021    17:36            936 comics.txt
-a---          29.06.2021    17:36       68812205 KimetsuNoYaiba.cbc
```

## Requirements

Uses pathlib to be os independent and thus requires:

+ [Python 3](https://www.python.org/)

