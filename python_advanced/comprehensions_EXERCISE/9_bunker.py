def get_input():
    return {name: {} for name in input().split(', ')}


def fill_stash(dd):
    n = int(input())
    for _ in range(n):
        category, item_name, values = input().split(" - ")
        quantity_token, quality_token = values.split(';')
        quantity = int(quantity_token.split(':')[1])
        quality = int(quality_token.split(':')[1])
        if not item_name in dd[category]:
            dd[category][item_name] = {
                'quantity': quantity, 'quality': quality}
        else:
            dd[category][item_name]['quantity'] += quantity
            dd[category][item_name]['quality'] += quality
    return dd


def calc_count_and_quality(dd):
    total_count = 0
    total_quality = 0
    for items in bunker.values():
        for value in items.values():
            total_count += value['quantity']
            total_quality += value['quality']
    return total_count, total_quality / len(bunker)


def print_output(count, avg, bunk):
    print(f'Count of items: {count}')
    print(f'Average quality: {avg:.2f}')

    for category, dd in bunk.items():
        items = [name for name in dd.keys()]
        print(f'{category} -> {", ".join(items)}')


stash = get_input()
bunker = fill_stash(stash)
count, avg = calc_count_and_quality(bunker)
print_output(count, avg, bunker)
