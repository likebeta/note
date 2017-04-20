#!/usr/bin/env python
# -*- coding=utf-8 -*-

# Author: likebeta <ixxoo.me@gmail.com>
# Create: 2017-04-20


def insertion_sort(arr):
    for i, v in enumerate(arr):
        j = i - 1
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v
    return arr


if __name__ == '__main__':
    import random
    for i in range(10000):
        array = [random.randint(0, 10000) for _ in range(20)]
        assert insertion_sort(array) == sorted(array)
