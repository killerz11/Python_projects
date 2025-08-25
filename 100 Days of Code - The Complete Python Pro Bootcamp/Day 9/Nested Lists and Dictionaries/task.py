capitals = {
    "France": "paris",
    "Germany": "Berlin"
}

# travel_log = {
#     "France": ["paris", "lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][0])

travel_log = {
    "France": {
        "num_time_visited": 8,
        "cities_visited": ["paris", "lille", "Dijon"]
    },
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"]["cities_visited"][2])