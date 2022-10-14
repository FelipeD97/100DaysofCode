# with open("Day 25/weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("Day 25/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("Day 25/weather_data.csv")
# print(type(data))

## Get data in a column
# print(data["condition"])

## Convert data to dictionary
data_dict = data.to_dict()
# print(data_dict)

## put data into a list
temp_list = data["temp"].to_list()
average_temp = sum(temp_list) / len(temp_list)

max_temp = data.temp.max()
# print(max_temp)

# print(data.temp)

## Get data in a row
# print(data[data.temp == max_temp])
monday = data[data.day == "Monday"]
# print(monday.condition)

f_temp = (monday.temp * (9 / 5)) + 32
print(f_temp)

## Create Data Frame from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

data = pandas.DataFrame(data_dict)
data.to_csv("Day 25/new_data.csv")
print(data)
