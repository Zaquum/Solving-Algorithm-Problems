class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = [
            "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return below_20[num - 1] + " "
            elif num < 100:
                return tens[num // 10 - 2] + " " + helper(num % 10)
            elif num < 1000:
                return below_20[num // 100 - 1] + " Hundred " + helper(num % 100)
            else:
                for idx, word in enumerate(thousands):
                    if num < 1000 ** (idx + 1):
                        return helper(num // (1000 ** idx)) + word + " " + helper(num % (1000 ** idx))

        return helper(num).strip()