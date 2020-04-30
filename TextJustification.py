import math

# L is the list of words and M is the size of each line
def justify(L, M):
    size = len(L)

    # cost[i][j] --> cost of a line with words i to j
    cost = [[0 for x in range(size)] for x in range(size)]

    # fill the cost 2_D_arr with extra spaces.
    # cost[i][j] --> no. of extra spaces if words from i to j are in a line 
    for i in range(size):
        cost[i][i] = M-len(L[i])
        for j in range(i+1, size):
            cost[i][j] = cost[i][j-1] - len(L[j]) - 1

    for i in range(size):
        for j in range(i, size):
            if cost[i][j] < 0:                  # if words from i to j can not be in a line
                cost[i][j] = math.inf
            else:                               # else square the extra spaces
                cost[i][j] = cost[i][j]**2      # it it the badness factor --> some times power 3
    
    # for every guess of j, find the minimum cost for justifying from i to j, j varying from i to th end
    # min_cost[i] --> the minimum penalty to justify words from i to the end
    min_cost = [0 for x in range(size)]
    res = [0 for x in range(size)]
    
    for i in range(size-1, -1, -1):
        min_cost[i] = cost[i][size-1]       # first set it to the cost of justifying from i to the end
        res[i] = size

        for j in range(size-1, i, -1):
            if cost[i][j-1] == math.inf:
                continue
            elif min_cost[i] > min_cost[j] + cost[i][j-1]:         # if the new j have the minimum penalty of justifying
                min_cost[i] = min_cost[j] + cost[i][j-1]
                res[i] = j

    print("cost: ", cost)
    print("min_cost: ", min_cost)
    print("res: ", res)

    print("\n~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.\n")

    # to print the answer
    indexes = []
    x = 0
    while x < size:
        tmp = res[x] - x - 1            # count number of spaces based on how many words it is in a line.
        y = 0
        for y in range(x, res[x]):
            tmp += len(L[y])
        indexes += [tmp]
        x = res[x]
    print("indexes: ", indexes)
    
    return min_cost[0]

# L = ["Sara", "Limooee", "likes","to","code"]
# print("minumum penalty: ", justify(L, 10))

L = ["22", "333", "1","4444", "4444", "666666"]
print("minumum penalty: ", justify(L, 8))