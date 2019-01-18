



def permutations(s):
    if len(s) == 1:
        return [s]

    result = []
    for char in s:
        tail_list = permutations(s.replace(char, ''))

        mapped = list(map(lambda x : char + x, tail_list))
        result += mapped
    return result

if __name__ == '__main__':

    print(permutations('abc'))