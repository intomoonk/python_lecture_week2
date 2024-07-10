def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

numbers = [10,11,2,7,155,10]
average = calculate_average(numbers)
print(average)