//Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the //sum of the three integers. You may assume that each input would have exactly one solution.

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
        int n = nums.size();
        int j,k,sum,diff;
        sort(nums.begin(), nums.end());
        int min= 9999999;
        int result=0;
        for(int i =0;i<n-2;i++)
        {
            j=i+1;
            k=n-1;
            while(j<k)
            {
                sum= nums[i]+nums[j]+nums[k];
                diff = abs(sum-target);
                if(diff==0)
                    return sum;
                if(diff<min)
                {
                    min=diff;
                    result=sum;
                }
                if(sum<=target)
                    j++;
                else
                    k--;
            }
            
        }
        return result;
        
    }
};
