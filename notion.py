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
    def create_page (self, description, date, status):
        create_url = "https://api.notion.com/v1/pages"


        data = {
            "parent": { "database_id":self.database_id },
            "properties": {
                "Description": {
                    "title": [
                        {
                            "text": {
                                "content": description
                            }
                        }
                    ]
                },
                "Date": {
                    "date": [
                        {
                            "text": {
                                "content": date
                            }
                        }
                    ]
                },
                "Food group": {
                    "select": {
                        "name": "Vegetable"
                    }
                },
                "Price": { "number": 2.5 }
            },
            "children": [
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "text": [{ "type": "text", "text": { "content": "Lacinato kale" } }]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                                    "link": { "url": "https://en.wikipedia.org/wiki/Lacinato_kale" }
                                }
                            }
                        ]
                    }
                }
            ]
        }'
