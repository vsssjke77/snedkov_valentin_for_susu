def entry():
    departure_hours = int(input('1'))
    departure_minutes = int(input('2'))
    hours_on_the_way = int(input('3'))
    minutes_on_the_way = int(input('4'))
    return departure_hours, departure_minutes, hours_on_the_way, minutes_on_the_way


def travel_time(departure_hours, departure_minutes, hours_on_the_way, minutes_on_the_way):
    global k
    amount1 = departure_minutes + minutes_on_the_way
    if amount1 > 60:
        hours_on_the_way += 1
    amount2 = hours_on_the_way + departure_hours
    while amount2 > 23:
        amount2 -= 24
        k += 1
    return k


def arrival_time(departure_hours, departure_minutes, hours_on_the_way, minutes_on_the_way):
    arrival_minutes = departure_minutes + minutes_on_the_way
    if arrival_minutes >= 60:
        hours_on_the_way += 1
        arrival_minutes -=60
    else:
        arrival_minutes = departure_minutes + minutes_on_the_way
    arrival_hours = departure_hours + hours_on_the_way
    if arrival_hours >= 24:
        while arrival_hours >= 24:
            arrival_hours -= 24
    return arrival_hours, arrival_minutes


def main():
    departure_hours, departure_minutes, hours_on_the_way, minutes_on_the_way = entry()
    a_hours, a_minutes = arrival_time(departure_hours, departure_minutes, hours_on_the_way, minutes_on_the_way)
    print(f"{a_hours} hours : {a_minutes} minutes")
    time = travel_time(departure_hours, departure_minutes, hours_on_the_way, minutes_on_the_way)
    print(f"{time} days")


k = 0
a_hours = 0
a_minutes = 0
if __name__ == "__main__":
    main()
