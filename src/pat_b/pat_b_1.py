s = input()

const = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']

sum = 0
for c in s:
    sum += int(c)

result = ''
for c in str(sum):
    result += const[int(c)] + ' '

print(result[:-1])