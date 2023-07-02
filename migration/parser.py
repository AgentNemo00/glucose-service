from dateutil import parser
import pathlib as p
from typing import Dict, Generator, List

import csv23

from migration.mapping import map_keys
from models.data import Data
from models.entry import Entry
from models.user import User


class Parser:

    def __init__(self, path: p.Path):
        self.path = path
        self.header = None  # csv header
        self.user = None
        self.timestamp = None

    def read_raw(self) -> Generator[Dict, None, None]:
        """
        Reads raw data from a csv file
        :return: Generator
        """
        meta_data_parsed = False
        header_parsed = False
        with csv23.open_csv(self.path.resolve()) as reader:
            for index, row in enumerate(reader):
                if not row:
                    continue  # skip empty rows
                if not meta_data_parsed:
                    self.set_meta_data(row=row)
                    meta_data_parsed = True
                    continue
                if not header_parsed:
                    self.header = row
                    header_parsed = True
                    continue
                yield self.row_to_dict(row=row)

    def read_data(self) -> Generator[Data, None, None]:
        """
        Reads data from a csv file and returns it as a class
        :return: Generator
        """
        for raw in self.read_raw():
            data = {}
            for key in raw.keys():
                data[map_keys(key)] = raw.get(key) if raw.get(key) else ""
            yield Data(**data)

    def read(self) -> Entry:
        """
        Parses all information
        :return:
        """
        data_list = []
        for data in self.read_data():
            data_list.append(data)
        return Entry(user=self.user, data=data_list, timestamp=self.timestamp)

    def row_to_dict(self, row: List) -> Dict:
        """
        Converts a list of values in a dictionary
        :param row:
        :return:
        """
        return dict((self.header[index], v) for index, v in enumerate(row))

    def set_meta_data(self, row: List):
        if row[-2] == "Erstellt von":  # TODO: hardcoded, outsource this
            self.user = User(user_id=self.path.stem, name=row[-1])
        if row[1] == "Erstellt am":
            try:
                self.timestamp = parser.parse(row[2])
            except:
                pass
