from datetime import datetime, timedelta
from src.schedule_entry import ScheduleEntry
from src.schedule_queue import ScheduleQueue


def scheduler(argcompanies, times):
    queue = ScheduleQueue.from_list(argcompanies)
    schedule_times = []
    for time in times:
        ret_time = time + timedelta(days=1)
        if ret_time.weekday() < 5:
            company = queue.repop()
            schedule_times.append(ScheduleEntry(company, time, ret_time))
    return schedule_times


def parse_args(args):
    if len(args) < 3:
        print("Please give an initial time, a max number of dates and at least one company")
        exit(1)
    time = datetime.fromisoformat(args[0])
    days = int(args[1])
    provided_companies = args[2:]
    return time, days, provided_companies


def get_weekdays_for_scheduling(days, init_time):
    weekdays = [init_time]
    i = 0
    while len(weekdays) < days+1:
        if i % 2 == 0:
            depart_date = init_time + timedelta(days=i + 2)
            if depart_date.weekday() < 5 or depart_date.weekday() == 6:
                weekdays.append(depart_date)
        i += 1
    return weekdays
