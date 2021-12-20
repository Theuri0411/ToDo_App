import json
import requests



class NotionClient:
    def __init__(self, token, database_id) -> None:
        self.database_id = database_id
        self.headers = {
            "Authorization": "Bearer" + token,
            "Content-Type" : "application/json",
            "Notion-Version" : "2021-08-16"
        }
    def create_page (self, decription, date, status):
        pass
    