import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        
        if (s.length() < 2) {
            return false;
        }
        
        int i = 0;
        while (i < s.length()) {
            char ch = s.charAt(i);
            
            if (ch == '(' || ch == '{' || ch == '[') {
                stk.push(ch);
            } else if (!stk.isEmpty() && 
                      ((ch == '}' && stk.peek() == '{') || 
                       (ch == ')' && stk.peek() == '(') || 
                       (ch == ']' && stk.peek() == '['))) {
                stk.pop();
            } else {
                return false;
            }
            
            i++;  
        }
        
        return stk.isEmpty();
    }
}
