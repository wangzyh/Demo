# 167. Two Sum II - Input array is sorted
# 2020/7/4


def main(numbers, target: int):
    for i in range(len(numbers)):
        minus = target-numbers[i]
        if minus in numbers[i+1:]:
            return [i+1, numbers[i+1:].index(minus)+i+2]


if __name__ == '__main__':
    a = main(numbers=[1,2,2,13], target=4)
    print(a)
