class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        result = 0
        i = 0

        if s[0] in ('-', '+'):
            sign = -1 if s[0] == '-' else 1
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            if result > (2**31 - 1 - digit) //10:
                return 2**31 - 1 if sign == 1 else -2**31

            result = result * 10 + digit
            i += 1

        return result * sign