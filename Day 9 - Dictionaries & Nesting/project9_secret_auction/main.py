from logo import gavel
from os import system, name


def clear():

    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def take_bid(name, bid):
    bids.append({"name": name, "bid": bid})


def highest_bid(bids):
    highest_bidder = {"name": "", "bid": 0}

    for item in bids:
        if highest_bidder["bid"] < item["bid"]:
            highest_bidder = item

    print(
        f'The highest bidder is {highest_bidder["name"]} with a ${highest_bidder["bid"]} bid.'
    )


bids = []
bid_active = True

print(gavel)
print("Welcome to the Secret Auction")

while bid_active:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))

    take_bid(name, bid)

    more_bidders = input("Are more people bidding?: ")
    more_bidders.lower()

    if more_bidders == "no":
        highest_bid(bids)
        bid_active = False
    else:
        clear()
