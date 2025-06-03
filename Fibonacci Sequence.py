def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    try:
        terms = int(input("Enter number of terms in Fibonacci sequence: "))
        if terms <= 0:
            print("Enter a positive integer.")
            return
        result = generate_fibonacci(terms)
        print("Fibonacci sequence:")
        print(" ".join(str(num) for num in result))
    except ValueError:
        print("Invalid input. Enter a valid integer.")

if __name__ == "__main__":
    main()