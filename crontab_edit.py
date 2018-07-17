# -*- coding: utf-8 -*-
from crontab import CronTab

my_user_cron = CronTab(user=True)

job = my_user_cron.new(command='echo date >> ~/time.log')

job.setall('*/2 * * * *')

job.set_comment("time log job")

iter = my_user_cron.find_comment('time log job')

my_user_cron.write()

print(iter)