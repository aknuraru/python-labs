import datetime

start_str = input("Enter the start date and time (YYYY-MM-DD HH:MM:SS): ")
start_date = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")

end_str = input("Enter the end date and time (YYYY-MM-DD HH:MM:SS): ")
end_date = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")

time_diff = (end_date - start_date).total_seconds()

print("The difference between", start_date, "and", end_date, "is", time_diff, "seconds.")