from tracemalloc import DomainFilter
import requests


class ZendeskApiHandler:
    def __init__(self, domain, credentials={}):
        self.domain = domain
        self.credentials = credentials or {
            "username": '',
            "password": ''
        }

    def create_ticket(self, assignee, priority, subject, body):
        payload = {
            "assignee": assignee,
            "priority": priority,
            "subject": subject,
            "body": body
        }

        try:
            requests.post(f"{self.domain}/", data=payload,
                          auth=(self.credentials['username'], self.credentials['password']))

        except requests.exceptions.HTTPError as http_err:
            print(str(http_err))
