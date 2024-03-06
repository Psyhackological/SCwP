def add_time(start, duration, day=None):
    # EXTRACTING NEEDED DATA
    (time_start, time_format) = start.split(" ")
    (hour_start, minute_start) = time_start.split(":")
    (hour_duration, minute_duration) = duration.split(":")

    # PERFORMING CALCULATIONS ON HOURS AND MINUTES
    total_minutes = int(minute_start) + int(minute_duration)
    total_hours = int(hour_start) + int(hour_duration)

    # NOT ALLOWING MINUTES TO BE MORE THAN 60 AND ALSO ADDING +1 TO TOTAL HOURS
    if total_minutes > 60:
        total_hours += 1
        total_minutes -= 60

    # ADDING THE 0 WHEN MINUTES LESS THAN 10
    if total_minutes < 10:
        total_minutes = f"0{total_minutes}"

    # MAP OF THE WEEK
    week_map = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7,
    }

    # OPTIONAL VARIABLES DETERMINED LATER IF THEY HAVE TO BE USED
    extra_days = None
    day_number = None

    # GETTING THE NUMBER OF THE WEEK
    if day is not None:
        day_number = week_map.get(day.capitalize())

    # DETERMINING IF EXTRA DAYS IS NEEDED OR NOT
    if total_hours > 24 and time_format == "AM":
        # RETURNS N DAYS LATER
        n = total_hours // 24

        # RETURNS GETTING THE DAY NUMBER AND THEN NOT ALLOWING TO BE MORE THAN 7
        if day_number is not None:
            day_number += n % 7

        # RETURNS SPEAKS FOR ITSELF
        if n == 1:
            extra_days = "(next day)"
        # RETURNS LITERALLY N DAYS LATER
        else:
            extra_days = f"({n} days later)"
        # RETURNS DETERMINING IF EXTRA DAYS IS NEEDED OR NOT

    elif total_hours > 12 and time_format == "PM":
        # RETURNS N DAYS LATER
        n = (total_hours // 24) + 1

        # RETURNS GETTING THE DAY NUMBER AND THEN NOT ALLOWING TO BE MORE THAN 7
        if day_number is not None:
            day_number += n
            day_number %= 7

        # RETURNS SPEAKS FOR ITSELF
        if n == 1:
            extra_days = "(next day)"
        # RETURNS LITERALLY N DAYS LATER
        else:
            extra_days = f"({n} days later)"

    # RETURNS CHECKING IF IT IS NEEDED TO CHECK TIME FORMAT OR NOT
    if (((total_hours // 12) % 2) == 1) and (time_format == "AM"):
        time_format = "PM"
    elif (((total_hours // 12) % 2) == 1) and (time_format == "PM"):
        time_format = "AM"

    # RETURNS NOT ALLOWING THE HOURS TO BE 0 (INSTEAD OF 12)
    if (total_hours % 12) == 0:
        total_hours = 12
    # RETURNS OTHERWISE GET REAL NUMBER (CANNOT BE BIGGER THAN 12)
    else:
        total_hours %= 12

    # RETURNS USING WEEK DAY DICTIONARY TO GET KEY BY VALUE
    if day_number is not None:
        for key, value in week_map.items():
            if day_number == value:
                day = key
                break

    # RETURNS DETERMINING WHAT CASE IS THIS (THIS IS AN AND GATE)
    if extra_days is None and day is None:
        new_time = f"{total_hours}:{total_minutes} {time_format}"
    elif extra_days is not None and day is None:
        new_time = f"{total_hours}:{total_minutes} {time_format} {extra_days}"
    elif extra_days is None and day is not None:
        new_time = f"{total_hours}:{total_minutes} {time_format}, {day}"
    else:
        new_time = f"{total_hours}:{total_minutes} {time_format}, {day} {extra_days}"

    # RETURNS FINALLY FINISH
    return new_time
