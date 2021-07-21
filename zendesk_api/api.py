from requests.exceptions import HTTPError, ConnectionError
import requests


class ZendeskApiHandler:
    def __init__(self, domain, credentials={}):
        self.domain = domain
        self.credentials = credentials or {
            "username": '',
            "password": ''
        }

    def google_example(self):
        result = requests.get('https://google.ca')

        print(result.text)

    def create_ticket(self, assignee, priority, subject, body):
        payload = {
            assignee: {
                "id": "12345k",
            }
        }

        try:
            requests.post(f"{self.domain}/", data=payload,
                          auth=(self.credentials['username'], self.credentials['password']))

        except HTTPError as http_err:
            print(str(http_err))
        except ConnectionError as con_err:
            print(str(con_err))
