from collections import Counter

def analyze_text(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)

    word_freq = Counter(words)
    most_common = word_freq.most_common(1)[0] if word_freq else ("None", 0)

    print("\n Text Analysis:")
    print(f"Total words: {word_count}")
    print(f"Total characters: {char_count}")
    print(f"Most Frequent word: '{most_common[0]}' (appears {most_common[1]} times)")
    print("\nWord Frequencies:")
    for word, freq in word_freq.items():
        print(f"'{word}': {freq} times")

def main():
    print("Enter your text (end input with an empty line):")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)

    full_text = ' '.join(lines)
    analyze_text(full_text)

if __name__ == "__main__":
    main()