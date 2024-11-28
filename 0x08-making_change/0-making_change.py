#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed to meet a given amount.
"""

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

    # Initialize dp array with a large value (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total of 0

    # Update dp array for each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If total is not reachable, return -1
    return dp[total] if dp[total] != float('inf') else -1

