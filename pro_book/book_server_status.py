# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import gs_config
import gs_crontab_def
import requests
import socket
import os


class book_server_status():
    def __init__(self):
        self.version = '0.0.2'
        self.indexPath=os.path.abspath(os.path.dirname(__file__))
        self.indexName='book_server_status.py'
        self.indexPathName=self.indexPath+'\\'+self.indexName
        self.indexCronComt='job_book_server_status'
        self.hostName = 'book_server'
        self.serverUrl = 'http://oa.9oe.com/index.php/book/apiserver'

    def print_path(self):
        print(self.indexPathName)

    def init_crontab(self):
        commond='python3 '+self.indexPathName
        comment=self.indexCronComt
        print(commond,comment)
        gs_crontab_def.appendCron10(comd=commond,comt=comment)

        #gs_crontab.appendCron10(comd=commond,comt=comment)

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

    if len(sys.argv)==2:
        if sys.argv[1]=='init':
            #print('init')
            book_server_status().init_crontab()
    else:
        #print('aaaa')
        book_server_status().run()