image_test = [[1,1,0],[1,0,1],[0,0,0]]

def solve(image):
    res = []
    for arr in image:
        res_part = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                res_part.append(1)
            else:
                res_part.append(0)
        res.append(res_part)
    return res

print(solve(image_test))