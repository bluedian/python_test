# -*- coding: utf-8 -*-
import sys
sys.path.append('.')
sys.path.append('..')
#import gs_config
from pro_book import gs_config
from unit_config import config_url
import requests
import socket


class book_server_status():
    def __init__(self):
        self.version = '0.0.1'
        self.hostName = 'book_server'
        self.serverUrl = 'http://oa.9oe.com/index.php/book/apiserver'

    def get_hostname(self):
        try:
            self.hostName = socket.gethostname()
        except:
            pass
        return self.hostName

    def update_status(self):
        statusurl = self.serverUrl
        try:
            statusurl = gs_config.url_server_status
        except:
            pass
        data = {
            'model': 'server_status_update',
            'server_info_name': self.get_hostname(),
        }
        html = requests.post(url=statusurl, data=data).text
        print(html)

    def run(self):
        self.update_status()


if __name__ == '__main__':
    book_server_status().run()
