"""Generator which stores n values provided by user
Values calculated based on equation provided 'num_next = (num_previous * 3) // 5'
num_previous chosen randomly"""
def generator(user_input):
    num_previous = 1000
    """Iterating as many times as user provided"""
    for _ in range(user_input):
        num_next = (num_previous * 3) // 5.
        num_previous = num_next
        """Stores calculated value"""
        yield num_next


"""Iterates through generator object and prints the value as many times as user provides"""
def print_generator_values(user_input):
    values = generator(user_input)
    for value in values:
        print(value)


print_generator_values(5)

