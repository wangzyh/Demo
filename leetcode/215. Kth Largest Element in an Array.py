def main(nums, k):
    import heapq
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heapq.heappop(heap)

    # return sorted(nums)[-k]



if __name__ == '__main__':
    a = main([3, 2, 1, 5, 6, 4], k=2)
    print(a)
