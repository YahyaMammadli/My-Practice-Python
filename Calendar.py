import calendar
import matplotlib.pyplot as plt

# unfinished fan project

def myCalendar (year, month):
    cal = calendar.monthcalendar(year, month)
    fig, ax = plt.subplots()
    ax.axis("off")
    weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    ax.table(cellText=cal, colLabels=weekdays, loc= "center")

    plt.savefig(f"calendar_{year}_{month}.png")
    print(f"Calendar saved")

if __name__ == "__main__":
    y = int(input("Year => "))
    m = int(input("Month => "))
    myCalendar(y,m)




import calendar
import matplotlib.pyplot as plt


def myCalendar(year, month):
    cal = calendar.monthcalendar(year, month)
    cal = [[day if day != 0 else "" for day in week] for week in cal]
    ax = plt.subplots()
    ax.axis("off")
    weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    table = ax.table(cellText=cal, colLabels=weekdays, loc="center", cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 2)  

    plt.savefig(f"calendar_{year}_{month}.png")
    print(f"Calendar saved as calendar_{year}_{month}.png")


if __name__ == "__main__":
    y = int(input("Year => "))
    m = int(input("Month => "))
    myCalendar(y, m)




