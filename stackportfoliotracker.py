import os

# 1. Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOG": 150.00,
    "AMZN": 175.00,
    "MSFT": 400.00
}

def display_market_prices():
    print("\n--- Available Stocks & Current Prices ---")
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price:.2f}")
    print("-----------------------------------------\n")

def main():
    print("Welcome to the Simple Stock Portfolio Tracker!")
    display_market_prices()
    
    portfolio = {}
    total_investment = 0.0
    
    # 2. User Input Loop
    while True:
        symbol = input("Enter stock symbol (or type 'done' to finish): ").strip().upper()
        
        if symbol == 'DONE':
            break
            
        if symbol not in STOCK_PRICES:
            print(f"Sorry, '{symbol}' is not in our system. Please try a valid stock.")
            continue
            
        try:
            quantity = int(input(f"How many shares of {symbol} do you own? "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")
            continue
            
        # Add or update the stock quantity in the portfolio
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} shares of {symbol}.\n")

    # 3. Calculation & Display
    if not portfolio:
        print("\nYour portfolio is empty. Goodbye!")
        return

    print("\n==============================")
    print("      YOUR PORTFOLIO SUMMARY   ")
    print("==============================")
    
    summary_lines = []
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = quantity * price
        total_investment += value
        
        line = f"{symbol}: {quantity} shares x ${price:.2f} = ${value:.2f}"
        print(line)
        summary_lines.append(line)
        
    total_line = f"\nTotal Portfolio Value: ${total_investment:.2f}"
    print("------------------------------")
    print(total_line)
    print("==============================")

    # 4. Optional File Handling (Saving the result)
    save_choice = input("\nWould you like to save this summary to a text file? (y/n): ").strip().lower()
    if save_choice == 'y':
        file_name = "portfolio_summary.txt"
        with open(file_name, "w") as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write("=======================\n")
            for line in summary_lines:
                file.write(line + "\n")
            file.write("-----------------------\n")
            file.write(total_line + "\n")
        print(f"Success! Summary saved to '{os.path.abspath(file_name)}'.")
    else:
        print("Summary not saved. Thank you for using the tracker!")

if __name__ == "__main__":
    main()
