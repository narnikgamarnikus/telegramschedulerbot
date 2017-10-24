from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from multiselectfield import MultiSelectField

@python_2_unicode_compatible
class Scheduler(models.Model):

	WEEK_DAYS = (('Monday', 'Monday'),
               	   ('Tuesday', 'Tuesday'),
               	   ('Wednesday', 'Wednesday'),
                   ('Thursday', 'Thursday'),
                   ('Friday', 'Friday'),
                   ('Saturday', 'Saturday'),
                   ('Sunday', 'Sunday'))

	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
	message = models.CharField(max_length=500)
	one_time = models.BooleanField(default=False)
	every = models.PositiveSmallIntegerField(
		default=0,
		verbose_name = _('Every'),
		help_text = _('The message will be sent each N number of minutes'),
		null=True, 
		blank=True
		)
	start_datetime = models.DateTimeField(null=True, blank=True)
	send_datetime = models.DateTimeField(null=True, blank=True)
	end_datetime = models.DateTimeField(null=True, blank=True)
	days = MultiSelectField(choices=MY_CHOICES)


	def __str__(self):
		return self.message[:25]

	def get_absolute_url(self):
		return reverse('schedulers:detail', kwargs={'pk': self.pk})