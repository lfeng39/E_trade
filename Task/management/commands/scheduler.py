# myapp/management/commands/scheduler.py

import schedule
import datetime, time, zoneinfo, pytz
from django.core.management.base import BaseCommand
from Task import task
from JAL import models, urls, spider, images, forms, verify


class Command(BaseCommand):
    help = 'Run scheduled tasks'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Scheduler is running...'))
        '''
        do it
        '''
        def job():
            # # 获取当前时间
            current_time = datetime.datetime.now(tz=spider._shanghai_).strftime(spider._format_)
            print('SHA: ',current_time)
            # task.sendMail()

        '''
        do time
        '''
        # schedule.every().seconds.do(job)
        # schedule.every().minutes.do(job)
        # schedule.every().hour.do(job)
        schedule.every().day.at('21:15').do(job)
        schedule.every().monday.do(job)
        schedule.every().wednesday.at('13:15').do(job)
        schedule.every().minute.at(':17').do(job)

        while True:
            # 运行任务调度器
            schedule.run_pending()
            print(datetime.datetime.now(tz=spider._shanghai_).strftime(spider._format_))
            # 等待一段时间，比如0.1秒
            time.sleep(3)
            # if datetime.datetime.now(tz=spider._shanghai_).strftime('%S') == '00':
            #     print(datetime.datetime.now(tz=spider._shanghai_).strftime(spider._format_))