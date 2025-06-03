def count_word_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        words = text.split()
        print(f"Total words in '{filename}': {len(words)}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    filename = input("Enter the filename (with .txt extension): ")
    count_word_in_file(filename)

if __name__ == "__main__":
    main()