from typing import List

def sort_words(words: List[str]) -> List[str]:
    # Sort by word length in descending order
    return sorted(words, key=len, reverse=True)

def sort_numbers(numbers: List[int]) -> List[int]:
    # Sort by absolute value in ascending order
    return sorted(numbers, key=abs)


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))
print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))