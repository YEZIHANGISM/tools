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
		week = date.isoweekday()

		if week > 5:
			hour = 16
		date = self.is_playday(date+timedelta(days=1), hour, holiday)

		return date

	def is_playday(self, date, hour, holiday):
		week = date.isoweekday()

		if date.month in holiday.keys() and date.day not in holiday[date.month] and week <= 5:
			if hour > 15:
				return self.is_playday(date+timedelta(days=1), 10, holiday)
			else:
				return date
		return self.is_playday(date+timedelta(days=1), hour, holiday)

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
free_charge_days = fundsr.free_charge_days