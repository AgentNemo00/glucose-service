from dateutil import parser
import datetime
import os
import pathlib as p

from fastapi import FastAPI, Depends

from const.sort import Sort
from controller.datacontroller import DataController
from migration.fileparser import FileParser

router = FastAPI(title=os.getenv("SWAGGER_TITLE", default="UNA-HEALTH"),
                 version=os.getenv("SWAGGER_VERSION", default=str(datetime.datetime.now())),
                 description=os.getenv("SWAGGER_DESCRIPTION", default="Service for fetching glucose data"),
                 license_info={
                     "name": "Apache 2.0",
                     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                 }, )


async def get_controller():
    one = FileParser(path=p.Path("1.csv"))
    two = FileParser(path=p.Path("2.csv"))
    three = FileParser(path=p.Path("3.csv"))
    return DataController(entries=[one.read(), two.read(), three.read()])


@router.get("/api/v1/levels", description="Fetches all entries about a user")
async def get_by_user(user_id: str = 0, start: str = None, stop: str = None, limit: int = None, sort: int = None,
                      controller: DataController = Depends(get_controller)):
    start_t = None
    stop_t = None
    sort_by = None
    try:
        start_t = parser.parse(start)
    except:
        pass
    try:
        stop_t = parser.parse(stop)
    except:
        pass
    try:
        sort_by = Sort(sort)
    except:
        pass
    return controller.get_all_data_by_user_id(user_id=user_id, start=start_t, stop=stop_t, limit=limit,
                                              sort_by=sort_by)


@router.get("/api/v1/levels/{level_id}", description="Fetches a single entry about a user")
async def get_by_user(level_id: int = 0, user_id: str = 0,
                      controller: DataController = Depends(get_controller)):
    return controller.get_data_by_user_id(user_id=user_id, level_id=level_id)
