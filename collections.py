from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

strs = ["eat", "tea", "badcredit", "ate", "listen", "silent", "debitcard"]
print(group_anagrams(strs))
