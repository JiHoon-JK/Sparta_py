import random


def get_lotto():
    lotto_range = range(1, 45)
    lotto_num = random.sample(lotto_range, 6)
    return lotto_num


print(get_lotto())
