def score_word(word):
    scored_words = []
    for word in data:
        word_low = word.lower()
        if scrabble_word(word_low):
            total = 0
            for letter in word_low:
                total = total + scores[letter]
            scored_words.append([total, word_low])
    return sorted(scored_words, reverse = True)
