import urllib.parse

from requisition import Requisition
import requests
import json
from urllib import parse

class TaskThree:

    __REQUISITION__ = Requisition()
    __ODATA_ACTION__ = "selectProduct"


    def selectProducts(self):
        community_id = self.__REQUISITION__.getCommunityId()
        headers = {
            "Accept" : "application/json",
        }
        content = {
            "communityid": community_id
        }
        req = requests.post(url=self.__REQUISITION__.getNorthbreezeURL() + self.__ODATA_ACTION__, headers=headers, json=content)
        if req.status_code != 200:
            return req.content
        return json.loads(req.content)["value"]

    def getHashForProducts(self):
        return self.__REQUISITION__.getHash(urllib.parse.quote(self.selectProducts()))

