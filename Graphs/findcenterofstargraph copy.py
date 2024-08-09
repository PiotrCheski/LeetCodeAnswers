def findCenter(edges):
    candidates = []
    for num in edges[0]:
        candidates.append(num)
    for num in edges[1]:
        if num in candidates:
            candidates = [num]
    return candidates[0]



edges_t = [[1,2],[5,1],[1,3],[1,4]]
print(findCenter(edges_t))