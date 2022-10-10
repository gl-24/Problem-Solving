class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack,res = deque(),[]
        for i in range(len(nums2)-1,-1,-1):
            if not stack:
                res.append(-1)
            elif stack[-1] > nums2[i]:
                res.append(stack[-1])
            else:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                if stack and stack[-1] > nums2[i]:
                    res.append(stack[-1])
                else:
                    res.append(-1)
            stack.append(nums2[i])
        res = res[::-1]
        ans = []
        for num in nums1:
            ans.append(res[nums2.index(num)])
        return ans
                    
            