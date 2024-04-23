from datetime import datetime, timedelta


def days_from_today(days, direction):
    if direction.lower() == "past":
        delta = timedelta(days=-days)
    elif direction.lower() == "future":
        delta = timedelta(days=days)
    else:
        print("Invalid direction. Enter 'past' or 'future'.")
        return

    result_date = datetime.now() + delta
    return result_date.strftime("%Y-%m-%d")


def main():
    days = int(input("Enter number of days: "))
    direction = input("Enter 'past' or 'future': ")

    result_date = days_from_today(days, direction)
    if result_date:
        print(f"The date {days} days {direction} from today is: {result_date}")


if __name__ == "__main__":
    main()
