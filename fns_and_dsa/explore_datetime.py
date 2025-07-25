import datetime
def display_current_datetime():
    """Display the current date and time."""
    now = datetime.datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    """Calculate the date after a given number of days."""
    now = datetime.datetime.now()
    future_date = now + datetime.timedelta(days=days)
    print(f"Date after {days} days:", future_date.strftime("%Y-%m-%d"))
def main():
    display_current_datetime()
    days = int(input("Enter the number of days to calculate the future date: "))
    calculate_future_date(days)
if __name__ == "__main__":
    main()