
import random

def get_lucky_numbers(amount: int) -> tuple[int]:
    '''
    returns tuple of random ints between 1-100

    :param amount: how many numbers
    :return:  tuples of random ints
    '''
    # numbers = random.choices(range(1, 100), k=amount)

    random.choices(['hi', 'hello'], k=5)
    random.sample(range(1, 101), 20)
    # return tuple(random.randint(1, 100) for _ in range(amount))
    if amount <= 0:
        return tuple()

    result = []
    for _ in range(amount):
        result.append(random.randint(1, 100))

    return tuple(result)

def input_until_lucky(lucky_numbers: tuple) -> int:
    """
    input numbers from the user until guessed the lucky number

    :param lucky_numbers: number to guess
    :return: how many attempts
    """
    count = 0
    while True:
        try:
            # critical section
            user_guess = int(input('Guess a number 1-100? '))

        except ZeroDivisionError or ValueError as e:
            print(f'invalid. {e}')
            int(input('Guess a number 1-100? '))
            continue

        if user_guess in lucky_numbers:
            print(f'Bingo! {user_guess}')
            return count

lucky_numbers = get_lucky_numbers(30)
print(lucky_numbers)
attempts = input_until_lucky(lucky_numbers)
print(f"it took you {attempts} attempts")

