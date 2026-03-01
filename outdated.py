months=["January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"

]

while True:
    try:
        user = input("Date: ")
        if "/" in user:
            month, day, year = user.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if month not in range(1, 13):
                continue
            if day not in range(1, 32):
                continue
        elif "," in user:
            month, day, year = user.replace(",", "").split(" ")
            month = int(months.index(month) + 1)
            day = int(day)
            year = int(year)
            if day not in range(1, 32):
                continue
        else:
            continue
        print(f"{year:04}-{month:02}-{day:02}")
        break
    except ValueError:
        continue 