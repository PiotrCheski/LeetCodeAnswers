from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1  # Start with a carry of 1 since we want to add 1 to the number.
        
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10  # Calculate the new carry.

            # Update the current digit to be the remainder after division by 10.
            digits[i] %= 10

        # If there's still a carry after the loop, insert it at the beginning of the list.
        if carry:
            digits.insert(0, carry)

        return digits


digits = [9]
print(Solution().plusOne(digits))