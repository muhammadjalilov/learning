from django.db import models

from apps.account.models import Account
from apps.shared.models import SlugStampedModel, TimeStampedModel


class Quote(TimeStampedModel):
    body = models.TextField()
    quote_by = models.CharField(max_length=200, default='Some wise human')
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'

    def __str__(self):
        return self.body


class BlogPost(SlugStampedModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField()
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True, blank=True)


class BlogPostImage(models.Model):
    image = models.ImageField(upload_to='blog_posts/')
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)


class BlogPostComment(TimeStampedModel):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Blog Post Comment'
        verbose_name_plural = 'Blog Post Comments'

    def __str__(self):
        return self.body


