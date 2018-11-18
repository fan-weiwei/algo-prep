#Merging two sorted list
#We have two sorted lists, and we want to write a function to merge the two lists into one sorted list:

a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]




def merge(a, b):

    #assume lists are positive and non-empty
    # a little sloppy
    result = []
    index = (0,0)

    while index[0] < len(a) or index[1] < len(b):

        if index[0] < len(a):
          next_a = a[index[0]]

        if index[1] < len(b):
          next_b = b[index[1]]

        if index[0] == len(a):

            result += [next_b]
            index = (index[0], index[1] + 1)
            continue

        if index[1] == len(b):
            result += [next_a]
            index = (index[0] + 1, index[1])
            continue

        if next_a > next_b:
            # then add b
            result += [next_b]
            index = (index[0] , index[1] + 1)
            continue

        if next_b > next_a:
            result += [next_a]
            index = (index[0] + 1, index[1])
            continue

        if next_a == next_b:
            result += [next_a, next_b]
            index = (index[0] + 1, index[1] + 1)
            continue

    return result



print(merge(a,b))