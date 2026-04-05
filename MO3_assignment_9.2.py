def get_odds():
    """Generator function that yields odd numbers from range(10)."""
    for number in range(10):
        if number % 2 != 0:
            yield number

# Use a for loop to find and print the third value returned
count = 1
for odd in get_odds():
    if count == 3:
        print(f"The third odd number is: {odd}")
        break
    count += 1