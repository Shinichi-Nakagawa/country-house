from django.db import models


class HouseRecord(models.Model):
    created = models.DateTimeField(auto_now_add=True, primary_key=True)
    code = models.TextField()
    temperature = models.FloatField()
    memo = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey('auth.User', related_name='house_recordsR')

    class Meta:
        db_table = 'house_record'
        ordering = ('created',)
        unique_together = (('created', 'code'))