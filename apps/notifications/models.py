from django.db import models


class PeriodNotifications(models.Model):
    title = models.TextField()
    account = models.ForeignKey('account.Account', on_delete=models.CASCADE, related_name='notifications')

    class Meta:
        verbose_name = 'PeriodNotification'
        verbose_name_plural = 'PeriodNotifications'

    def __str__(self):
        return self.title
