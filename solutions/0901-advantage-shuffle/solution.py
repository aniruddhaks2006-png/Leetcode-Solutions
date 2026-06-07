class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        indexed_nums2 = sorted(enumerate(nums2), key=lambda x: x[1])

        res = [0] * len(nums1)
        left, right = 0, len(nums1) - 1
        for num in nums1:
            if num > indexed_nums2[left][1]:
                idx = indexed_nums2[left][0]
                res[idx] = num
                left += 1
            else:
                idx = indexed_nums2[right][0]
                res[idx] = num
                right -= 1
        return res
