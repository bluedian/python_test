# -*- coding: utf-8 -*-
from crontab import CronTab

class gs_crontab():
    def __init__(self):
        self.my_cron=CronTab(user=True)
        self.command=''
        self.coment='test_crontab_job'
        self.time_m='*'
        self.time_h='*'
        self.day_d='*'
        self.day_m='*'
        self.day_y='*'

    def appendCron(self):
        self.delCron(self.coment)
        my_user_cron = self.my_cron
        job = my_user_cron.new(command='echo date >> ~/time.log')
        job.setall('*/2 * * * *')
        job.set_comment(self.coment)
        iter = my_user_cron.find_comment(self.coment)
        my_user_cron.write()
        print(iter)

    def appendCron10(self,comd='echo date >> ~/time.log',comt='test_crontab_job'):
        self.delCron(self.coment)
        my_user_cron = self.my_cron
        job = my_user_cron.new(command=comd)
        job.set_comment(comt)
        job.minute.every(10)
        my_user_cron.write()

    def appendCron_all(self,comd='echo date >> ~/time.log',comt='test_crontab_job'):
        self.delCron(self.coment)
        my_user_cron = self.my_cron
        job = my_user_cron.new(command=comd)
        job.minute.on(5)
        job.hour.every(10)  # Set to * */10 * * *
        job.dom.on(1)
        job.month.every(3)
        job.set_comment(comt)
        my_user_cron.write()

    def delCron(self,comt='test_crontab_job'):
        my_user_cron = self.my_cron
        iter = my_user_cron.find_comment(comt)
        print(my_user_cron.remove(iter))


if __name__ == '__main__':
    #test_crontab().appendCron()
    print('test------>')
    test_crontab().appendCron10()
