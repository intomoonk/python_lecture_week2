def find_max_min(numbers):
    if len(numbers) == 0:
        return None, None
    return max(numbers), min(numbers)

numbers = [5, 10, 15, 20, 25]
max_value, min_value = find_max_min(numbers)
print(max_value, min_value)