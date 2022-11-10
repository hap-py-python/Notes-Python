import calendar as cl

cal = cl.month(2022,11)
cal2 = cl.weekday(2022, 11, 1) # The first of November was on Tuesday
# In Calendar days of the week starts with 0, so Mon - 0, Tue - 1, Wed - 2, Thr - 3, Fr - 4, Sat -5, Sun - 6.

print(cal)
print(cal2)