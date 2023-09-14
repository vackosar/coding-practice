class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        Absent (A), Late (L), Present (P).
        Absent max 2 days in total.
        Never late more than 3 days in a row (consecutive).
        Return true if above is true.

        """

        absent = 0
        too_late = 0

        consecutive_late_count = 0
        for c in s:
            if c == 'A':
                absent += 1

            if c == 'L':
                consecutive_late_count += 1
                if consecutive_late_count > 2:
                    too_late += 1

            else:
                consecutive_late_count = 0

        return absent < 2 and too_late == 0