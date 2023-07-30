sentence = "way a is there will a is there where"

def reverse_sentence(sentence):
    str = sentence.split()
    str = ' '.join(reversed(str))
    return str

print(reverse_sentence(sentence))