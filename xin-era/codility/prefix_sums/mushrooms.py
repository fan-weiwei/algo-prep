

def poor_solution(field, start, moves, count=0):

    if start < 0 or start >= len(field):
        return 0

    new_field = field.copy()

    count += new_field[start]
    new_field[start] = 0

    if moves == 0:
        return count

    return max(poor_solution(new_field, start - 1, moves - 1, count),
               poor_solution(new_field, start + 1, moves - 1, count))

def better_solution(field, start, moves):

    n = len(field) -1

    prefix = []
    tally = 0
    for item in field:
        tally += item
        prefix.append(tally)

    result = 0
    final = 0

    ## Assume left first
    for offset in range(moves + 1):
        left = max(0, start - offset)
        right = max(min(n, left + (moves - offset)), start)

        if left == 0:
            result = prefix[right]
        else:
            result = prefix[right] - prefix[left - 1]
        final = max(result, final)

    ## Assume right now
    for offset in range(moves + 1):
        right = min(n, start + offset)
        left = min(start, max(0, right - (moves - offset)))

        if left == 0:
            result = prefix[right]
        else:
            result = prefix[right] - prefix[left - 1]

        #print('Left {}, Right {}, Offset {}, Result {}'.format(left, right, offset,result))
        final = max(result, final)


    return final


if __name__ == '__main__':


    field = [2, 3, 7, 5, 1, 3, 9]
    start = 4
    moves = 6


    solution = poor_solution(field, start, moves)
    print(solution)

    solution = better_solution(field, start, moves)
    print(solution)