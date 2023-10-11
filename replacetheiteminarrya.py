

def replacetheitem(nums1 , nums2):
    j = 0
    for i in range(len(nums1)):
        if nums1[i] == 0 and j < len(nums2):
            nums1[i] = nums2[j]
            j += 1
    nums1[:] = sorted(nums1)
    return nums1

print(replacetheitem([1,2,0,0,5],[3,4]))