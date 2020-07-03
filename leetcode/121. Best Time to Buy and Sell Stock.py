# 121. Best Time to Buy and Sell Stock
# 2020/6/3


def main(prices):
    index = 0
    sell = 0
    for i in range(1, len(prices)):
        if prices[index] < prices[i]:
            sell = max(sell, max(prices[i:]) - prices[index])

        index += 1

    return sell


if __name__ == '__main__':
    prices = [5,424,2344,2334,2,34,4,5,7,89,666,54,3,5,7,8,9,6,3,3,5,56,9,7]
    a = main(prices)
    print(a)

