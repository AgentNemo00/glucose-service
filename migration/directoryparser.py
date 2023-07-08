import pathlib as p
from typing import List
from os import listdir
from os.path import isfile, join, isdir
from migration.fileparser import FileParser
from models.entry import Entry


class DirectoryParser:

    def __init__(self, path: p.Path):
        self.path = path

    def read(self) -> List[Entry]:
        """
        Reads the directory and parses all files inside
        TODO: check for csv files
        """
        ret = []
        if not isdir(self.path):
            return ret
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in files:
            fp = FileParser(path=p.Path(file))
            ret.append(fp.read())
        return ret
