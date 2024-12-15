def calculate_average(numbers):
    if not numbers:
        return 0
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers")
    return sum(numbers) / len(numbers)

# Example usage
try:
    averages = [calculate_average([1, 2, 3]), calculate_average([]), calculate_average([4, 5, 6])]
    print(averages)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError as e:
    print(f"Error: {e}")

#Example of catching other errors
try:
    averages = [calculate_average([1,2,'a']), calculate_average([]), calculate_average([4, 5, 6])]
    print(averages)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError as e:
    print(f"Error: {e}")
