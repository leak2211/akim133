from collections import Counter

sentence = str(input())



def split(z):
    z = [char for char in z]
    return z

def words_counter(z):
    words = z.split(' ')
    count_words = len(words)
    return count_words

def replacer(z):
    rep = z.replace(input(), '😎')
    return rep


def same_symbols_couter(z):
    z = split(z)
    count = Counter(z)
    return count

print(words_counter(sentence))
print(replacer(sentence))
print(same_symbols_couter(sentence))