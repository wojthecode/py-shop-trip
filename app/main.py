from __future__ import annotations
from json import load
from customer import Customer
from shop import Shop


def shop_trip() -> None:

    with open("app/config.json") as config_file:
        config = load(config_file)

    fuel_price = config["FUEL_PRICE"]
    shop_list = Shop.create_shops_list(config["shops"])
    customers = Customer.create_customer_list(config["customers"])

    for customer in customers:
        shops_trip_cost = customer.calculate_trip_cost(shop_list, fuel_price)
        print(f"{customer.name} has {customer.money} dollars")
        for cost, shop in shops_trip_cost.items():
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
        if customer.money < min(shops_trip_cost.keys()):
            print(f"{customer.name} \
doesn't have enough money to make a purchase in any shop")
            continue
        trip_cost = min(shops_trip_cost.keys())
        cheapest_shop = shops_trip_cost[trip_cost]
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        cheapest_shop.print_receipt(customer.shoping_list, customer.name)
        money_left = round(customer.money - trip_cost, 2)
        print(f"\n{customer.name} rides home")
        print(f"{customer.name} now has {money_left} dollars\n")


shop_trip()
