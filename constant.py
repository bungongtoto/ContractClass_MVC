DaysoftheWeek = ("Monday", "Tuesday" , "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def chooce_working_days()->tuple:
        count = 0
        for day in DaysoftheWeek:
            print(f"{count}.) {day} ")
            count += 1
        return DaysoftheWeek[int(input("Enter start day: ")): int(input("Enter end day number: "))+1]   
    