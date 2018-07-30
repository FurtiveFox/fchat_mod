import json
import requests
from .constants import flistEndpoints as E
from .constants import requestsConstants as R


class account:

    def __init__(self, username, userpass):
        self.username = username
        self.userpass = userpass
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': R.userAgent})

    def init_auth(self):
        """Authenticates with f-list web api to get full acount info"""
        payload = {'account': self.username, 'password': self.userpass, 'new_character_list': "true"}
        try:
            response = self.s.post(E.domain + E.getApiTicket, params=payload)
            response_dict = json.loads(response.text)
            self.acct_dict = response_dict
        except requests.exceptions.RequestException as e:
            print(e)

    def get_ticket(self):
        """Authenticates with f-list web api and requests minimal info"""
        payload = {'account': self.username, 'password': self.userpass, 'no_characters': 'true', 'no_friends': 'true', 'no_bookmarks': 'true'}
        response = self.s.post(E.domain + E.getApiTicket, params=payload)
        response_dict = json.loads(response.text)
        self.ticket = response_dict['ticket']
