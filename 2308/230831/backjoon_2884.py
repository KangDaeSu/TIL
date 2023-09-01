hours, minute = map(int, input().split())
if minute >= 45:
    m = minute - 45
    print(hours, m)
else:
    m = (minute+60) - 45
    if hours == 0:
        h = (hours + 24) - 1
        print(h, m)
    else:
        h = hours - 1
        print(h, m)
