//方法1
class Solution {
    public int findRepeatNumber(int[] nums) 
    {
        Set<Integer> dic = new HashSet<>();
        for(int num : nums)
        {
            if(dic.contains(num))
                return num;
            dic.add(num);
        }
        return -1;
    }
}



//方法2
class Solution {
    public int findRepeatNumber(int[] nums) 
    {
        int i = 0;
        while(i<nums.length)
        {
            if(nums[i]==i)
            {
                i+=1;
                continue;
            }
            if(nums[nums[i]] == nums[i])
                return nums[i];
            int tmp = nums[i];
            nums[i] = nums[tmp];
            nums[tmp] = tmp; 
        }
        return -1;
    }
}
