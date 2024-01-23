
import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Using regular expression to find all occurrences of "um" as a whole word
    um_occurrences = re.findall(r'\bum\b', s, flags=re.IGNORECASE)
    return len(um_occurrences)

if __name__ == "__main__":
    main()
