import datetime
def isLeapYear(year):
    return (year % 400 == 0) or (year%4==0 and year %100 != 0)

def songay(d, m , y):
    s = sum(365 + isLeapYear(i) for i in range(1, y))
    t = [0, 31, 28 + isLeapYear(y), 31, 30, 31, 30,31,31,30,31,30,31 ]
    return s+ sum(t[:m])+d
    
# if __name__ == '__main__':
#     d1, m1, y1 = map(int, input().split())
#     d2, m2, y2 = map(int, input().split())
#     print(songay(d2, m2, y2) - songay(d1, m1, y1))
    

# if __name__ == '__main__':
#     d, m , y = map(int, input().split())
#     s = songay(d, m, y)%7
#     thu = ["Chu nhat", "Thu 2", "Thu 3", "Thu 4", "Thu 5", "Thu 6", "Thu 7"]
#     print(thu[s])

d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())
s = datetime.date(y2, m2, d2) - datetime.date(y1, m1, d1)
print(s.days)