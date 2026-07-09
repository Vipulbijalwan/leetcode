class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i=0;
        
        while(i<nums.length-1){
            int j=1+i;
        while(j<nums.length){
            if(nums[i]+nums[j] == target){
                int[] arr =new int[2];
                arr[0]=i;
                arr[1]=j;
                return arr;
            }
            j++;
        }
        i++;
        }
        return new int[2];
    }
}