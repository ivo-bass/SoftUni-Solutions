name = input()
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_percentage = int(input())

income = days_count * tickets_count * ticket_price
income -= cinema_percentage/100 * income

print(f"The profit from the movie {name} is {income:.2f} lv.")
