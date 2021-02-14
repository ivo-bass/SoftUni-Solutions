def stock_availability(flavours_list, action, *args):
    if action == 'delivery':
        flavours_list.extend(args)
    else:
        if not args:
            flavours_list.pop(0)
        elif type(args[0]) == int:
            for _ in range(args[0]):
                flavours_list.pop(0)
        else:
            for flavour in args:
                if flavour in flavours_list:
                    flavours_list = list(filter(lambda x: x != flavour, flavours_list))
    return flavours_list

# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
