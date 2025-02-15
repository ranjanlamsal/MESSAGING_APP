from celery import shared_task
from .utils import *

@shared_task
def send_email_task(subject, body, subscriber):        
    Util.send_email(subject, body, subscriber)
