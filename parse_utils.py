import re
from word2number import w2n

def extract_number_from_text(text):
    try:
        return int(w2n.word_to_num(text))
    except:
        match = re.search(r'\d+', text)
        return int(match.group()) if match else 1

def words_to_digits(text):
    word_to_digit = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    words = text.lower().split()
    digits = [word_to_digit.get(word, "") for word in words]
    return ''.join(digits)
