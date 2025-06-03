conversion_rates = {
    "USD": 85.54,
    "EUR": 97.60,
    "INR": 1.0,
}

def convert_currency(base, target, amount):
    if base not in conversion_rates or target not in conversion_rates:
        print("Unsupported currency.")
        return
    
    in_inr = amount * conversion_rates[base]
    converted = in_inr / conversion_rates[target]
    print(f"{amount} {base} = {converted:.2f} {target}")

def main():
    print("Available currencies:", ", ".join(conversion_rates.keys()))
    base = input("Enter base currency name: ").strip().upper()
    target = input("Enter target currency name: ").strip().upper()

    try:
        amount = float(input("Enter amount: "))
        convert_currency(base, target, amount)
    except ValueError:
        print("Please enter a valid number for the amount.")

if __name__ == "__main__":
    main()