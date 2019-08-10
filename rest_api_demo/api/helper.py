import flask_restplus
import json
import os
import yaml

url = "http://localhost:8888/api"
yml_dirname = "\\ymls\\"
curr_dir = os.path.dirname(os.path.abspath(__file__))
yml_dir = curr_dir + yml_dirname


class Helper(object):

    def __init__(self):
        self.id = 0

    def get(self):
        files = [f for f in os.listdir(yml_dir) if os.path.isfile(os.path.join(yml_dir, f))]
        return files

    def get_yml(self, name):
        file_fpath = yml_dir + name + ".yml"
        with open(file_fpath, 'r') as f:
            data = f.read()
        print(yaml.safe_load(data))
        return yaml.safe_load(data)