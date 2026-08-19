class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0;
        let r = nums.length - 1;
        
        while(l <= r){
            let mean = Math.floor((l + r) / 2);

            if(nums[mean] == target){
                return mean;
            }else if(nums[mean] < target){
                l = mean + 1;
            }else{
                r = mean - 1;
            }
        }
        return -1;
    }
}
