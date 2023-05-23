from django.apps import AppConfig


class SqlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SQL'

    def ready(self):
        from SQL.signals import task_start  # 引入signals模块
        from SQL.SqlInjector import Injection
        task_start.connect(Injection)  # 连接信号与函数
