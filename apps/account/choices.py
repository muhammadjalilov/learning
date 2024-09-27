from django.db import models


class AccountSubscriptions(models.TextChoices):
    STARTER = 'starter', 'Starter'
    LEARNER = 'learner', 'Learner'
    MASTER = 'master', 'Master'
