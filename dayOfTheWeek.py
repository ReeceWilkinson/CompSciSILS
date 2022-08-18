import datetime 

week_days = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]

def inputs():
    Day = int(input("What day of the month is it?: "))
    Month = int(input("What number month is it. E.G. Febuary = 2 and june = 6: "))
    Year = int(input("What year is it?: "))
    week_num = datetime.date(Year,Month,Day).weekday()
    print(week_days[week_num])

inputs()