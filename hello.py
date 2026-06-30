def anagramMappings(nums1, nums2):
    countMap = {}
    arr = []
    for k, v in nums2:
        if k in countMap:
            countMap[k] += 1
        else:
            countMap[k] = v

    for i in nums2:
        if i in countMap and countMap[i] > 0:
            arr.append(nums2.index(i))
            countMap[i] -= 1
    return arr
