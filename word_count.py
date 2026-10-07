import string
import sys
from collections import Counter


def read_words(filename):
    with open(filename, encoding='utf-8') as file:
        text = file.read()

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()


def top_words_with_counter(words, n=5):
    return Counter(words).most_common(n)


def top_words_with_dict(words, n=5):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    sorted_words = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]


def print_result(title, result):
    print(title)
    for word, count in result:
        print(f'  {word}: {count}')


if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'text.txt'
    words = read_words(filename)

    print_result('Top 5 words (collections.Counter):', top_words_with_counter(words))
    print()
    print_result('Top 5 words (own dictionary):', top_words_with_dict(words))
