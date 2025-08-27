def add_prefix_un(word):
    return 'un' + word

def make_word_groups(vocab_words):
    return ' :: '.join([vocab_words[0]] + [vocab_words[0] + word for word in vocab_words[1:]])

def remove_suffix_ness(word):
    if word.endswith('iness'):
        return word[:-5] + 'y'
    else:
        return word[:-4]

def adjective_to_verb(sentence, index):
    words = sentence.strip('.').split()
    return words[index] + 'en'
