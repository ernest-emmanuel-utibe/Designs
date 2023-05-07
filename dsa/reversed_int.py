def reversed_int(self, number):
    x = number.length
    for i in range(x.length):
        x[i] = number[x.length - i - 1]

    return x


if __name__ == '__main__':
    num = {4, 6, 8, 9, 2, 5}

    print(f"The Reversed Array is: {num}")
    # print(reversed_int(number))
