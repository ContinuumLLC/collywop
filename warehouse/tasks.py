from celery.task.schedules import crontab
from celery.decorators import periodic_task
from warehouse.utils import scrapers
from celery.utils.log import get_task_logger
from datetime import datetime

logger = get_task_logger(__name__)
from .models import IsAlive

# A periodic task that will run every minute (the symbol "*" means every)

'''
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def is_alive():
    logger.info("Start task")
    now = datetime.now()
    r = IsAlive(result=now)
    r.save()

@periodic_task(run_every=(crontab(hour="*", minute="0", day_of_week="*")))
def budget_update():
    scrapers.budget()
'''
