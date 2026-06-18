# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total_investment = 0

# Number of stocks to enter
n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock = input("Enter stock name (AAPL, TSLA, GOOG, MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"Value of {stock}: ${value}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save result to a text file
file = open("portfolio.txt", "w")
file.write(f"Total Investment Value: ${total_investment}")
file.close()

print("Result saved in portfolio.txt")