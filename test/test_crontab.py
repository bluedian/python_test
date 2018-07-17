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

    def appendCron(self):
        my_user_cron = self.my_cron
        job = my_user_cron.new(command='echo date >> ~/time.log')
        job.setall('*/2 * * * *')
        job.set_comment(self.conment)
        iter = my_user_cron.find_comment(self.conment)
        my_user_cron.write()
        print(iter)

    def isCron(self):
        my_user_cron = self.my_cron
        iter = my_user_cron.find_comment(self.conment)

        for cron in my_user_cron:
            print(cron)

        print(iter)
        if iter is None:
            print('不存在')
        else:
            print('找到了')

    def delCron(self):
        my_user_cron = self.my_cron
        iter = my_user_cron.find_comment(self.conment)
        print(my_user_cron.remove(iter))


if __name__ == '__main__':
    #test_crontab().appendCron()
    print('test------>')
    test_crontab().delCron()
