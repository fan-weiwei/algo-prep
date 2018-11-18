corpus = ['oath','pea','eat','rain']

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]



import time
start_time = time.time()

class Node:
    def __init__(self, val=None):
        self.next = dict()
        self.val = val
        self.is_word = False

# returns 'eat', 'oath'
def cross(A, B):
    return [(a,b) for a in A for b in B]

adj = dict()

for row, col in cross(range(4), range(4)):
    local_adjacent = set(cross([row - 1, row, row + 1], [col - 1, col, col + 1]))
    local_adjacent -= {(row, col)}
    local_adjacent = set(filter(lambda x: x[0] in range(4) and x[1] in range(4), local_adjacent))
    adj[(row, col)] = local_adjacent

print(adj)


def add_word_to_node(word, node):
    if len(word) == 0:
        node.is_word = True
        return

    letter = word[0]
    if letter not in node.next:
        next_node = Node(letter)
        node.next[letter] = next_node

    add_word_to_node(word[1:], node.next[letter])

word_lookup = Node()
for word in corpus:
    add_word_to_node(word, word_lookup)



histories = []
def step(row, col, history, node):

    letter = board[row][col]
    results = []
    if letter in node.next:

        #print(letter, len(history))

        for next_row, next_col in adj[(row, col)]:

            # Check if we've been there already
            if (next_row, next_col) in history: continue

            results += step(next_row, next_col, history + [(row, col)], node.next[letter])
            if node.next[letter].is_word:
                return results + [history + [(row, col)]]


    return results

def solve():

    found_histories = []
    for row, col in cross(range(4), range(4)):
        result = step(row,col, [], word_lookup)
        if result:
            found_histories += result

    found_words = set()
    for history in found_histories:
        string = ''
        for loc in history:
            string += board[loc[0]][loc[1]]
        found_words.add(string)

    end_time = time.time()

    #print(found_histories)
    print(found_words)
    print('time taken: {:.6f} ms'.format(end_time - start_time))


solve()