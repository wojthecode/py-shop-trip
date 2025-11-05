from __future__ import annotations
from json import load
from app.customer import Customer
from app.shop import Shop


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

        min_trip_cost = min(shops_trip_cost.keys())
        if customer.money < min_trip_cost:
            print(f"{customer.name} \
doesn't have enough money to make a purchase in any shop")
            continue
        cheapest_shop = shops_trip_cost[min_trip_cost]
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        cheapest_shop.print_receipt(customer.product_cart, customer.name)
        money_left = round(customer.money - min_trip_cost, 2)
        print(f"\n{customer.name} rides home")
        print(f"{customer.name} now has {money_left} dollars\n")


shop_trip()
