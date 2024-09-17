from dateutil import parser
from datetime import datetime,date
import logging
from pytz import timezone 

def get_ist_time():
    return datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')


def convert_to_date(datetime_input):
    '''
    input: takes any format of date string
    output: returns date
    '''
    if isinstance(datetime_input, str):
        try:
            dt_object = parser.parse(datetime_input)
            date_only = dt_object.date()
            return date_only
        except ValueError:
            logging.error(f"Error: '{datetime_input}' is not a recognizable date format.")
        return None
    elif isinstance(datetime_input, date):
        # If input is already a date object, return it directly
        return datetime_input
    elif isinstance(datetime_input, datetime):
        # If input is a datetime object, extract date component
        return datetime_input.date()
    elif isinstance(datetime_input, (int, float)):
        # If input is a timestamp, convert it to a datetime object first
        try:
            dt_object = datetime.fromtimestamp(datetime_input)
            return dt_object.date()
        except ValueError:
            logging.error(f"Error: '{datetime_input}' Error: Input timestamp is invalid.")
            return None
    else:
        return None

def get_date_diff(date1, date2):
    '''
    date1: the fist date
    date2: the latest date
    date2-date1 will give positive numbers
    '''
    if date1 and date2:
        try:
            return (date2-date1).days
        except:
            return -1
    else:
        return -1

def convert_string_to_number(input_string):
    # Directly return if the input is already a number
    if isinstance(input_string, (int, float)):
        return input_string

    # Attempt to clean and convert the string to a number
    elif isinstance(input_string, str):
        cleaned_string = input_string.replace(',', '').strip()

        # Try converting to int first
        try:
            return int(cleaned_string)
        except ValueError:
            logging.error(f"Error: '{cleaned_string}': Input number is invalid.")
            pass  # Skip to trying float conversion

        # Next, try converting to float
        try:
            return float(cleaned_string)
        except ValueError:
            logging.error(f"Error: '{cleaned_string}' is not a valid number.")
    else:
        logging.error(f"Unsupported input type: {type(input_string).__name__}")
        return None
    return None


    def x_months_ago(date, months):
        """
        Function to get the datetime object for the first day, X months before the given date
        Simple approach to subtract months (might need adjustment for edge cases)
        """
        month = date.month - months - 1
        year = date.year + month // 12
        month = month % 12 + 1
        day = min(date.day, [31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
        return datetime(year, month, day)

def month_to_num(month_name):
    """
    Function to convert month name to number
    :param: takes months number and return
    """
    datetime_object = datetime.strptime(month_name, "%b")
    return datetime_object.month