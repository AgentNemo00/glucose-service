
def map_keys(key: str) -> str:
    if key == "Gerät":
        return "device"
    if key == "Seriennummer":
        return "sid"
    if key == "Gerätezeitstempel":
        return "device_timestamp"
    if key == "Aufzeichnungstyp":
        return "record_type"
    if key == "Glukosewert-Verlauf mg/dL":
        return "record_type"
    if key == "Glukose-Scan mg/dL":
        return "glucose_level_mg_dl"
    if key == "Nicht numerisches schnellwirkendes Insulin":
        return "none_numeric_fast_acting_insulin"
    if key == "Schnellwirkendes Insulin (Einheiten)":
        return "fast_acting_insulin_units"
    if key == "Nicht numerische Nahrungsdaten":
        return "none_numeric_food_data"
    if key == "Kohlenhydrate (Gramm)":
        return "carbohydrates_gram"
    if key == "Kohlenhydrate (Portionen)":
        return "carbohydrates_portion"
    if key == "Nicht numerisches Depotinsulin":
        return "none_numeric_depot_insulin"
    if key == "Depotinsulin (Einheiten)":
        return "depot_insulin_units"
    if key == "Notizen":
        return "notes"
    if key == "Glukose-Teststreifen mg/dL":
        return "glucose_test_strips_mg_dl"
    if key == "Keton mmol/L":
        return "keton_mmol_l"
    if key == "Mahlzeiteninsulin (Einheiten)":
        return "mealtime_insulin_units"
    if key == "Korrekturinsulin (Einheiten)":
        return "correction_insulin_units"
    if key == "Insulin-Änderung durch Anwender (Einheiten)":
        return "insulin_user_changes_units"
    return ""  # default return typ. This should not happened
