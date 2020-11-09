hall_rent = int(input())

statuettes = 0.7 * hall_rent
catering = 0.85 * statuettes
sound = 0.5 * catering
total = hall_rent + statuettes + catering + sound
print(f'{total:.2f}')
