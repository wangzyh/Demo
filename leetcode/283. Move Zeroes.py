def main(nums):
    A = nums
    k = 0
    for j in range(len(A)):
        if A[j] != 0:
            A[k] = A[j]
            k += 1

    for i in range(k, len(A)):
        A[i] = 0

if __name__ == '__main__':
    a = main([0,1,0,3,12])
    print(a)
