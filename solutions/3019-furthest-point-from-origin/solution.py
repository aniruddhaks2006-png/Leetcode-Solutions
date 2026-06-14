class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=0
        r=0
        sp=0
        for i in moves:
            if i=="L":
                l+=1
            elif i=="R":
                r+=1
            else:
                sp+=1
        return max(l,r)+sp-min(l,r)
        
