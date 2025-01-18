import random

def get_numbers_ticket(min_val, max_val, quantity):
    if not (1 <= min_val <= 1000 and 1 <= max_val <= 1000 and min_val <= max_val and 1 <= quantity <= max_val - min_val + 1):
        return []

    numbers = random.sample(range(min_val, max_val + 1), quantity)
    numbers.sort()
    return numbers

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 60, 6)
print("Ваші лотерейні числа:", lottery_numbers)