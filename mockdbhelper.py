#!/usr/bin/python2
# coding=utf-8
# @Date: 7/23/18
# @Author: HZH
"""

"""
import datetime

MOCK_USERS = [{'email': 'test@example.com',
               'salt': 'JCNMR4z/iHINHytlh9FZpiES9zI=',
               'hashed': "5fa1147f3e9faf6824f4487b68c3d39170727d5b9207381f1dd2ea0ae1cac5b8ab31ed5814f3af425310cf12e3624c0f93437f051419727fadc89ab8bd39d24a"
               }]

MOCK_TABLES = [{"_id": "1", "number": "1", "owner": "test@example.com", "url": "mockurl"}]

MOCK_REQUESTS = [{"_id": "1", "table_number": "1", "table_id": "1", "time": datetime.datetime.now()}]

class MockDBHelper:
    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get("email") == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({
            "email": email,
            "salt": salt,
            "hashed": hashed
        })

    def add_table(self, number, owner):
        MOCK_TABLES.append({"_id": number, "number": number, "owner": owner})
        return number

    def update_table(self, _id, url):
        for table in MOCK_TABLES:
            if table.get("_id") == _id:
                table["url"] = url
                break

    def get_tables(self, ownere_id):
        return MOCK_TABLES

    def get_table(self, table_id):
        for table in MOCK_TABLES:
            if table.get("_id") == table_id:
                return table

    def delete_table(self, table_id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get("_id") == table_id:
                del MOCK_TABLES[i]
                break


    def add_request(self, table_id, time):
        table = self.get_table(table_id)
        MOCK_REQUESTS.append({"_id": table_id, "owner": table["owner"], "table_number": table["number"],
                              "table_id": table_id, "time": time})

    def get_requests(self, owner_id):
        return MOCK_REQUESTS

    def delete_request(self, request_id):
        for i, request in enumerate(MOCK_REQUESTS):
            if request.get("_id") == request_id:
                del MOCK_REQUESTS[i]
                break
