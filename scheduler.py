import sys
import src as app


if __name__ == '__main__':
    initial_time, range_days, companies = app.parse_args(sys.argv[1:])
    allowed_times = app.get_weekdays_for_scheduling(range_days, initial_time)

    schedule = app.scheduler(companies, allowed_times)

    for s in schedule:
        print("{}\n".format(s))
