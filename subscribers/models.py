from django.db import models


class Subscriber(models.Model):
  """A subscriber model."""  

  email = models.CharField(max_length=100, blank=False, null=False, help_text='Email address')
  full_name = models.CharField(max_length=100, blank=False, null=False, help_text='First and last name')

  def __str__(self):
    return self.full_name

  class Meta: # noqa
    verbose_name = "ニュースレター購読者"
    verbose_name_plural = "ニュースレター購読者"
