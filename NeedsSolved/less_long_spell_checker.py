import string
from typing import Counter

# Basically the same as levenshtien_distance,
# allows for the ability to use swaps/transposition adjacently
def damerau_levenshtein_distance(source: str, target: str) -> int:
    len_a = len(source)
    len_b = len(target)
    d = [[0 for _ in range(len_b + 2)] for _ in range(len_a + 2)]

    # Create a distance matrix
    # We add 1 to the lengths to accommodate the initial empty string case
    d = [[0] * (len_b + 1) for _ in range(len_a + 1)]

    # Initialize the matrix for empty strings
    for i in range(len_a + 1):
        d[i][0] = i
    for j in range(len_b + 1):
        d[0][j] = j

    # Store the last seen index for each character in string a
    # Keys are characters, values are their last seen index (1-based for the algorithm)
    last_seen_a = {}

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            # Calculate cost for substitution
            cost = 0 if source[i - 1] == target[j - 1] else 1

            # Calculate the cost for transposition
            # We need to check if characters match previous ones in a specific way
            transposition_cost = float('inf') # Initialize with infinity
            if i > 1 and j > 1 and source[i - 1] == target[j - 2] and source[i - 2] == target[j - 1]:
                transposition_cost = d[i - 2][j - 2] + 1
            
            # Calculate the three standard edit operations
            substitution_cost = d[i - 1][j - 1] + cost
            insertion_cost = d[i][j - 1] + 1
            deletion_cost = d[i - 1][j] + 1

            # Get the minimum of the four operations
            print(transposition_cost, min(substitution_cost, insertion_cost, deletion_cost, transposition_cost))
            d[i][j] = min(substitution_cost, insertion_cost, deletion_cost, transposition_cost)
            if d[i][j] == transposition_cost:
                sourceList = list(source)
                sourceList[i - 1] = target[j - 2] 
                sourceList[i - 2] = target[j - 1]
                source = ''.join(sourceList)

        # Update the last_seen_a for the current character of a
        last_seen_a[source[i - 1]] = i

    return d[len_a][len_b]

def correct_spelling(text, word_list):
    # compare every word in the text to every word in the word_list
    # use levenshtein distance to determine if the word is a misspelling
    # if the distance is 1 or less, add the correct spelling to the list of suggestions
    # unless there is no 1s then add 2s
    answer_dict = {}
    for word in text.split(' '):
        word = word.strip(string.punctuation)
        if word not in word_list and word.lower() not in word_list and word != '':
            print(word)
            answer_dict[word] = []
            for correct_word in word_list:
                distance = damerau_levenshtein_distance(word.lower(), correct_word.capitalize() if word.istitle() else correct_word)
                if distance <= 2:
                    answer_dict[word].append((correct_word.capitalize() if word.istitle() else correct_word, distance))
            answer_dict[word] = sorted(answer_dict[word])
        
            counts = Counter([t[1] for t in answer_dict[word]])
            if counts.keys().__contains__(1):
                answer_dict[word] = [item[0] for item in answer_dict[word] if item[1] == 1]
            else:
                answer_dict[word] = [item[0] for item in answer_dict[word] if item[1] == 2]

    return answer_dict




print(correct_spelling("Her well-being is admirable, nlike his illBE-ING. E wouldn't lie, but she 'WOULD'NT'.", 
                                                 ["he", "is", "her", "his", "lie", "but", "she", "like", "unlike", "wouldn't", "admirable", "ill-being", "well-being"]))

# {'illBE-ING': ['ill-beING'], 'nlike': ['like', 'unlike'], 'E': ['He'], "WOULD'NT": ["WOULDN'T"]} should equal
# {'nlike': ['like', 'unlike'], 'illBE-ING': ['ill-being'], 'E': ['He'], "WOULD'NT": ["wouldn't"]} output

print(correct_spelling("Ther Quickk BROWN fox wont' jump over the lazy droog.", 
                                                 ["the", "fox", "dog", "jump", "over", "lazy", "door", "won't", "quick", "brown", "doggy", "their", "wouldn't", "quickly"]))

{'Ther': ['The', 'Their'], 'Quickk': ['Quick'], 'wont': ["won't"], 'droog': ['dog', 'door']} # should equal
{'Ther': ['Over', 'The', 'Their'], 'Quickk': ['Quick'], 'wont': ["won't"], 'droog': ['dog', 'door']} # output