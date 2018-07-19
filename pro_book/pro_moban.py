# -*- coding: utf-8 -*-
import os, sys

sys.path.append('..')

import bese_crontab


class pro_moban():
    def __init__(self):
        self.version = '0.0.1'
        self.indexPath = os.path.abspath(os.path.dirname(__file__))
        self.indexName = 'pro_moban.py'
        self.indexPathName = self.indexPath + '\\' + self.indexName
        self.indexRun = 'python3 ' + self.indexPathName
        self.indexCronComt = 'gsjob_pro_moban'
        self.indexCronTime = '*/2 * * * *'
        pass

    def info(self):
        print('version:', self.version)
        print('indexName:', self.version)
        print('indexCronTime:', self.indexCronTime)
        print('indexCronComt:', self.indexCronComt)
        print('RUN:', self.indexRun)

    def init_cron(self):
        print('init')
        # pass
        cron = bese_crontab.bese_crontab()
        cron.appendCron(setmin=2, comd='python3 ' + self.indexPathName, comt=self.indexCronComt)

    def run(self):
        print('run')
        pass


if __name__ == '__main__':

    if len(sys.argv) == 2:
        if sys.argv[1] == 'init':
            pro_moban().init_cron()
        if sys.argv[1] == 'info':
            pro_moban().info()
    else:
        pro_moban().run()
