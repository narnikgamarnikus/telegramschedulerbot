import ujson as json

from celery import shared_task

from django.dispatch import receiver

from django.db.models.signals import pre_save, post_save

from .models import Scheduler

from annoying.functions import get_object_or_None

from django.utils import timezone

import telegram

bot = telegram.Bot(token='379009194:AAG60zqmbY0-fkM6hLgmC_QgoQPpiWvLA5A')


@receiver(post_save, sender=Scheduler)
def create_scheduler(sender, instance, created, **kwargs):
	if created:
		bot.send_message(chat_id='412866215', text=instance.message)
		start_scheduler.apply_async(args=(instance.pk), retry=True)
		print('start_scheduler')
		send_message.apply_async(args=(instance.pk), retry=True)
		print('send_message')


@shared_task
def start_scheduler(scheduler_pk):
	print('start_scheduler')
	print('start_scheduler')
	scheduler = get_object_or_None(Scheduler, pk=schedule_pk)
	print(scheduler)
	if scheduler:
		countdown = timezone.now() - scheduler.datetime
		print(countdown)
		send_message.apply_async(args=(scheduler_pk, ), countdown=int(countdown.seconds)*60)


@shared_task
def send_message(scheduler_pk):
	print('send_message')
	scheduler = get_object_or_None(Scheduler, pk=scheduler_pk)
	if scheduler and not scheduler.one_time:
		bot.send_message(chat_id='412866215', text=scheduler.message)
		#print('send notification')
		send_message.apply_async(args=(scheduler_pk, ), countdown=int(scheduler.every)*60)
	elif scheduler and scheduler.one_time:
		#print('send notification one time')
		bot.send_message(chat_id='412866215', text=scheduler.message)

