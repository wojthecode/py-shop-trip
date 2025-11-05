from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: Products

    @classmethod
    def create_shops_list(cls, shops: list[dict]) -> list[Shop]:
        shops_list = []
        for shop in shops:
            shops_list.append(
                Shop(
                    shop["name"],
                    shop["location"],
                    Products.create_products_list(shop["products"])
                )
            )
        return shops_list

    def calculate_cart_cost(self, customers_cart: Products) -> dict:
        return {
            "milk": round(self.products.milk * customers_cart.milk, 1),
            "bread": round(self.products.bread * customers_cart.bread, 1),
            "butter": round(self.products.butter * customers_cart.butter, 1)
        }

    def print_receipt(self, cart: Products, customer_name: str) -> None:

        curent_date = datetime(2021, 1, 4, 12, 33, 41)
        recipt_date = datetime.strftime(curent_date, "%d/%m/%Y %H:%M:%S")

        cost = self.calculate_cart_cost(cart)
        print(f"Date: {recipt_date}")
        print(f"Thanks, {customer_name}, for your purchase!\nYou have bought:")
        print(f"{cart.milk:g} milks for {cost['milk']:g} dollars")
        print(f"{cart.bread:g} breads for {cost['bread']:g} dollars")
        print(f"{cart.butter:g} butters for {cost['butter']:g} dollars")
        print(f"Total cost is {sum(cost.values())} dollars")
        print("See you again!")


@dataclass
class Products:
    milk: float
    bread: float
    butter: float

    @classmethod
    def create_products_list(cls, products: dict) -> Products:
        return Products(
            products["milk"],
            products["bread"],
            products["butter"]
        )
