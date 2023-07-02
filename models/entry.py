from datetime import datetime
from typing import List

from models.data import Data
from models.user import User


class Entry:
    user: User = None
    data: List[Data] = None
    timestamp: datetime = None

    def __init__(self, user: User = None, data: List[Data] = None, timestamp: datetime = None):
        self.user = user
        self.data = data
        self.timestamp = timestamp
