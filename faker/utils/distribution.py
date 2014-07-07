import bisect
import random


def random_sample(seed=None):
    if seed is not None:
        random.seed(seed)
    return random.uniform(0.0, 1.0)


def cumsum(it):
    total = 0
    for x in it:
        total += x
        yield total


def searchsorted_right(a, v):
    return bisect.bisect_right(a, v)


def choice_distribution(a, p, seed=None):
    assert len(a) == len(p)

    cdf = list(cumsum(p))
    cdf2 = cdf[:]
    cdf = [i / cdf[-1] for i in cdf2]
    uniform_sample = random_sample(seed)
    idx = searchsorted_right(cdf, uniform_sample)

    return a[idx]
