class Solution {
    public boolean hasDuplicate(int[] nums) {
        List<Integer> list = new ArrayList<Integer>();

        for (var num: nums)
        {
            if (list.contains(num))
                return true;
            
            list.add(num);
        }

        return false;
    }
}
