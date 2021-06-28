import argparse
from os import listdir
from os.path import isfile, join
from zipfile import ZipFile
from pathlib import Path


class merge():
    """
    Merges cbz to cbc file containing comics.txt for calibre
    """

    def __init__(self, directory, filename="comics.cbc") -> None:
        super().__init__()
        self.directory = Path(directory)
        self.filename = filename

    def get_all_files(self):
        onlyfiles = [f for f in listdir(str(self.directory)) if isfile(
            join(str(self.directory), f))]
        onlycbz = [f for f in onlyfiles if ".cbz" in f or ".CBZ" in f]
        return onlycbz

    def get_names(self, files):
        names = files
        for ele in [".cbz", ".CBZ"]:
            names = list(map(lambda x: x.replace(ele, ""), names))
        return names

    def create_comics_txt(self, files, names):
        zipped = (list(zip(files, names)))
        result = ""
        for ele in zipped:
            result += "{}:{}\n".format(ele[0], ele[1])
        return result

    def save_comics_txt(self, txt):
        with open(self.directory / 'comics.txt', 'w') as f:
            f.write(txt)
            f.close()

    def save(self, files):
        zipObj = ZipFile(self.directory / self.filename, 'w')
        for f in files+["comics.txt"]:
            zipObj.write(self.directory / f, arcname=f)
        zipObj.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Bundles .CBZ Files to CB-Collection (.cbc)')
    parser.add_argument("-d", help="directory to search cbz in", type=str)
    parser.add_argument("-o", help="file to save the cbc as", type=str)
    args = parser.parse_args()
    filename = "comics.cbc"

    if (args.d == None):
        args.d = input("Please specify directory > ")

    if (args.o != None):
        filename = args.o

    merge = merge(args.d, filename)
    files = merge.get_all_files()
    names = merge.get_names(files)
    txt = merge.create_comics_txt(files, names)
    merge.save_comics_txt(txt)
    merge.save(files)