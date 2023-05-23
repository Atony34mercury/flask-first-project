import requests
import json

class DatabaseCnx():
    
    def __init__(self) -> None:   
      self.url_get = "https://us-east-1.aws.data.mongodb-api.com/app/data-vplka/endpoint/data/v1/action/find"
      self.url_create = "https://us-east-1.aws.data.mongodb-api.com/app/data-vplka/endpoint/data/v1/action/insertOne"
      self.url_delete = "https://us-east-1.aws.data.mongodb-api.com/app/data-vplka/endpoint/data/v1/action/deleteOne"

      self.create_json = {
          "collection": "Conditions",
          "database": "Testing",
          "dataSource": "TestingDB",
          "document": {
              "name": "John Sample",
              "age": 42
            }
      }

      self.get_json = {
          "collection": "Conditions",
          "database": "Testing",
          "dataSource": "TestingDB",
          "filter": { 
              # "column1": "CustomerNumber"
          }
      }

      self.delete_json = {
          "collection": "Conditions",
          "database": "Testing",
          "dataSource": "TestingDB",
          "document": {
              "name": "John Sample",
              "age": 42
            }
      }

    def databaseAction(self, action:str = "", document:dict = {}) -> str:
      """
        Description:
          Make a request to the API
        Parameters:
          action -> It can be "create,delete,get,update"
          document -> document that you want to manipulate
      """
      json_data = ""
      final_url = ""
      if(action.lower() in "create"):
        json_data = self.create_json
        json_data["document"] = document
        final_url = self.url_create
      elif (action.lower() in "delete"):
        json_data = self.delete_json
        json_data["document"] = document
        final_url = self.url_delete
      else:
        json_data = self.get_json
        json_data["filter"] = document
        final_url = self.url_get

      payload = json.dumps(json_data)

      headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': "AFDSUypfm5wMdJ8Y8MdgEX3dSFCkFjqxVNisw1gAjQbsazxNCOKVT4fXXNB5R2UB", 
      }

      response = requests.request("POST", final_url, headers=headers, data=payload)

      print(response.text)

      return response.status_code,response.text
