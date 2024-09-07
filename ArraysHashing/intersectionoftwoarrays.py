def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

nums1_t = [1,2,2,1]
nums2_t = [2,2]
print(intersection(nums1_t, nums2_t))