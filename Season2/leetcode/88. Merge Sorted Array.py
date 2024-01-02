class Solution:
    def merge(self, nums1, m, nums2, n):    
        tmp = nums1[:m]
        nums1_idx = 0
        nums2_idx = 0
        
        while nums1_idx < m and nums2_idx < n:
            if tmp[nums1_idx] <= nums2[nums2_idx]:
                nums1[nums1_idx + nums2_idx] = tmp[nums1_idx]
                nums1_idx += 1
            else:
                nums1[nums1_idx + nums2_idx] = nums2[nums2_idx]
                nums2_idx += 1
        
        while nums1_idx < m:
            nums1[nums1_idx + nums2_idx] = tmp[nums1_idx]
            nums1_idx += 1
        
        while nums2_idx < n:
            nums1[nums1_idx + nums2_idx] = nums2[nums2_idx]
            nums2_idx += 1
        
        print(nums1)

if __name__== '__main__':
    '''
    Example 1:

    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

    Example 2:

    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].

    Example 3:

    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
    '''
    
    sol = Solution()
    
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3
    sol.merge(nums1, m, nums2, n)
    
    nums1 = [1]
    nums2 = []
    m, n = 1, 0
    sol.merge(nums1, m, nums2, n)
    
    nums1 = [0]
    nums2 = [1]
    m, n = 0, 1
    sol.merge(nums1, m, nums2, n)