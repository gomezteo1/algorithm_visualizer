import random

from core.config import (
    ARRAY_SIZE,
    MIN_VALUE,
    MAX_VALUE
)


def generate_random_data():

    return [
        random.randint(MIN_VALUE, MAX_VALUE)
        for _ in range(ARRAY_SIZE)
    ]