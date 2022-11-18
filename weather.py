import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

# result = format_temperature("5")
# print(result)


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # print(iso_string)
    today_date = datetime.fromisoformat(iso_string)  # current date and time
    # print(type(today_date))
    # print(today_date)
    date_str = today_date.isoformat()
    weekday_list = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
    # print(weekday_list[date.weekday(today_date)])

    day = today_date.strftime("%d")
    # print(day)

    month = int(today_date.strftime("%m"))
    month_list = ['0', 'January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    # print(month_list[month])

    year = today_date.strftime("%Y")
    # print(year)

    # print(
    #     f"{weekday_list[date.weekday(today_date)]} {day} {month_list[month]} {year}")

    return f"{weekday_list[datetime.weekday(today_date)]} {day} {month_list[month]} {year}"


# TEST
# result = convert_date("2021-07-05T07:00:00+08:00")
# print(result)


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_farenheit = float(temp_in_farenheit)
    temp_in_celcius = float((temp_in_farenheit-32)*5/9)
    result = round(temp_in_celcius, 1)
    return (result)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    for i in range(0, len(weather_data)):
        weather_data[i] = float(weather_data[i])
    average = sum(weather_data)/len(weather_data)
    return (average)

# TEST
# weather_data = ["51", "58", "59", "52", "52", "48", "47", "53"]
# for i in range(0, len(weather_data)):
#     weather_data[i] = float(weather_data[i])
# average = sum(weather_data)/len(weather_data)
# print(average)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        header = next(csv_file)
        for line in reader:
            line[1] = int(line[1])
            line[2] = int(line[2])
            return (list[line])


# with open("tests/data/example_one.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     header = next(csv_file)
#     for line in reader:
#         line[1] = int(line[1])
#         line[2] = int(line[2])
#         print(line)


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if len(weather_data) == 0:
        return ("()")
    else:
        for i in range(len(weather_data)):
            weather_data[i] = float(weather_data[i])
        low_temp = (min(weather_data))
        index = weather_data.index(low_temp)
        if weather_data.count(low_temp) == 2:
            result = (round(low_temp, 1), len(weather_data) - index - 1)
        else:
            result = (round(low_temp, 1), weather_data.index(low_temp))
        return (result)


# TEST
# weather_data = []
# if len(weather_data) == 0:
#     print("()")
# else:
#     for i in range(len(weather_data)):
#         weather_data[i] = float(weather_data[i])
#     low_temp = (min(weather_data))
#     index = weather_data.index(low_temp)
#     if weather_data.count(low_temp) == 2:
#         result = (round(low_temp, 1), len(weather_data) - index - 1)
#     else:
#         result = (round(low_temp, 1), weather_data.index(low_temp))
#     print(result)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data) == 0:
        return ("()")
    else:
        for i in range(len(weather_data)):
            weather_data[i] = float(weather_data[i])
        high_temp = (max(weather_data))
        index = weather_data.index(high_temp)
        if weather_data.count(high_temp) == 2:
            result = (round(high_temp, 1), len(weather_data) - index - 2)
        else:
            result = (round(high_temp, 1), weather_data.index(high_temp))
        return (result)

# test
# weather_data = [49, 57, 56, 55, 57, 53, 49]
# if len(weather_data) == 0:
#     print("()")
# else:
#     for i in range(len(weather_data)):
#         weather_data[i] = float(weather_data[i])
#     high_temp = (max(weather_data))
#     index = weather_data.index(high_temp)
#     if weather_data.count(high_temp) == 2:
#         result = (round(high_temp, 1), len(weather_data) - index - 2)
#     else:
#         result = (round(high_temp, 1), weather_data.index(high_temp))
#     print(result)


def generate_summary(weather_data):  # to do at the end
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):  # the second last one to do
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    date = weather_data[0]
    for line in weather_data:
        return (f"---- {convert_date(date)} ----")
        return (f"Minimum Temperature: {format_temperature(find_min)}")
        return (f"Maximum Temperature: {format_temperature(find_max)}")


# ---- Friday 02 July 2021 - ---
# Minimum Temperature: 9.4°C
# Maximum Temperature: 19.4°C

# ---- Saturday 03 July 2021 - ---
# Minimum Temperature: 13.9°C
# Maximum Temperature: 20.0°C
