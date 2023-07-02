from datetime import datetime
from typing import List, Optional

from const.sort import Sort
from models.data import Data
from models.entry import Entry


class DataController:
    entries: List[Entry]

    def __init__(self, entries: List[Entry] = None):
        if not entries:
            entries = []
        self.entries = entries

    def get_entry_by_user_id(self, user_id: str) -> Optional[Entry]:
        """
        Returns te first entry found with the user id
        :param user_id:
        :return:
        """
        for entry in self.entries:
            if entry.user.user_id == user_id:
                return entry
        return None

    def get_data_by_user_id(self, user_id: str, level_id: int) -> Optional[Data]:
        """
        Returns a single Data
        :param user_id: user id
        :param level_id: level id
        :return:
        """
        data = self.get_all_data_by_user_id(user_id=user_id)
        if not data:
            return None
        if len(data) < level_id:
            return None
        return data[level_id]

    def get_all_data_by_user_id(self, user_id: str, start: datetime = None, stop: datetime = None, limit: int = None,
                                sort_by: Sort = None) -> Optional[List[Data]]:
        """
        Returns a list of Data for a given user
        :param user_id: user id
        :param start: filter datetime start
        :param stop: filter datetime stop
        :param limit: limit of results
        :param sort_by: sorting results
        :return:
        """
        entry = self.get_entry_by_user_id(user_id=user_id)
        if not entry:
            return None
        if not entry.data:
            return None
        data = entry.data
        if start is not None or stop is not None:
            data = DataController.filter(data_list=data, start=start, stop=stop)
        if limit is not None:
            data = data[:limit]
        if sort_by is not None:
            data = DataController.sort(data_list=data, sort_by=sort_by)
        return data

    @staticmethod
    def filter(data_list: List[Data], start: datetime, stop: datetime) -> List[Data]:
        """
        Filters a list by start and stop timestamps
        :param data_list: data list
        :param start: filter datetime start
        :param stop: filter datetime stop
        :return:
        """
        ret = []
        for data in data_list:
            if start is None and data.device_timestamp < stop:
                ret.append(data)
                continue
            if stop is None and start < data.device_timestamp:
                ret.append(data)
                continue
            if start < data.device_timestamp < stop:
                ret.append(data)
        return ret

    @staticmethod
    def sort(data_list: List[Data], sort_by: Sort) -> List[Data]:
        if sort_by == Sort.TIME:
            data_list.sort(key=lambda x: x.device_timestamp)
        elif sort_by == Sort.RECORD_TYPE:
            data_list.sort(key=lambda x: int(x.record_type))
        return data_list
