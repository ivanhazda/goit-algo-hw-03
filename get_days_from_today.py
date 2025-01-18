from datetime import datetime,date

def get_days_from_today(date_string):
    try:
        target_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = date.today()

        return (target_date - today).days
    except ValueError:
        return "Неправильний формат дати"
print(get_days_from_today("2021-10-09"))  