from apscheduler.schedulers.background import BackgroundScheduler
from yminer.crypto.cmc import update_crypto_tables
from datetime import datetime


def yminer_service():

    update_crypto = update_crypto_tables
    CRYPTO_JOB_FREQUENCY = 1 # in hours

    sched = BackgroundScheduler(daemon=True)
    sched.add_job(update_crypto,'interval',minutes=60, next_run_time=None) #datetime.now()
    sched.start()
    
