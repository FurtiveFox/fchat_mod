import json
import requests


""" https://toys.in.newtsin.space/api-docs/ """
domain = "https://f-list.net"
getApiTicket = "/json/getApiTicket.php"
mappingList = "/json/api/mapping-list.php"
characterData = "/json/api/character-data.php"
characterFriends = "/json/api/character-friends.php"
characterImages = "/json/api/character-images.php"
characterMemoGet = "/json/api/character-memo-get.php"
characterMemoSave = "/json/api/character-memo-save.php"
characterGuestbook = "/json/api/character-guestbook.php"
friendBookmarkLists = "/json/api/friend-bookmark-lists.php"
bookmarkAdd = "/json/api/bookmark-add.php"
bookmarkRemove = "/json/api/bookmark-remove.php"
friendRemove = "/json/api/friend-remove.php"
requestAccept = "/json/api/request-accept.php"
requestDeny = "/json/api/request-deny.php"
requestCancel = "/json/api/request-cancel.php"
requestSend = "/json/api/request-send.php"
# flist_reportSubmit = "/json/api/report-submit.php"


class account:

    def __init__(self, username, userpass):
        self.username = username
        self.userpass = userpass
        self.acctdata = self.init_auth(self.username, self.userpass)
        self.ticket = self.acctdata['ticket']
        self.defaultcharacter = self.acctdata['default_character']
        self.characters = self.acctdata['characters']
        self.friends = self.acctdata['friends']
        self.bookmarks = self.acctdata['bookmarks']

    def init_auth(self, username, password):
        """Authenticates with f-list web api to get full acount info"""
        payload = {'account': username, 'password': password}
        try:
            response = requests.post(domain + getApiTicket, params=payload)
            response_dict = json.loads(response.text)
            if response_dict['error'] is None:
                return response_dict
            else:
                print(response_dict['error'])
                return response_dict
        except requests.exceptions.RequestException as e:
            print(e)

    def get_ticket(self):
        """Authenticates with f-list web api and requests minimal info"""
        payload = {'account': self.username, 'password': self.userpass, 'no_characters': 'true', 'no_friends': 'true', 'no_bookmarks': 'true'}
        response = requests.post(domain + getApiTicket, params=payload)
        response_dict = json.loads(response.text)
        self.ticket = response_dict['ticket']
