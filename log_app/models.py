from django.db import models


class RequestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    query_params = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=50)
    response_code = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.timestamp} - {self.method} {self.path}"
