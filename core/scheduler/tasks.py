from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from core.handlers.play import play_scheduler


# Time Tasks
def scheduler_tasks():
    scheduler = AsyncIOScheduler(timezone="Europe/Kiev")
    # scheduler.add_job(play_scheduler, trigger='cron', minute='*', kwargs={'bot': bot})
    return scheduler
