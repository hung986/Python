def anagramMappings(nums1, nums2):
    countMap = {}
    arr = []
    for k, v in nums2:
        if k in countMap:
            countMap[k] += 1
        else:
            countMap[k] = 1

    for i in nums2:
        if i in countMap and countMap[i] > 0:
            arr.append(nums2.index(i))
            print(f"Mapping {i} from nums1 to index {nums2.index(i)} in nums2")
    return arr
    #add new feature to the code
    #give the user the option to input their own lists of numbers for nums1 and nums2