def findCenter(edges):
    if edges[0][0] in edges[1]:
        return edges[0][0]
    return edges[0][1]



edges_t = [[1,2],[5,1],[1,3],[1,4]]
print(findCenter(edges_t))