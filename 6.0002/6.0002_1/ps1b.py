###########################
# 6.0002 Problem Set 1b: Space Change

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always an egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    assert 1 in egg_weights
    assert all(x<y for x, y in zip(egg_weights, egg_weights[1:]))

    dp = [0 for i in range(target_weight+1)]
    for i in range(1, target_weight+1):
        dp[i] = 1 + min([dp[i-weight] for weight in egg_weights if weight<=i])
    return dp[target_weight]


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    # Test 1
    print("--- Test 1 ---")
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights =", egg_weights)
    print("n =", n)
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    # Test 2
    print("--- Test 2 ---")
    egg_weights = (1, 5, 10, 20, 50)
    n = 208
    print("Egg weights =", egg_weights)
    print("n =", n)
    print("Expected ouput: 8 (4 * 50 + 1 * 5 + 3 * 1 = 208)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    # Test 3 （注意）
    print("--- Test 3 ---")
    egg_weights = (1, 9, 90, 91)
    n = 99
    print("Egg weights =", egg_weights)
    print("n =", n)
    print("Expected ouput: 2 (1 * 90 + 1 * 9)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    # Test 4
    print("--- Test 4 ---")
    egg_weights = (1,)  # 只有一个元素的元组不能省略逗号
    n = 13
    print("Egg weights =", egg_weights)
    print("n =", n)
    print("Expected ouput: 13 (13 * 1 = 13)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    # Test 5
    print("--- Test 5 ---")
    egg_weights = (1, 2, 4, 8, 16, 32, 64)
    n = 127
    print("Egg weights =", egg_weights)
    print("n =", n)
    print("Expected ouput: 7 (等比数列求和)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    # Wrong test
    # print("--- Wrong Test ---")
    # egg_weights = (1, 2, 4, 8, 16, 128, 64)  # 没有1
    # n = 127
    # print("Actual output:", dp_make_weight(egg_weights, n))
    # print()