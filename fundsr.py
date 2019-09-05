from datetime import datetime, timedelta
from pytz import timezone, country_timezones


class FundSR(object):

    def free_charge_days(self, year, month, day, hour):
        tz = timezone(country_timezones('cn')[0])
        date = datetime(year, month, day, hour, minute=0, second=0, tzinfo=tz)

        # 调整申购日
        date = self.regulate_date(date, hour)

        # 赎回日
        rdate = date + timedelta(days=7)

        return ("申购确认日: %d-%d-%d 星期%s\r\n"
                "可赎回日: %d-%d-%d 星期%s"
                % (date.year, date.month, date.day, date.isoweekday(),
                   rdate.year, rdate.month, rdate.day, rdate.isoweekday()))


    def regulate_date(self, date, hour):
        holiday = self.holiday()

        # 节假日
        if date.month in holiday.keys() and date.day in holiday[date.month]:
            diff = len(holiday[date.month]) - holiday[date.month].index(date.day)
            date += timedelta(days=diff)

        # 周末
        date = self.is_weekend(date, hour)

        return date


    # 是否是周末
    def is_weekend(self, date, hour):
        week = date.isoweekday()

        if week < 4:
            if hour < 15:
                return date + timedelta(days=1)
            else:
                return date + timedelta(days=2)
        elif week == 4:
            if hour < 15:
                return date + timedelta(days=1)
            else:
                return date + timedelta(days=4)
        elif week == 5:
            if hour < 15:
                return date + timedelta(days=3)
            else:
                return date + timedelta(days=4)
        elif week == 7 and hour > 15:
            return self.is_weekend(date + timedelta(days=1), hour=10)
        else:
            return self.is_weekend(date + timedelta(days=1), hour)


    def holiday(self):
        return {
            12: [30, 31],
            1: [1, ],
            2: [2, 3, 4, 5, 6, 7, 8, 9, 10],
            4: [5, 6, 7],
            5: [1, 2, 3, 4],
            6: [7, 8, 9],
            9: [13, 14, 15],
            10: [1, 2, 3, 4, 5, 6, 7]
        }

fundsr = FundSR()
fundsr = fundsr.free_charge_days