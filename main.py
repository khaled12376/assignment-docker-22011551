from nltk.corpus import stopwords
from collections import Counter


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words


text = read_file('paragraphs.txt')

filtered_words = remove_stop_words(text)

word_count = Counter(filtered_words)

sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_word_count:
    print(f'{word}: {count}')


