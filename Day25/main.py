import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
# #converting the dataframe into dict
# print(data.to_dict())
# #conerting the data frame into list
#
# temp_list = data["temp"].to_list()
#
# print(data["temp"].max())
#
# #get data in columns
# print(data["condition"])
# print(data.condition)

#et data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
#
# monday_temp = (monday.temp*(9/5)+32)
# print(monday_temp)

# data_dict = {
#     "names":["A","b", "c","d"],
#     "points":[23,43,55,66]
# }
#
# data = pandas .DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("Squirrel_Data.csv")
Gray_squirrel = len(data[data["Primary Fur Color"]=="Gray"])
Black_squirrel = len(data[data["Primary Fur Color"]=="Black"])
Cinnamon_squirrel = len(data[data["Primary Fur Color"]=="Cinnamon"])

print(Gray_squirrel, Black_squirrel, Cinnamon_squirrel)

data_dict = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [Gray_squirrel, Black_squirrel,  Cinnamon_squirrel]
}

Squirrel_data=pandas.DataFrame(data_dict)
Squirrel_data.to_csv("Squirrel_count.csv")