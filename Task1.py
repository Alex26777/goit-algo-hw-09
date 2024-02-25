def find_coins_greedy(amount, coins):
    """
    Жадібний алгоритм для визначення кількості монет для формування суми.
    :param amount: Сума для видачі решти.
    :param coins: Доступні номінали монет.
    :return: Словник із кількістю монет кожного номіналу.
    """
    result = {}
    for coin in sorted(coins, reverse=True):
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    return result

def find_min_coins(amount, coins):
    """
    Алгоритм динамічного програмування для визначення мінімальної кількості монет.
    :param amount: Сума для видачі решти.
    :param coins: Доступні номінали монет.
    :return: Словник із номіналами монет та їх кількістю для досягнення заданої суми.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Відновлення відповіді: які монети використані
    result = {}
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break
    return result

# Демонстрація роботи функцій
coins = [50, 25, 10, 5, 2, 1]
amount = 113

print("Жадібний алгоритм:", find_coins_greedy(amount, coins))
print("Динамічне програмування:", find_min_coins(amount, coins))