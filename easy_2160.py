class Solution:
    def minimumSum(self, num: int) -> int:
        # get all digits
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10
        # iteratively get two smallest digits to form two
        # sub num
        num1, num2 = 0, 0
        while digits:
            min1 = min(digits)
            num1 *= 10
            num1 += min1
            digits.remove(min1)

            min2 = min(digits)
            num2 *= 10
            num2 += min2
            digits.remove(min2)
        # return the sum
        return num1 + num2
