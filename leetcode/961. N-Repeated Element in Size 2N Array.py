import numpy as np
def main(A):
    A = np.array(A)
    return np.argmax(np.bincount(A))


if __name__ == '__main__':
    a = main([1,2,3,3])
    print(a)

