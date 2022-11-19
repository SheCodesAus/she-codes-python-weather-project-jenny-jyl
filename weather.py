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
    date = datetime(int(iso_string[0:4]),
                    int(iso_string[5:7]),
                    int(iso_string[8:10]))
    return date.strftime(f"%A %d %B %Y")


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
    with open(csv_file) as csv_file_data:
        reader = csv.reader(csv_file_data)
        header = next(reader)
        return_list = []
        for line in reader:
            if line == []:
                continue
            else:
                new_line = []
                new_line.append(line[0])
                new_line.append(int(line[1]))
                new_line.append(int(line[2]))
                return_list.append(new_line)
    return return_list

# result = load_data_from_csv("tests/data/example_two.csv")
# print(result)


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if len(weather_data) == 0:
        return ()
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
        return ()
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


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    result = ""
    no_days = len(weather_data)
    result += str(no_days) + " Day Overview"
    result += "\n"
    low = []
    high = []
    for data in weather_data:
        low.append(data[1])
        high.append(data[2])
    min_temp = format_temperature(convert_f_to_c(min(low)))
    max_temp = format_temperature(convert_f_to_c(max(high)))
    dates = []
    for data in weather_data:
        dates.append(data[0])
    low_date = convert_date(dates[low.index(min(low))])
    high_date = convert_date(dates[high.index(max(high))])
    avg_low = sum(low)/len(low)
    avg_low = format_temperature(convert_f_to_c(avg_low))
    avg_high = sum(high)/len(high)
    avg_high = format_temperature(convert_f_to_c(avg_high))
    result += "  The lowest temperature will be " + \
        min_temp + ", and will occur on " + low_date + "."
    result += "\n"
    result += "  The highest temperature will be " + \
        max_temp + ", and will occur on " + high_date + "."
    result += "\n"
    result += "  The average low this week is " + avg_low + "."
    result += "\n"
    result += "  The average high this week is " + avg_high + "."
    result += "\n"
    return (result)

# generate_summary([
#     ["2021-07-02T07:00:00+08:00", 49, 67],
#     ["2021-07-03T07:00:00+08:00", 57, 68],
#     ["2021-07-04T07:00:00+08:00", 56, 62],
#     ["2021-07-05T07:00:00+08:00", 55, 61],
#     ["2021-07-06T07:00:00+08:00", 53, 62]
# ])

# 5 Day Overview
# The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
# The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
# The average low this week is 12.2°C.
# The average high this week is 17.8°C.

# generate_summary([
#     ["2020-06-19T07:00:00+08:00", 47, 46],
#     ["2020-06-20T07:00:00+08:00", 51, 67],
#     ["2020-06-21T07:00:00+08:00", 58, 72],
#     ["2020-06-22T07:00:00+08:00", 59, 71],
#     ["2020-06-23T07:00:00+08:00", 52, 71],
#     ["2020-06-24T07:00:00+08:00", 52, 67],
#     ["2020-06-25T07:00:00+08:00", 48, 66],
#     ["2020-06-26T07:00:00+08:00", 53, 66]
# ])

# 8 Day Overview
# The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.
# The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
# The average low this week is 11.4°C.
# The average high this week is 18.8°C.


generate_summary([
    ["2020-06-19T07:00:00+08:00", -47, -46],
    ["2020-06-20T07:00:00+08:00", -51, 67],
    ["2020-06-21T07:00:00+08:00", 58, 72],
    ["2020-06-22T07:00:00+08:00", 59, 71],
    ["2020-06-23T07:00:00+08:00", -52, 71],
    ["2020-06-24T07:00:00+08:00", 52, 67],
    ["2020-06-25T07:00:00+08:00", -48, 66],
    ["2020-06-26T07:00:00+08:00", 53, 66]
])

# 8 Day Overview
#   The lowest temperature will be -46.7°C, and will occur on Tuesday 23 June 2020.
#   The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#   The average low this week is -16.1°C.
#   The average high this week is 12.4°C.


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    result = ""
    for line in weather_data:
        # print(line)
        day = line[0]
        day = convert_date(day)
        day = "---- "+day+" ----"
        result += day
        result += "\n"
        min = line[1]
        min = format_temperature(convert_f_to_c((min)))
        result += "  Minimum Temperature:" + " "+min
        result += "\n"
        max = line[2]
        max = format_temperature(convert_f_to_c((max)))
        result += "  Maximum Temperature:" + " " + max
        result += "\n"
        result += "\n"
    return result
