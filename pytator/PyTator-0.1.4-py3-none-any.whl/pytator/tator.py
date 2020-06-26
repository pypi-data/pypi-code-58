""" Python library for interacting with Tator REST API"""

import pytator.api as apiImpl
import argparse

try:
    import requests
except:
    print("Couldn't required libraries (might be in setup.py)")

def cli_parser(parser=None):
    """ Convenience function to return an argument parser with boiler-plate 
        required arguments for initializing a pytator.Tator

        :param argparse.ArgumentParser parser: A constructed parser (or None) 
    """
    if parser is None:
        parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--token", required=True)
    return parser

class Auth:
    def getToken(url, username, password):
        response=requests.post(url.rstrip('/') + '/' + 'Token',
                               json={'username': username,
                                     'password': password})
        if response.status_code==200:
            token_msg = response.json()
            return token_msg['token']
        else:
            print("ERROR: {}".format(response.json()))
            return None

class Tator:
    """
    Top-level module for access Tator API endpoints
    """
    def __init__(self, url, token, project):
        self.project = project
        self._url = url
        self._token = token
        self.Algorithm = apiImpl.Algorithm((url,token,project))
        self.Localization = apiImpl.Localization((url,token,project))
        self.LocalizationType = apiImpl.LocalizationType((url,token,project))
        self.Media = apiImpl.Media((url,token,project))
        self.MediaSection = apiImpl.MediaSection((url,token,project))
        self.MediaType = apiImpl.MediaType((url,token,project))
        self.Membership = apiImpl.Membership((url,token,project))
        self.Project = apiImpl.Project((url,token,None))
        self.State = apiImpl.State((url,token,project))
        self.StateType = apiImpl.StateType((url,token,project))
        self.Track = apiImpl.Track((url,token,project))
        self.TreeLeaf = apiImpl.TreeLeaf((url,token,project))
        self.TreeLeafType = apiImpl.TreeLeafType((url,token,project))
        self.User = apiImpl.User((url,token,None))
        self.Version = apiImpl.Version((url,token,project))
        self.GetFrame = apiImpl.GetFrame((url,token,project))
        self.StateGraphic = apiImpl.StateGraphic((url,token,project))
        self.TemporaryFile = apiImpl.TemporaryFile((url,token,project))

    def baseURL(self):
        """ Returns the URL for accessing site content """
        remove_rest = self._url.replace("/rest", "")
        return remove_rest + "/"

    def whoami(self):
        """ Returns current user """
        ep = self._url + "/User/GetCurrent"
        response = requests.get(
            ep,
            headers={"Authorization" : "Token {}".format(self._token),
                     "Content-Type": "application/json",
                     "Accept-Encoding": "gzip"},
        )
        return response.json()
