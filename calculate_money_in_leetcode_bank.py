# TODO finish

class Solution:
    def totalMoney(self, n: int) -> int:
        """
        Hercy saves money in a bank. Starts with 1 USD on Monday.
        From Tuesday to Sundays puts +1 than the previous day.
        On next Monday, he puts +1 USD than the previous week Monday.
        Given `n` days, what is the total amount of money he saved?

        >>> Solution().totalMoney(0)
        0

        >>> Solution().totalMoney(1)
        1

        # 1+2
        >>> Solution().totalMoney(2)
        3

        # 1+2+3+4+5+6+7+2+3+4
        >>> Solution().totalMoney(10)
        37

        >>> Solution().totalMoney(20)
        96

        The simplest is to implement the counting by the days.
        But faster it would be to instead write an analytical formula.
        The formula must involve the 7-reminder, week savings calculation,
            and modification for the growth.

        If we are within the week the savings of the week are:
        3 days is odd: (3 + 1) + (3 + 1) / 2 = 3 / 2 * (3+1)
        4 days is even: 2 * (4 + 1)  = 4 / 2 * (4+1)
        i days: ( i / 2 * (i + 1))

        The week starts with n_week, progresses to n_week + 7.
        Week 1: 28
        Week 2: 2+3+4+5+6+7+8 = 7 * 1 + 1+2+3+4+5+6+7
        So each week it is `7 * n_week + 28`.

        Week 1 + Tuesday: 28 + 2 + 3 = 28

        """

        reminder_days = n % 7
        n_full_weeks = n // 7

        if reminder_days == 0:
            return (7 * (n_full_weeks - 1) + 28) * n_full_weeks

        else:
            return (7 * (n_full_weeks - 1) + 28) * n_full_weeks + int((n_full_weeks + reminder_days) / 2 * (reminder_days + 1))
