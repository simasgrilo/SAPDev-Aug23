import json
#import PyYAML
from typing import List
from UnsuportedFormatException import UnsuportedFormatException
from connection import requisition as r


class TaskFour:
    #access https://api.sap.com/ to get the api endpoint specs as json and yaml:

    __requisitioner__ = r.Requisition()

    def parse_spec(self, file_name: str, file_ext: str):
        if file_ext != "JSON" and file_ext != "YAML":
            raise UnsuportedFormatException("Please specify a JSON or YAML file.")
        file_str = ""
        with open(file_name, "rt") as fp:
            for line in fp:
                file_str += line
        resulting_endpoint = ""
        filter_endpoints = []
        if file_ext.lower() == 'json':
            endpoints = json.loads(file_str)
            for endpoint, properties in endpoints["paths"].items():
                if properties["get"] is not None and properties["get"]["produces"][0] == "application/json":
                    filter_endpoints.append(endpoint)
            filter_endpoints.sort()
            resulting_endpoint = ":".join(filter_endpoints)

        #elif file_ext == 'YAML':
            #TODO
        return resulting_endpoint

    def hash_value(self,file_name: str, file_ext: str):
        return self.__requisitioner__.getHash(self.parse_spec(file_name,file_ext))

