junior_count = int(input())
senior_count = int(input())
track_type = input()

taxes = {"trail": {"juniors": 5.5, "seniors": 7},
         "cross-country": {"juniors": 8, "seniors": 9.5},
         "downhill": {"juniors": 12.25, "seniors": 13.75},
         "road": {"juniors": 20, "seniors": 21.5}}

junior_money = taxes[track_type]["juniors"] * junior_count
senior_money = taxes[track_type]["seniors"] * senior_count

total_money = junior_money + senior_money * 0.95
if track_type == "cross-country" and junior_count + senior_count >= 50:
    total_money *= 0.75

total_money *= 0.95

print(f"{total_money:.2f}")
