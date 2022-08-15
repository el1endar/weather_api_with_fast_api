import json


class Loader(object):

    @staticmethod
    def loadJson(path):

        with open(path) as file:
            return json.load(file)
