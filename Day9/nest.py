capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}


# travel_log = {
#     "France" : ["Paris" , "Lille", "Dijon"] ,
#     "Germany" : ["Stuttgart", "Berlin"]
# }


# print(travel_log["France"][1])


travel_log = {
    "France" : {
        "num_times_visited" : 8 ,
        "cities_visited" : ["Paris","Lille","Dijon"]
        } ,
    "Germany" : {
        "cities_visited" : ["Berlin", "Hamburg","Stuttgart"],
        "total_visits" : 5
    }
}

#print out "Stuttgart"
print(travel_log["Germany"]["cities_visited"][2])