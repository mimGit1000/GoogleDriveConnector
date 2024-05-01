__author__ = 'mslone'

'''
Module to enable communction between python and Google Sheets
'''
import os
import pprint

import google.oauth2.credentials
from google.oauth2 import service_account

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google_auth_oauthlib.flow import Flow

class DriveConnector(object):
    def __init__(self, service_name, service_ver, conn_type='client_secret', conn_json='client_secret.json', scopes='https://www.googleapis.com/auth/drive'):
        
        self.conn_json = conn_json
        self.scopes = scopes
        self.service_name = service_name
        self.service_version = service_ver
        self.conn_type = conn_type

    @property
    def service_name(self):
        return self._service_name
    
    @service_name.setter
    def service_name(self,value):
        self._service_name = value

    def get_service(self):
        if self.conn_type == 'service_acct':
            creds = service_account.Credentials.from_service_account_file(self.conn_json, scopes=self.scopes)
        elif self.conn_type == 'client_secret':
            creds = Flow.from_client_secrets_file(self.conn_json, self.scopes)
        
        return build(self.service_name, self.service_version, credentials=creds)
    
    