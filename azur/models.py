from django.db import models


class WebPage(models.Model):
    visited = models.DateTimeField()
    tag = models.CharField(max_length=128)
    url = models.TextField()
    domain = models.TextField()
    time_to_load = models.IntegerField()
    load_code = models.IntegerField()
    size = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'web pages'

    def __str__(self):
        return self.domain

