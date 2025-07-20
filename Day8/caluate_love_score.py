def calculate_love_score(name1, name2):
    name_str = (name1 + name2).upper()
    #print(name_str)
    count1 = 0
    count0 = 0
    for i in name_str:
        if i == "T" or i == "R" or i == "U" or i == "E":
            count1 += 1
            #print(f"count1 : {count1}")

        if i == "L" or i == "O" or i == "V" or i == "E":
            count0 += 1
            #print(f"count0 : {count0}")
    love_score = str(count1) + str(count0)
    print(love_score)
            
    

calculate_love_score("Kanye West", "Kim Kardashian")
            