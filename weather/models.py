from django.db import models

class QueryHistory(models.Model):
    city_name = models.CharField(max_length=200)
    query_time = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.city_name} ({self.query_time})"

    class Meta:
        app_label = 'weather'
