from typing import List


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        """
        The input is celsius temperature which is rounded to 2 decimal places.
        Convert to Kelvin and Fahrenehit.
        Return [kelvin, fahrenheit]

        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32

        # Examples
        >>> Solution().convertTemperature(36.5)
        [309.65, 97.7]

        >>> Solution().convertTemperature(122.11)
        [395.26, 251.798]

        """

        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32

        return [kelvin, fahrenheit]