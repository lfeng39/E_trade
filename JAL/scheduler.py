from django.test import TestCase
from JAL import models
from django.core.management.base import BaseCommand
from django.utils import timezone
import schedule
import time

class Command(BaseCommand):
    help = 'Run scheduled tasks'

    def handle(self, *args, **options):
        # 定义定时任务
        def job():
            # 获取当前时间
            current_time = timezone.now()

            # 打印当前时间
            print("Current Time:", current_time)

        # 每隔一分钟执行一次 job 函数
        schedule.every(1).minutes.do(job)

        while True:
            # 运行任务调度器
            schedule.run_pending()

            # 等待一段时间，比如0.1秒
            time.sleep(0.1)