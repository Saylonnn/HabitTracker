import flet as ft
import pickle
from Habit import Habit
import datetime as dt

STORAGE_FILENAME = 'habits.pkl'
HABITS: list[Habit] = []


def load_from_storage() -> list[Habit]:
    habits = []
    with open(STORAGE_FILENAME, 'rb') as file:
        saves: list[Habit] = pickle.load(file)
    habits.append(saves)
    return habits


def main(page: ft.Page):
    # HABITS = load_from_storage()
    HABITS.append(Habit(
        name="Drink Water",
        start_date=dt.datetime(2024, 1, 4),
        description="""
        Drink only Drinks with 0 calories. 
        1 Glass with > 0 calories per day.
        1 Cheat Day/Week""",
        icon=ft.icons.WATER_DROP
    ))

    page.title = "Habit Tracker"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def addNavBar():
        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.HOME_ROUNDED, label="Home"),
                ft.NavigationDestination(icon=ft.icons.SETTINGS_ROUNDED, label="Settings"),
            ]
        )
    addNavBar()
    page.update()
    for habit in HABITS:
        card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(habit.icon),
                            title=ft.Text(habit.name),
                            subtitle=ft.Text(habit.description)
                        ),
                        ft.Column(
                            [
                                ft.Text(f"Progress: {habit.get_progress()}%"),
                                ft.ProgressBar(color="2879ff", value=habit.get_progress())
                            ]
                        ),
                        ft.Row(
                            [ft.TextButton("Check"), ft.TextButton("Fail")],
                            alignment=ft.MainAxisAlignment.END
                        ),
                    ]
                ),
                # width=400,
                padding=10
            )
        )
        page.add(card)
        page.update()

ft.app(target=main)

