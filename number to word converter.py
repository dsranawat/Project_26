digit_map = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three',
    '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
    '8': 'eight', '9': 'nine'
    }

def number_to_words(num_str):
    words = [digit_map[d] for d in num_str if d in digit_map]
    return ' '.join(words)

def main():
    try:
        num_str = input("Enter a number: ")
        if not num_str.isdigit():
            print("Please enter only digits.")
            return
        print(f"The number in words is: {number_to_words(num_str)}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()