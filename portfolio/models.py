# portfolio/models.py
from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    client_name = models.CharField(max_length=255)
    developer_name = models.CharField(max_length=255)
    link = models.URLField()
    image = models.ImageField(upload_to='portfolio_images/')
    video = models.FileField(upload_to='portfolio_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
