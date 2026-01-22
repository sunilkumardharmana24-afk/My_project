import json

def read_json(file_path):
    with open(file_path) as file:
        testdata = json.load(file)
    return testdata

def read_json_multiple(file_path1):
    with open(file_path1) as file1:
        testdata2 = json.load(file1)
    return testdata2