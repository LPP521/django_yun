from django.db import models


class File(models.Model):
    _file_id = models.AutoField(
        primary_key=True
    )
    _file_name = models.CharField(
        max_length=225,
        verbose_name="文件名称",
        default=''
    )
    file_type = (
        ('apk', 'apk'),
        ('exe', 'exe'),
        ('unknow', 'unknow'),
    )
    _file_type = models.CharField(
        max_length=50,
        choices=file_type,
        default='',
    )
    _file_size = models.IntegerField(
        verbose_name="文件大小",
        default=0
    )
    _file_path = models.CharField(
        max_length=225,
        verbose_name="文件路径",
        default=''
    )
    file_md5 = models.CharField(
        max_length=50,
        default=''
    )
    _upload_data = models.DateField(
        auto_now=True
    )
    _upload_time = models.TimeField(
        auto_now=True
    )

    def __str__(self):
        return str(self._file_name)
