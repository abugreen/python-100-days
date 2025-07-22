from art import logo

print(logo)

run_flag = True
bidding_record = {}

def find_highest_bidder(bidding_record):
    heighest_bid = 0
    heighest_name =""
    for bidder in bidding_record:
        if bidding_record[bidder] > heighest_bid:
           heighest_bid = bidding_record[bidder]
           heighest_name = bidder
    print(f"The winner is {heighest_name} wiht a bid of {heighest_bid}") 
        

while run_flag:
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    bidding_record[name] = int(bid)
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower() 
    if should_continue == 'no':
        find_highest_bidder(bidding_record)
        run_flag = False
        print("Bidding has ended.")
        
    elif should_continue != 'yes':
        print("Please enter 'yes' or 'no'.")
        
       