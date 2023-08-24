

import requests
import json

class Requisition:

    __HASH_URL__ = "https://developer-challenge.cfapps.eu10.hana.ondemand.com"
    __HASH_ENDPOINT__ = "/v1/hash"
    __COMMUNITY_ID__ = "erickgrilo"
    __NORTHBREEZE_ENDPOINT__ = "https://developer-challenge.cfapps.eu10.hana.ondemand.com/odata/v4/northbreeze/"

    def getHash(self, value : str):
        reqHeaders = {
            "CommunityID" : self.__COMMUNITY_ID__
        }
        value = "(value=\'{}\')".format(value)
        req = requests.get(self.__HASH_URL__ + self.__HASH_ENDPOINT__ + value, headers=reqHeaders)
        if req.status_code != 200:
            return json.loads(req.content)
        return req.content

    def getCommunityId(self):
        return self.__COMMUNITY_ID__

    def getNorthbreezeURL(self):
        return self.__NORTHBREEZE_ENDPOINT__



