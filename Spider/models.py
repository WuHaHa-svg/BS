import time
from django.db import models
from django.utils import timezone
from Log.models import LogModel


# from Utils.models import SaveModel


# Create your models here.

class TaskModel(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    url = models.CharField(max_length=2000)
    is_sql_scan = models.CharField(max_length=4, default='Y')
    is_xss_scan = models.CharField(max_length=4, default='Y')
    depth = models.IntegerField(default=0)
    max_depth = models.IntegerField(default=5)
    status_sql_scan = models.CharField(max_length=10, default='INIT')
    status_xss_scan = models.CharField(max_length=10, default='INIT')
    super_url = models.CharField(max_length=2000, null=True, blank=True)
    created_time = models.DateTimeField(null=True, blank=True)
    recv_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(int(time.time() * 1000))
        try:
            existing_obj = TaskModel.objects.get(url=self.url)
            self.id = existing_obj.id
            if not self.created_time:
                self.created_time = timezone.now()
            message = '任务URL："{}"已经存在，新任务将不再保存！'.format(self.url)
            log = LogModel(message=message)
            log.created_time = timezone.now()
            log.save()
        except TaskModel.DoesNotExist:
            xss = ''
            sql = ''
            if self.is_xss_scan == 'Y':
                xss = "XSS注入扫描开启！"
            else:
                xss = "XSS注入扫描关闭！"
            if self.is_sql_scan == 'Y':
                sql = "SQL注入扫描开启！"
            else:
                sql = "SQL注入扫描关闭！"
            message = '任务URL："{}"已经创建成功！'.format(self.url)
            message = message + sql + xss
            log = LogModel(message=message)
            log.created_time = timezone.now()
            log.save()
            page = SaveModel(id=self.id, url=self.url, is_save='N')
            page.save()
            message = '任务URL："{}"标签文件保存任务创建成功！'.format(self.url)
            log = LogModel(message=message)
            log.created_time = timezone.now()
            log.save()
        super(TaskModel, self).save(*args, **kwargs)


class SaveModel(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    url = models.CharField(max_length=2000)
    is_save = models.CharField(max_length=16, default='N')
