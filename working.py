"""
implement a function called convert that expects a str in either of the 12-hour formats 
below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect 
that AM and PM will be capitalized (with no periods therein) and that there will be a space 
before each. Assume that these times are representative of actual times, not necessarily 9:00 AM 
and 5:00 PM specifically.
"""
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d{1,2}:\d{2})\s?(AM|PM)"
    match = re.search(pattern, s)
    if match:
        time = match.group(1)
        period = match.group(2)
        hours, minutes = map(int, time.split(":"))
        
        if period == "AM":
            if hours == 12:
                hours = 0
        elif period == "PM":
            if hours != 12:
                hours += 12
        
        return f"{hours:02}:{minutes:02}"
    
    raise ValueError("Invalid time format")


if __name__ == "__main__":
    main()