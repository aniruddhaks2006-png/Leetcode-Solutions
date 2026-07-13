class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        scales=["", "Thousand", "Million", "Billion"]
        tens = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
        }
        ones = {
            0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
        }
        def convertHundreds(num):
            res = []
            if num >= 100:
                res.append(ones[num //100])
                res.append("Hundred")
                num%=100
            if num>=20:
                res.append(tens[num//10])
                if num%10:
                 res.append(ones[num %10])
            elif num>0:
                res.append(ones[num])
            return " ".join(res)
        ans=[]
        i=0
        while num>0:
            part=num%1000
            if part:
                word=convertHundreds(part)
                if scales[i]:
                    word+=" "+scales[i]
                ans.append(word)
            num//=1000
            i+=1
        return " ".join(ans[::-1])
