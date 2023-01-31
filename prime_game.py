def is_winner(x, nums):
    """
    Function that returns the winner of the prime game
    """
    wins_maria, wins_ben = 0, 0
    # Play the rounds
    for i in range(x):
        prime_numbers = _get_amount_prime_numbers(nums[i])
        if prime_numbers == 0:
            pass
        elif prime_numbers % 2 == 0:
            wins_ben += 1
        else:
            wins_maria += 1
    # Assess the winner
    if wins_ben == wins_maria:
        return None
    return "Ben" if wins_ben > wins_maria else "Maria"


def _get_amount_prime_numbers(num):
    """
    Given a number returns the amount of prime numbers from 2 to that number
    """
    total_prime_numbers = 0
    for i in range(2, num + 1):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            total_prime_numbers += 1

    return total_prime_numbers
