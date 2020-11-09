city_name = input()        # ("Bansko", "Borovets", "Varna", "Burgas")
deal_type = input()        # ("noEquipment", "withEquipment", "noBreakfast", "withBreakfast")
vip_discount = input()     # ("yes", "no")
days = int(input())

city_names = ("Bansko", "Borovets", "Varna", "Burgas")

deal1_cities = ("Bansko", "Borovets")
deal2_cities = ("Varna", "Burgas")

deal1_options = ("noEquipment", "withEquipment")
deal2_options = ("noBreakfast", "withBreakfast")

deal1_prices = {"noEquipment": 80.00, "withEquipment": 100.00}
deal2_prices = {"noBreakfast": 100.00, "withBreakfast": 130.00}

deal1_discounts = {"noEquipment": 0.05, "withEquipment": 0.1}
deal2_discounts = {"noBreakfast": 0.07, "withBreakfast": 0.12}

price = 0
error_msg = "Invalid input!"

if days > 7:
    days -= 1

if days > 1:
    if city_name in city_names:
        if city_name in deal1_cities:
            if deal_type in deal1_options:
                price = deal1_prices[deal_type]
                if vip_discount == "yes":
                    price -= price * deal1_discounts[deal_type]
                total_price = days * price
                print(f"The price is {total_price:.2f}lv! Have a nice time!")
            else:
                print(error_msg)

        elif city_name in deal2_cities:
            if deal_type in deal2_options:
                price = deal2_prices[deal_type]
                if vip_discount == "yes":
                    price -= price * deal2_discounts[deal_type]
                total_price = days * price
                print(f"The price is {total_price:.2f}lv! Have a nice time!")
            else:
                print(error_msg)
    else:
        print(error_msg)
else:
    print("Days must be positive number!")

# nqma takava agenciq! :D
