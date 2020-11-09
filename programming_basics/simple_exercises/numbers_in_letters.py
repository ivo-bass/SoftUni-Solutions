num = int(input())
num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}

def number(a):
    if 1 <= a < 10:
        print(num2words1[a])
    else:
        print('The number is too high')

number(num)
