n = int(input())
output = ''

if n == 88:
    output = "Leo finally won the Oscar! Leo is happy"
elif n == 86:
    output = "Not even for Wolf of Wall Street?!"
elif n < 88 and n != 86:
    output = "When will you give Leo an Oscar?"
else:
    output = "Leo got one already!"

print(output)
