day_made_res = int(input())
month_made_res = int(input())
day_check_in = int(input())
month_check_in = int(input())
day_check_out = int(input())
month_check_out = int(input())

stay = day_check_out - day_check_in

if day_check_in - day_made_res >= 10 or month_check_in != month_made_res:
    price = 25.00
else:
    price = 30.00

if month_check_in != month_made_res:
    cost = format((price * stay) - (20/100*(price * stay)), '0.2f')
else:
    cost = format(price * stay, '0.2f')

print("Your stay from " + str(day_check_in) + "/" + str(month_check_in) + " to " +
      str(day_check_out) + "/" + str(month_check_out) + " will cost " + str(cost))

