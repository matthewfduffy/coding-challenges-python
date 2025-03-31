def timeConversion(s):
    # Write your code here
    time_to_convert = s.strip()
    hours = str(time_to_convert[0] + time_to_convert[1])
    minutes = str(time_to_convert[3] + time_to_convert[4])
    seconds = str(time_to_convert[6] + time_to_convert[7])
    denom = str(time_to_convert[8] + time_to_convert[9])

    if denom.upper() == 'PM':
        if hours == "12":
            pass
        else:
            hours = str(int(hours) + 12)

    if denom.upper() == 'AM' and hours == "12":
        hours = "00"

    return hours + ":" + minutes + ":" + seconds





# Test(s)
a = "01:05:10PM"
b = "12:11:11PM"

print(timeConversion(a))
print(timeConversion(b))