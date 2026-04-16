from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)

user_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

parts = user_input.split(",")

parts = strip_whitespaces(parts)

numbers = []
valid = True

for item in parts:
    if item.replace("-", "").isdigit():
        numbers.append(float(item))
    else:
        print("Data Error: Please make sure you only enter numbers separated by commas.")
        valid = False
        break

if valid:
    cleaned = remove_duplicates(numbers)

    print("Cleaned and unique data:", cleaned)
    print("--------------------")
    print("Mean:", round(calculate_mean(cleaned), 2))
    print("Maximum:", find_maximum(cleaned))
    print("Minimum:", find_minimum(cleaned))