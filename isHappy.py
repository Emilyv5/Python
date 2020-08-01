def isHappy(n):
    seen = set()
    while n!= 1:
        cur = 0
        while n!= 0:
            cur += (n%10)**2
            n //=10
        if cur in seen:
            return False
        seen.add(cur)
        n = cur
    return True

print('hello')
print(isHappy(200))

class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n!= 1:
            cur = 0
            while n!=0:
                cur += (n%10)**2
                n //=10
            if cur in seen:
                return False
            seen.add(cur)
            n = cur
    return True
    

