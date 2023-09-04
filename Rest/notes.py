from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        l = 0
        r = len(nums) - 1
        res = []

        if nums[l] == target and nums[r] == target:
            return [l, r]
        
        mid = (l + r) // 2
        mid_l_l = l
        mid_l_r = mid - 1 if mid > 0 else mid + 1


        while mid_l_l < mid_l_r:
            mid_l = (mid_l_l + mid_l_r) // 2
            if nums[mid_l] == target:
                if nums[mid_l-1] == target:
                    res.append(mid_l-1)
                    res.append(mid_l)
                    return res
                elif nums[mid_l+1] == target:
                    res.append(mid_l)
                    res.append(mid_l+1)
                    return res
                res.append(mid_l)
                break
            
            if nums[mid_l] > target:
                mid_l_l = mid_l + 1
            else:
                mid_l_r = mid_l - 1

        mid_r_l = mid + 1
        mid_r_r = r 
        print(mid_r_l, mid_r_r)
    
        while mid_r_l <= mid_r_r:
            mid_r = (mid_r_l + mid_r_r) // 2
            print(mid_r)
            if nums[mid_r] == target:
                if mid_r + 1 < len(nums) - 1 and nums[mid_r+1] == target:
                    res.append(mid_r)
                    res.append(mid_r+1)
                    return res
                elif nums[mid_r-1] == target:
                    res.append(mid_r-1)
                    res.append(mid_r)
                    return res
                res.append(mid_r)
                break

            if nums[mid_r] > target:
                mid_r_l = mid_r + 1
            else:
                mid_r_r = mid_r - 1


        if len(res) == 0:
            return [-1, -1]
        
        if len(res) == 1:
            return [res[0], res[0]]
        else:
            return res


numstest = [1,4]
targettest = 4
print(Solution().searchRange(numstest, targettest))