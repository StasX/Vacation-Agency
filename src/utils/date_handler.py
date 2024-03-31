from datetime import datetime, time


class DateHandler:

    @staticmethod
    # Format to date:
    def format_date(unformatted_date):
        formatted_date = unformatted_date.strftime("%d/%m/%Y")
        return formatted_date

    @staticmethod
    def format_vacation_dates(vacation):
        vacation["start_date"] = DateHandler.format_date(
            vacation["start_date"])
        vacation["end_date"] = DateHandler.format_date(vacation["end_date"])
        return vacation
    # Get current date:
    @staticmethod
    def now():
        time_now = datetime.now()
        return time_now
    # Convert string to date
    @staticmethod
    def to_date(string):
        date = datetime.strptime(string, '%Y-%m-%d').date()
        return datetime.combine(date, time(0, 0))
