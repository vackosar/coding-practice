class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # TODO size limits
        # TODO handle negative numbers
        sign = -1
        max_pos = (1 << 30) - 1 + (1 << 30)
        max_neg = -1 << 31

        # flip to negative as more space there
        if dividend < 0 and divisor >= 0:
            sign = -1
            divisor = -divisor
            # dividend = -dividend

        elif dividend >= 0 and divisor < 0:
            sign = -1
            dividend = -dividend
            # divisor = -divisor

        elif dividend < 0 and divisor < 0:
            sign = +1
            # divisor = -divisor
            # dividend = -dividend

        else:
            sign = +1
            divisor = -divisor
            dividend = -dividend

        def get_bit_length(num: int):
            if num == 0:
                return 0

            for i in range(33):
                if num >> i == -1:
                    return i + 1

                if num >> i == 0:
                    return i

        if divisor == 0:
            raise ValueError()

        if dividend == 0:
            return 0

        result = 0
        dd_len = get_bit_length(dividend)
        # ds_len = get_bit_length(divisor)
        reminder = dividend

        for rot in range(dd_len, -1, -1):
            m_divisor = divisor << rot
            result = result << 1
            if reminder - m_divisor > 0:
                continue

            else:
                reminder = reminder - m_divisor
                result = result - 1

        if sign < 0:
            return result

        else:
            if max_neg == result:
                return max_pos

            else:
                return -result
