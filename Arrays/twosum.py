class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        tmp = {}
        ans = []
        for indx, ele in enumerate(nums):
            tmp[ele] = tmp.get(ele, []) + [indx]

        for indx, ele in enumerate(nums):
            req=target-ele
            if req in tmp:
                if req == ele:
                    if len(tmp[req])>1:
                        return (tmp[req][0], tmp[req][1])
                else:
                    return(indx, tmp[req][0])