class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        """
        Input are sentence string and discount integer percent.
        Retrun a sentence with the percent discount applied and exactly two decimal places prices.

        Sentence string is a space separated words and digits with dollar signs.
        Only allowed symbols are lower case, digit, dollar.
        Price word has a format of f"${digits}".


        You could just split, parse, and format. But then you would consume O(N).
        Which it will anyway, as I need to build the output.
        Could use some streaming to safe memory.


        # Python Split and Regex Solution

        output_words = []
        regex = re.compile(r'^\$([0-9]+)$')
        discount_multiplier = (1.0 - discount / 100.0)
        for word in sentence.split(' '):
            match = regex.fullmatch(word)
            if match is not None:
                price = int(match.groups(0)[0])
                d_price = discount_multiplier * price
                word = f"${d_price:.2f}"

            output_words.append(word)

        return ' '.join(output_words)


        # Regex FindIter Generator Solution

        discount_multiplier = (1.0 - discount / 100.0)
        regex = re.compile(r'(\$([0-9]+)|[^ ]+)( +|$)')
        def match_to_word(match):
            groups = match.groups()
            if groups[1] is not None:
                price = int(groups[1])
                d_price = discount_multiplier * price
                word = f"${d_price:.2f}"

            else:
                word = groups[0]

            return word

        return ' '.join(match_to_word(match) for match in regex.finditer(sentence))

        """

        # Python Split and Isdigit

        output_words = []
        discount_multiplier = (1.0 - discount / 100.0)
        for word in sentence.split(' '):
            if word[0] == "$" and word[1:].isdigit():
                price = int(word[1:])
                d_price = discount_multiplier * price
                word = f"${d_price:.2f}"

            output_words.append(word)

        return ' '.join(output_words)


assert "there are $0.50 $1.00 and 5$ candies in the shop" == Solution().discountPrices("there are $1 $2 and 5$ candies in the shop", 50)
assert "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$" == Solution().discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100)
# Subscribe at https://vaclavkosar.com/