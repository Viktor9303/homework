from datetime import datetime
from calendar import isleap
import unittest

def CalculateDueDate(submit_date,turnaround):
    #submit date: [2023,5,16,9,20]-->2023.5.16 9:20
    year = submit_date[0]
    month = submit_date[1]
    day = submit_date[2]
    hour = submit_date[3]
    minute = submit_date[4]

    is_leap_year = isleap(year)
    current_year = Logic.get_month_dict(is_leap_year)
    max_day = current_year[str(month)]

    is_completed_today = turnaround + hour < 17
    # one day is enough for finishing the task
    if is_completed_today:
        hour += turnaround
        return datetime(year, month, day, hour, minute)


    #need more than one day to finish the task
    if not is_completed_today:
        hour_to_work = 17 - hour
        turnaround -= hour_to_work
        day += 1
        while True:
            if turnaround < 8:
                return datetime(year, month, day, hour + turnaround, minute)
            turnaround -= 8
            year, month, day = Logic.get_next_week_day(year,month,day,max_day)
            max_day = current_year[str(month)]






class Logic:
    @staticmethod
    def is_week_day(year,month,day):
        today = datetime(year,month,day)
        if today.weekday() < 5:
            return True
        else:
            return False

    @staticmethod
    def get_next_week_day(year, month ,day,max_day):
        day, month, year = Logic.increase_day(day,max_day,month,year)
        if Logic.is_week_day(year,month,day):
            return year,month,day

        while True:
            if Logic.is_week_day(year, month, day):
                return year, month, day
            else:
                day, month, year = Logic.increase_day(day=day,month = month,year = year,max_day=max_day)


    @staticmethod
    def increase_day(day, max_day, month, year):
        if max_day == day:
            if month == 12:
                month = 1
                day = 1
                year += 1
            else:
                month += 1
                day = 1
        else:
            day += 1
        return day, month, year

    @staticmethod
    def get_month_dict(is_leap_year):
        if is_leap_year:
            return  {"1": 31, "2": 29, "3": 31, "4": 30, "5": 31, "6": 30,
                 "7": 31, "8": 31, "9": 30, "10": 31, "11": 30, "12": 31}
        return  {"1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6": 30,
                 "7": 31, "8": 31, "9": 30, "10": 31, "11": 30, "12": 31}


class TestMain(unittest.TestCase):
    def test_one_day(self):
        self.assertEqual(CalculateDueDate([2023,5,16,9,20],4), datetime(2023, 5, 16, 13, 20))
        self.assertEqual(CalculateDueDate([2023,5,17,10,20],4), datetime(2023, 5, 17, 14, 20))

    def test_two_day(self):
        self.assertEqual(CalculateDueDate([2023,5,16,9,20],8), datetime(2023, 5, 17, 9, 20))
        self.assertEqual(CalculateDueDate([2023,5,17,9,20],10), datetime(2023, 5, 18, 11, 20))

    def test_one_week(self):
        self.assertEqual(CalculateDueDate([2023,5,16,9,20],40), datetime(2023, 5, 23, 9, 20))

    def test_one_year(self):
        self.assertEqual(CalculateDueDate([2023,5,14,9,20],40*52),datetime(2024, 5, 13, 9, 20))





print(CalculateDueDate([2023,5,14,9,20],40*52))




