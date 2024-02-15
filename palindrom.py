def plindrom(s):
    return s == s[::-1]


s = input("enter the name")
ans = plindrom(s)
print(ans)

