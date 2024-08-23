def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.upper() in str(other_words[i]).upper():
            same_words.append(other_words[i])
        elif str(other_words[i]).upper() in root_word.upper():
            same_words.append(other_words[i])
        else:
            continue
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies', 'ri')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel', 'MENT')
print(result1)
print(result2)
