# Enter your code here. Read input from STDIN. Print output to STDOUT
day1, month1, year1 = map(int, input().split())
day2, month2, year2 = map(int, input().split())

if year1 > year2:
    print(10000)
elif year1 == year2 and month1 > month2:
    print(500 * (month1 - month2))
elif year1 == year2 and month1 == month2 and day1 > day2:
    print(15 * (day1 - day2))
else:
    print(0)
