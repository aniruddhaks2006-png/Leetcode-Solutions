class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: If either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
            
        # Map string characters directly to their integer values (No ord required!)
        str_to_int = {
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
        }
        
        # Int-to-string mapping array for building the output string
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        # Convert num1 to an integer
        numbeh = 0
        for char in num1:
            numbeh = 10 * numbeh + str_to_int[char]
            
        # Convert num2 to an integer
        numah = 0
        for char in num2:
            numah = 10 * numah + str_to_int[char]
            
        # Calculate the total product
        num = numbeh * numah
        
        # Convert the product back to a string manually
        result = ""
        while num > 0:
            digit = num % 10
            result = digits[digit] + result
            num //= 10
            
        return result
