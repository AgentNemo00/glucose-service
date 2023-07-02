from datetime import datetime
from dateutil import parser


class Data:
    device: str = ""
    sid: str = ""
    device_timestamp: datetime = None
    record_type: str = ""
    glucose_level_mg_dl: str = ""
    glucose_scan_mg_dl: str = ""
    none_numeric_fast_acting_insulin: str = ""
    fast_acting_insulin_units: str = ""
    none_numeric_food_data: str = ""
    carbohydrates_gram: str = ""
    carbohydrates_portion: str = ""
    none_numeric_depot_insulin: str = ""
    depot_insulin_units: str = ""
    notes: str = ""
    glucose_test_strips_mg_dl: str = ""
    keton_mmol_l: str = ""
    mealtime_insulin_units: str = ""
    correction_insulin_units: str = ""
    insulin_user_changes_units: str = ""

    def __init__(self, device: str = "",
                 sid: str = "",
                 device_timestamp: str = "",
                 record_type: str = "",
                 glucose_level_mg_dl: str = "",
                 glucose_scan_mg_dl: str = "",
                 none_numeric_fast_acting_insulin: str = "",
                 fast_acting_insulin_units: str = "",
                 none_numeric_food_data: str = "",
                 carbohydrates_gram: str = "",
                 carbohydrates_portion: str = "",
                 none_numeric_depot_insulin: str = "",
                 depot_insulin_units: str = "",
                 notes: str = "",
                 glucose_test_strips_mg_dl: str = "",
                 keton_mmol_l: str = "",
                 mealtime_insulin_units: str = "",
                 correction_insulin_units: str = "",
                 insulin_user_changes_units: str = "", ):
        self.device: str = device
        self.sid: str = sid
        try:
            self.device_timestamp = parser.parse(device_timestamp)
        except:
            pass
        self.record_type: str = record_type
        self.glucose_level_mg_dl: str = glucose_level_mg_dl
        self.glucose_scan_mg_dl: str = glucose_scan_mg_dl
        self.none_numeric_fast_acting_insulin: str = none_numeric_fast_acting_insulin
        self.fast_acting_insulin_units: str = fast_acting_insulin_units
        self.none_numeric_food_data: str = none_numeric_food_data
        self.carbohydrates_gram: str = carbohydrates_gram
        self.carbohydrates_portion: str = carbohydrates_portion
        self.none_numeric_depot_insulin: str = none_numeric_depot_insulin
        self.depot_insulin_units: str = depot_insulin_units
        self.notes: str = notes
        self.glucose_test_strips_mg_dl: str = glucose_test_strips_mg_dl
        self.keton_mmol_l: str = keton_mmol_l
        self.mealtime_insulin_units: str = mealtime_insulin_units
        self.correction_insulin_units: str = correction_insulin_units
        self.insulin_user_changes_units: str = insulin_user_changes_units
