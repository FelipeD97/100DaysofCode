bids = [{"name": "Felipe", "bid": 100}, {"name": "Carlos", "bid": 200}]


def take_bid(name, bid):
    bids.append({"name": name, "bid": bid})
    print(bids)


def grab_bid(bids):
    highest = 0

    for item in bids:
        if highest > item["bid"]:
            highest = item["bid"]
            print(highest)


grab_bid(bids)


def highest_bid(bids):
    highest = 0

    for item in bids:
        for key in item:
            if bids["bid"] > bids.index(item["bid"] + 1):
                highest = item["bid"]
            print(f'The highest bidder is {item["name"]} with a ${item["bid"]} bid.')


bid_active = True

# while bid_active:
#     name = input("What is your name?: ")
#     bid = int(input("What is your bid?: "))

#     highest_bidder = ""

#     take_bid(name, bid)

#     more_bidders = input("Are more people bidding?: ")
#     more_bidders.lower()

#     if more_bidders == "no":
#         print(bids[2])
#         bid_active = False
