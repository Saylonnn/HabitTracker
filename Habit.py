from dataclasses import dataclass
import datetime as dt
import flet as ft

@dataclass
class Habit:
    name: str
    start_date: dt.datetime.date
    description: str
    icon: ft.icons

    def get_progress(self) -> int:
        """
        calculates the Progress in % (Target are 90 Days)

        :return:
        """
        today = dt.datetime.today()
        difference = today - self.start_date
        total_days = difference.days
        value = int(total_days * 100 / 90)
        return value
