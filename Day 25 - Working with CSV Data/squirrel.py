import pandas

data = pandas.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

number_of_gray = len(data[data["Primary Fur Color"] == "Gray"])
number_of_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
number_of_black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [number_of_gray, number_of_red, number_of_black],
}

squirrels = pandas.DataFrame(data_dict)
squirrels.to_csv("Day 25/modified_squirrel_data.csv")

# print(number_of_gray)
