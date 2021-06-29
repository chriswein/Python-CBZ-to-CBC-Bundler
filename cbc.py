import argparse
from os import listdir
from os.path import isfile, join
from zipfile import ZipFile
from pathlib import Path


class merge_cbc():
    """
    Merges cbz to cbc file containing comics.txt for calibre
    """

    def __init__(self, directory, filename="comics.cbc") -> None:
        super().__init__()
        self.directory = Path(directory)
        self.filename = filename
    
    def __matches_any_filetype(self,string):
        """Matches the file name any of our desired types?"""
        for t in [".cbz",".cbr",".CBZ",".CBR"]:
            if t in string:
                return True
        return False

    def get_all_filenames(self):
        onlyfiles = [f for f in listdir(str(self.directory)) if isfile(
            join(str(self.directory), f))]
        onlycbz = [f for f in onlyfiles if self.__matches_any_filetype(f)]
        return onlycbz

    def get_names_for_files(self, files):
        """Remove all trailing file extensions for the comics.txt file"""
        return [f[:-4] for f in files]

    def create_and_save_comics_txt(self, files, names):
        """Create a comics.txt file as defined in [Calibre](https://manual.calibre-ebook.com/de/conversion.html)"""
        zipped = (list(zip(files, names)))
        result = ""
        for ele in zipped:
            result += "{}:{}\n".format(ele[0], ele[1])
        
        # Save the file in the root directory of the cbz files
        (self.directory / "comics.txt").open('w').write(result)
        return result

    def save_cbc(self, files):
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

    merge_cbc = merge_cbc(args.d, filename)
    files = merge_cbc.get_all_filenames()
    names = merge_cbc.get_names_for_files(files)
    txt = merge_cbc.create_and_save_comics_txt(files, names)
    merge_cbc.save_cbc(files)
