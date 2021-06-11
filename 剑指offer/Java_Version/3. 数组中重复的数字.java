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
