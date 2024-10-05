from django.db import models


class NewsletterEmails(models.Model):
    email = models.EmailField()
    remote_address = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return f'{self.email}'
