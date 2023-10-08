from django.apps import AppConfig

print('===========================================')
print('>>> Django code running from here... \n')
print('>>> this is apps.py <<<')

class JalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'JAL'

    def ready(self):
        # 在这里执行与模型相关的操作，因为此时模型已经加载完毕
        from JAL import models
