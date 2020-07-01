from django.db import models


# Create your models here.
class Script(models.Model):
    """
    脚本
    """
    script_name = models.CharField(max_length=32, verbose_name='脚本名称')
    script_content = models.TextField(verbose_name='脚本内容')
    default_params = models.CharField(max_length=64, verbose_name='默认参数', default='')
    script_desc = models.CharField(max_length=32, verbose_name='脚本描述')

    class Meta:
        app_label = "apitest"
        verbose_name = "任务"
        verbose_name_plural = "任务"


class Operation(models.Model):
    """
    执行记录
    """
    user = models.CharField(max_length=32, verbose_name='用户')
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='开始时间')
    end_time = models.DateTimeField(auto_now_add=True, verbose_name='结束时间')
    biz = models.CharField(max_length=32, verbose_name='业务')
    machine_numbers = models.IntegerField(verbose_name='机器数')
    result = models.BooleanField(verbose_name='状态')
    script_id = models.IntegerField(verbose_name='脚本id')
    log = models.TextField(verbose_name='日志详情')
    status = models.TextField(default=-1, verbose_name='状态')

    class Meta:
        app_label = "apitest"                # 属于哪个app
        verbose_name = "执行记录"             # admin显示的名称
        verbose_name_plural = "执行记录"      # 复数形式
