import json
from typing import List

class SAPDevTask1():


    def getContent(self, message : str) -> List[str]:
        """
        :param message: String message in JSON format to be parsed
        :return: list of attributes that met the criteria 'kind' == 'EntitySet' in the json.
        """
        content = json.loads(message)['value']
        entityNames = []
        for item in content:
            if item['kind'] == "EntitySet":
                entityNames.append(item['name'])
        entityNames.sort()
        return entityNames
