def floodFill(image, sr, sc, color):
    start = image[sr][sc]
    queue = [(sr, sc)]
    visited = set()
    while len(queue) > 0:
        sr, sc = queue.pop()
        visited.add((sr, sc))
        image[sr][sc] = color
        for sr, sc in neighbours(image, sr, sc, start):
            if (sr, sc) not in visited:
                queue.append((sr, sc))
    return image

def neighbours(image, sr, sc, start):
    indices = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
    result = []
    for sr, sc in indices:
        if isValid(image, sr, sc) and image[sr][sc] == start:
            result.append((sr, sc))
    return result

def isValid(image, sr, sc):
    if sr >= 0 and sc >= 0 and sr < len(image) and sc < len(image[0]):
        return True 

image_t = [[1,1,1],[1,1,0],[1,0,1]]
sr_t = 1
sc_t = 1
color_t = 2
print(floodFill(image_t, sr_t, sc_t, color_t))
