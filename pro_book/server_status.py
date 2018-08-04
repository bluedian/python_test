# -*- coding: utf-8 -*-
import sys, os
sys.path.append('..')

import requests
import socket
import json

import bese_config
import bese_crontab

class server_status():
    def __init__(self):
        '''
        初始化
        '''
        self.indexName = 'server_status.py'
        self.version = '0.0.5'
        self.indexPath = os.path.abspath(os.path.dirname(__file__))
        self.indexPathName = self.indexPath + '/' + self.indexName

        self.indexCronComt = 'gsjob_server_status'
        self.indexCronTime = '*/3 * * * *'

        self.hostName = 'book_server'
        # self.serverUrl = 'http://oa.9oe.com/index.php/book/apiserver'

    def info(self):
        '''
        显示类的基本信息
        :return:
        '''
        print('indexName:', self.indexName)
        print('version:', self.version)
        print('indexCronTime:', self.indexCronTime)
        print('indexCronComt:', self.indexCronComt)

    def init_cron(self):
        '''
        增加类的时间任务执
        :return:
        '''
        print('init_cron')
        commond = 'python3 ' + self.indexPathName
        comment = self.indexCronComt
        cron = bese_crontab.bese_crontab()
        cron.appendCron(setmin=2, comd=commond, comt=comment)

    def del_cron(self):
        '''
        清理类的所有时间任务
        :return:
        '''
        print('del_cron')
        cron = bese_crontab.bese_crontab()
        cron.delCron(comt=self.indexCronComt)

    def get_hostname(self):
        try:
            self.hostName = socket.gethostname()
        except:
            pass
        return self.hostName

    def update_status(self):
        try:
            urlServer = bese_config.urlServer
        except:
            pass
        data = {
            'model': 'status',
            'server_hostname': self.get_hostname(),
            'server_version': self.version,
        }
        html = requests.post(url=urlServer, data=data).text
        print(html)
        try:
            json_html = json.loads(html)
            print(json_html['result'])
            print(json_html['result']['version'])
            if self.version == json_html['result']['version']:
                print('OK')
            else:
                self.update_git()
        except:
            pass


    def update_git(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        os.system('cd %s && git pull' % path)
        print('up version:', self.version)


    def run(self):
        print(bese_config.urlServer)
        self.update_status()

if __name__ == '__main__':
    gs_class_self = server_status()

    if len(sys.argv) == 2:
        if sys.argv[1] == 'init':
            gs_class_self.init_cron()
        if sys.argv[1] == 'info':
            gs_class_self.info()
        if sys.argv[1] == 'del':
            gs_class_self.del_cron()
        if sys.argv[1] == 'up':
            gs_class_self.update_git()
    else:
        gs_class_self.run()
