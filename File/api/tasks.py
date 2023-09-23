from celery.utils.log import get_task_logger
from celery import shared_task

from .utils import upload_check


logger = get_task_logger(__name__)


@shared_task()
def check_file(data):
    """Обрабатывает файл и ставит флажек processed"""
    logger.info('Обработка данных')
    return upload_check(data)
