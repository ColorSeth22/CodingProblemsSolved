import string
from typing import Counter

# need to replace this levenshtein distance with 
# Damerau lvenshtein distance, this is awful, I have made a mistake
# def levenshtein_distance(word, correct_spelling):
    # using dynamic programming to calculate the levenshtein distance
    # between two words and returning that distance
    # https://en.wikipedia.org/wiki/Levenshtein_distance#Computing_Levenshtein_distance
    # matrix = [[0 for _ in range(len(correct_spelling) + 1)] for _ in range(len(word) + 1)]

    # # create an index dictionary
    # da = {ch: 0 for ch in set(word + correct_spelling)}

    # # Initialize the first row and column
    # for i in range(len(word) + 1):
    #     matrix[i][0] = i
    # for j in range(len(correct_spelling) + 1):
    #     matrix[0][j] = j

    # # Fill the matrix using dynamic programming
    # for i in range(1, len(word) + 1):
    #     db = 0
    #     for j in range(1, len(correct_spelling) + 1):
    #         i1 = da[correct_spelling[j - 1]]
    #         j1 = db
    #         if word[i - 1] == correct_spelling[j - 1]:  # Characters match
    #             substitution_cost = 0
    #         else:  # Characters don't match
    #             substitution_cost = 1

    #         matrix[i][j] = min(
    #             matrix[i - 1][j] + 1,                  # Deletion
    #             matrix[i][j - 1] + 1,                  # Insertion
    #             matrix[i - 1][j - 1] + substitution_cost,  # Substitution


    #             # need to figure out how to add the tranposition to the matrix, 
    #             # this makes it so that the option to do a swap is possible.
    #             # https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
    #             matrix[i1][j1] + (i - i1 - 1) + substitution_cost + (j - j1 - 1)  # transposition
    #         )

    # # Return the Levenshtein distance (bottom-right corner of the matrix)
    # print(word, correct_spelling, matrix[len(word)][len(correct_spelling)])
    # return matrix[len(word)][len(correct_spelling)]

# Basically the same as levenshtien_distance,
# allows for the ability to use swaps/transposition
# def damerau_levenshtein_distance(source: str, target: str) -> int:
#     source = ' ' + source
#     target = ' ' + target
#     len_s = len(source) - 1
#     len_t = len(target) - 1
#     max_dist = len_s + len_t

#     # Initialize DP matrix
#     dp = [[0] * (len_t + 2) for _ in range(len_s + 2)]
#     dp[0][0] = max_dist
#     for i in range(1, len_s + 2):
#         dp[i][0] = max_dist
#         dp[i][1] = i - 1
#     for j in range(1, len_t + 2):
#         dp[0][j] = max_dist
#         dp[1][j] = j - 1

#     # Track all previous positions of characters
#     source_positions = {ch: [] for ch in set(source)}
#     target_positions = {ch: [] for ch in set(target)}

#     for i in range(2, len_s + 2):
#         for j in range(2, len_t + 2):
#             cost = 0 if source[i - 1] == target[j - 1] else 1

#             # Basic operations
#             dp[i][j] = min(
#                 dp[i - 1][j - 1] + cost,  # substitution
#                 dp[i][j - 1] + 1,         # insertion
#                 dp[i - 1][j] + 1          # deletion
#             )

#             # Try all valid transpositions
#             for k in source_positions.get(target[j - 1], []):
#                 for l in target_positions.get(source[i - 1], []):
#                     transposition_cost = (
#                         dp[k][l] +
#                         (i - k - 1) + cost + (j - l - 1)
#                     )
#                     dp[i][j] = min(dp[i][j], transposition_cost)

#             # Update character positions
#             source_positions[source[i - 1]].append(i - 1)
#             target_positions[target[j - 1]].append(j - 1)

#     print(source, target, dp[len_s + 1][len_t + 1])
#     return dp[len_s + 1][len_t + 1]

def damerau_levenshtein_unrestricted(a: str, b: str) -> int:
    # https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
    # used the pseudocode from the wiki page to turn this into python
    # Initialize character index dictionary
    da = {ch: 0 for ch in set(a + b)}
    
    len_a, len_b = len(a), len(b)
    maxdist = len_a + len_b

    # Initialize distance matrix with extra row/column for -1 indexing
    d = [[0] * (len_b + 2) for _ in range(len_a + 2)]
    d[0][0] = maxdist

    for i in range(1, len_a + 2):
        d[i][0] = maxdist
        d[i][1] = i - 1
    for j in range(1, len_b + 2):
        d[0][j] = maxdist
        d[1][j] = j - 1

    # flood the matrix with answers
    for i in range(1, len_a + 1):
        db = 0
        for j in range(1, len_b + 1):
            i1 = da.get(b[j - 1], 0)
            j1 = db

            cost = 0 if a[i - 1] == b[j - 1] else 1
            if cost == 0:
                db = j

            d[i + 1][j + 1] = min(
                d[i][j] + cost,                     # substitution
                d[i + 1][j] + 1,                    # insertion
                d[i][j + 1] + 1,                    # deletion
                d[i1][j1] + (i - i1 - 1) + cost + (j - j1 - 1)  # unrestricted transposition, characters dont have to be adjacent
            )
        da[a[i - 1]] = i

    return d[len_a + 1][len_b + 1]

def correct_spelling(text, word_list):
    # compare every word in the text to every word in the word_list
    # use levenshtein distance to determine if the word is a misspelling
    # if the distance is 1 or less, add the correct spelling to the list of suggestions
    # unless there is no 1s then add 2s
    answer_dict = {}
    for word in text.split(' '):
        word = word.strip(string.punctuation)
        if word not in word_list:
            print(word)
            answer_dict[word] = []
            for correct_word in word_list:
                distance = damerau_levenshtein_unrestricted(word, correct_word)
                print(word, correct_word, distance)
                if distance <= 2:
                    answer_dict[word].append((correct_word, distance))
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
# {'Her': ['her'], 'nlike': ['like', 'unlike'], 'illBE-ING': [], 'E': ['he', 'is'], "WOULD'NT": []} output


print(correct_spelling("hello-there hello -there ;*th;e*re,*?!", 
                                                ["hello", "there"]))

# {'hello-there': [], 'th;e*re': ['there']} # should equal
# {'hello-there': [], 'there': [], ';*th;e*re,*?!': []} # output