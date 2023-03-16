# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# DONE: The min() function finds the minimum value
print(f"Minimal value is {min(values)}")
print(f"Minimal value is {min(strings)}")

# DONE: The max() function finds the maximum value
print(f"Maximum value is {max(values)}")
print(f"Maximum value is {max(strings)}")

# DONE: define a custom "key" function to extract a data field
print(f"Minimal value is {min(strings, key=len)}")
print(f"Maximum value is {max(strings, key=len)}")

# DONE: open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print(data["metadata"]["title"])
print(len(data["features"]))


def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if magnitude is None:
        magnitude = 0
    return float(magnitude)


print(f'Minimal value is {min(data["features"], key=getmag)}')
print(f'Maximum value is {max(data["features"], key=getmag)}')
