def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage (potential error)
averages = [calculate_average([1, 2, 3]), calculate_average([]), calculate_average([4, 5, 6])]
print(averages)