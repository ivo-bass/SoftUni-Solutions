tables_count = int(input())
table_length_meters = float(input())
table_width_meters = float(input())


table_cloth = tables_count * (table_length_meters + 0.6) * (table_width_meters + 0.6)
table_top = tables_count * (table_length_meters / 2) * (table_length_meters / 2)

price_usd = table_cloth * 7 + table_top * 9
price_lv = price_usd * 1.85

print(f"{price_usd:.2f} USD")
print(f"{price_lv:.2f} BGN")
