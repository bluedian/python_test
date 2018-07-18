# -*- coding: utf-8 -*-
from crontab import CronTab
import os


def appendCron(comt='test_crontab_job'):
    delCron(comt)
    my_user_cron = CronTab(user=True)
    job = my_user_cron.new(command='echo date >> ~/time.log')
    job.setall('*/2 * * * *')
    job.set_comment(comt)
    my_user_cron.write()

def delCron(comt='test_crontab_job'):
    my_user_cron = CronTab(user=True)
    iter = my_user_cron.find_comment(comt)
    print(my_user_cron.remove(iter))
    my_user_cron.write()

def appendCron0(min=2,comd='echo date >> ~/time.log',comt='test_crontab_job'):
    delCron(comt)
    my_user_cron = CronTab(user=True)
    job = my_user_cron.new(command=comd)
    job.set_comment(comt)
    job.minute.every(min)
    my_user_cron.write()

def appendCron5(comd='echo date >> ~/time.log',comt='test_crontab_job'):
    delCron(comt)
    my_user_cron = CronTab(user=True)
    job = my_user_cron.new(command=comd)
    job.set_comment(comt)
    job.minute.every(5)
    my_user_cron.write()

def appendCron10(comd='echo date >> ~/time.log',comt='test_crontab_job'):
    delCron(comt)
    my_user_cron = CronTab(user=True)
    job = my_user_cron.new(command=comd)
    job.set_comment(comt)
    job.minute.every(10)
    my_user_cron.write()

def appendCron_all(comd='echo date >> ~/time.log',comt='test_crontab_job'):
    delCron(comt)
    my_user_cron = CronTab(user=True)
    job = my_user_cron.new(command=comd)
    job.minute.on(5)
    job.hour.every(10)  # Set to * */10 * * *
    job.dom.on(1)
    job.month.every(3)
    job.set_comment(comt)
    my_user_cron.write()




