sec = int(input())
hour = sec // 3600
sec = sec % 3600
min = sec // 60
sec = sec % 60
print("Hours:", hour, "Minutes:", min, "Seconds:", sec)
