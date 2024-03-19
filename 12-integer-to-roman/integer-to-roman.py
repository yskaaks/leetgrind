class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1000: "M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"
        }
        res = []

        for value, symbol in roman_dict.items():
            count = num // value

            if count != 0:
                res.append(symbol * count)
                num -= value * count
            if num == 0:
                break
        return ''.join(res)