from django.apps import AppConfig


class XssConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'XSS'

    def ready(self):
        from XSS.signals import task_start  # 引入signals模块
        from XSS.XssInjector import Injection
        task_start.connect(Injection)  # 连接信号与函数
