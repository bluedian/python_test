# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import gs_config
import gs_crontab_def
import requests
import socket
import os


class server_status():
    def __init__(self):
        '''
        初始化
        '''
        self.indexName = 'server_status.py'
        self.version = '0.0.1'
        self.indexPath = os.path.abspath(os.path.dirname(__file__))
        self.indexPathName = self.indexPath + '/' + self.indexName

        self.indexCronComt = 'gsjob_server_status'
        self.indexCronTime = '*/2 * * * *'

        self.hostName = 'book_server'
        self.serverUrl = 'http://oa.9oe.com/index.php/book/apiserver'

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
    gs_class_self=server_status()

    if len(sys.argv) == 2:
        if sys.argv[1] == 'init':
            gs_class_self.init_cron()
        if sys.argv[1] == 'info':
            gs_class_self.info()
        if sys.argv[1] == 'del':
            gs_class_self.del_cron()
    else:
        gs_class_self.run()
