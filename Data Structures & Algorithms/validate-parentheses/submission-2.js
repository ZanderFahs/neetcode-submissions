class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];
        const key = {
            ']': '[',
            '}': '{',
            ')': '(',
        };
        for (let c of s){
            if(key[c]){
                if(stack.length > 0 && stack[stack.length - 1] === key[c]){
                    stack.pop();
                }else{
                    return false;
                }
            }else{
                stack.push(c);
            }
        }
        return stack.length === 0;
    }
}
