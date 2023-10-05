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

        >>> Solution().totalMoney(175)
        2800

        The simplest is to implement the counting by the days.
        But faster it would be to instead write an analytical formula.
        The formula must involve the 7-reminder, week savings calculation,
            and modification for the growth.

        If we are within the week the savings of the week are:
        3 days is odd: (3 + 1) + (3 + 1) / 2 = 3 / 2 * (3+1)
        4 days is even: 2 * (4 + 1)  = 4 / 2 * (4+1)
        i days: ( i / 2 * (i + 1))

        Week 0 Sunday = 0
        Week 1 Sunday = 28
        Week 2 Sunday = 14 + 28 = 42
        Sum =

        The week starts with n_week, progresses to n_week + 7.
        Week 1: 28
        Week 2: 2+3+4+5+6+7+8 = 7 * 1 + 1+2+3+4+5+6+7
        So each week it is `7 * n_week + 28`.

        10 = Week 1 + Wednesday: 28 + 2 + 3 + 4 = 28 + (3 * 1) + 1 + 2 + 3 = 37


        # The analytical formula did not work out yet.

        reminder_days = n % 7
        n_full_weeks = n // 7

        full_weeks_sum = sum(i * 7 + 28 for i in range(n_full_weeks))
        assert full_weeks_sum == int((28 + (n_full_weeks - 1) * 7 + 28) * n_full_weeks / 2)
        assert n_full_weeks * reminder_days + int(reminder_days / 2 * (reminder_days + 1)) == sum(i * (n_full_weeks + 1) for i in range(1, reminder_days + 1))

        if reminder_days == 0:
            return full_weeks_sum * n_full_weeks

        else:
            return full_weeks_sum + n_full_weeks * reminder_days + int(reminder_days / 2 * (reminder_days + 1))

        """

        save_amount = 1
        saving_last_monday = save_amount
        total = 0
        for i in range(n):
            if i % 7 == 0 and i != 0:
                # it is monday
                saving_last_monday += 1
                save_amount = saving_last_monday

            total += save_amount
            save_amount += 1

        return total
