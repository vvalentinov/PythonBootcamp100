# data = []
#
# with open("weather_data.csv") as file:
#     lines = file.readlines()
#     for line in lines:
#         no_spaces_line = line.strip()
#         data.append(no_spaces_line)
#
# print(data)
# ------------------------------------------------------------------------
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in list(data)[1:]:
#         temperatures.append(int(row[1]))
# print(temperatures)
# -------------------------------------------------------------------------
# import pandas
#
# data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["temp"])

# data_dictionary = data.to_dict()
# print(data_dictionary)

# temp_list = data["temp"].to_list()
# print(temp_list)
# avg = round(sum(temp_list) / len(temp_list), 2)
# print(f"Average Temperature: {avg}")
# print(f"Average Temperature: {data["temp"].mean()}") # --> average temp value
# print(f"Maximum temp: {data["temp"].max()}")

# row = data[data.day == "Monday"]
# row = data[data.temp == data.temp.max()]
# print(row)

# monday = data[data.day == "Monday"]
# temp = monday.temp[0] * 1.8 + 32
# print(f"Temp in Fahrenheit: {temp}")

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data_frame = pandas.DataFrame(data_dict)
# data_frame.to_csv("new_data.csv")
# print(data_frame)
# ---------------------------------------------------------------------------
import pandas

data = pandas.read_csv("squirrel_data.csv")

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [0, 0, 0]
}

value_counts = data["Primary Fur Color"].value_counts()
print(value_counts)

gray_count = int(value_counts.iloc[0])
black_count = int(value_counts.iloc[1])
cinnamon_count = int(value_counts.iloc[2])
data_dict["Count"] = [gray_count, black_count, cinnamon_count]

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")