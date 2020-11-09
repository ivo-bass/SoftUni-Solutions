flour_price = float(input())
flour_q = float(input())
sugar_price = 0.75 * flour_price
sugar_q = float(input())
egg_price = 1.1 * flour_price
egg_packs = int(input())
yeast_price = 0.2 * sugar_price
yeast_packs = int(input())

total = flour_price * flour_q + \
        sugar_price * sugar_q + \
        egg_price * egg_packs + \
        yeast_price * yeast_packs

print(f'{total:.2f}')
