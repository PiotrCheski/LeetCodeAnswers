gain_test = [-5,1,5,0,-7]
def largestAltitude(gain):
    tmp = 0
    res = 0
    for i in range(len(gain)+1):
        if i == 0:
            tmp = gain[0]
            gain[i] = 0
        elif i <= len(gain)-1:
            curr_tmp = gain[i]
            gain[i] = gain[i-1] + tmp
            res = max(res, gain[i])
            tmp = curr_tmp
        else:
            gain.append(gain[i-1]+tmp)
            res = max(res, gain[i])

    return res

print(largestAltitude(gain_test))