# -*- coding: utf-8 -*-
from crontab import CronTab

class test_crontab():
    def __init__(self):
        self.my_cron=CronTab(user=True)
        self.command=''
        self.conment='test_crontab_job'
        self.time_m='*'
        self.time_h='*'
        self.day_d='*'
        self.day_m='*'
        self.day_y='*'
        pass

    def append(self):
        my_user_cron = self.my_cron
        job = my_user_cron.new(command='echo date >> ~/time.log')
        job.setall('*/2 * * * *')
        job.set_comment(self.conment)
        iter = my_user_cron.find_comment(self.conment)
        my_user_cron.write()
        print(iter)

    def isSave(self):
        my_user_cron = self.my_cron
        iter = my_user_cron.find_comment(self.conment)
        print(iter)

if __name__ == '__main__':
    test_crontab().append()
