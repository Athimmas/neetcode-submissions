class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while right > left:
            r = s[right]
            l = s[left]

            if(r.isalnum() and l.isalnum()):
                if(r.lower() == l.lower()):
                    right-=1;
                    left+=1;
                    continue
                else:
                    return False

            if(not r.isalnum()):
                right-=1;

            if(not l.isalnum()):
                left+=1;

        return True