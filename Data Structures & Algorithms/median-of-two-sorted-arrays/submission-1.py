class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #we will try to binary search on the smaller array and decide the number of elements will we take from the smaller array on the left side 
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        n1,n2=len(nums1),len(nums2)
        is_even=True if (n1+n2)%2==0 else False
        left_size=(n1+n2+1)//2
        #now we will binary search on the number of elements we will be taking from the smaller array(nums1) on left side
        low,high=0,n1
        while low<=high:
            mid=int(low+(high-low)/2) #number of elements on left side from nums1 array
            left_size_nums2=left_size-mid
            l1,l2,r1,r2=float('-inf'),float('-inf'),float('inf'),float('inf')
            

            if mid!=0: l1=nums1[mid-1]
            if mid!=n1: r1=nums1[mid]

            if left_size_nums2!=0: l2=nums2[left_size_nums2-1]
            if left_size_nums2!=n2: r2=nums2[left_size_nums2]

            if l1<r2 and l2<r1:
                if is_even:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            elif l1>r2:
                high=mid-1 #need to reduce number of elements from nums1 in left part 
            else:
                low=mid+1

        return 0                        

        