#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Parameters:
    coins (list): List of coin denominations.
    total (int): The total amount to achieve.

    Returns:
    int: Fewest number of coins needed, or -1 if total cannot be achieved.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Build up the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still 'inf', the total cannot be met with given coins
    return dp[total] if dp[total] != float('inf') else -1
