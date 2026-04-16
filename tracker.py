import json
import os

def create_library():
    # create only if library.json doesn't already exist
    if not os.path.exists("library.json"):
        data = []
        with open("library.json", "w") as json_file:
            json.dump(data, json_file, indent=2)