class Solution {
    /*
        https://leetcode.com/problems/calculate-digit-sum-of-a-string/

        Loop until string s is shorter than integer k:
        1. Split the string into chunks of size k.
        2. Sum up digits of each of the chunks.
        3. Concatenate results as string into a results.

     */

    public String digitSum(String s, int k) {
        while (s.length() > k) {
            StringBuilder nextS = new StringBuilder();
            for (int i = 0; i < Math.ceil(s.length() / (float) k); i++) {
                // split into chunks
                int endIndex = Math.min((i + 1) * k, s.length());
                String substring = s.substring(i * k, endIndex);
                int sum = 0;
                for (int j = 0; j < substring.length(); j++) {
                    // Byte encoding of digit characters can be reverted by substracting offset of the zero character.
                    sum += s.charAt(i * k + j) - '0';
                }
                nextS.append(sum);
                /*
                Slower but easy to understand alternative:
                 int sum = Arrays.stream(substring.split("")).map(Integer::valueOf).reduce(0, Integer::sum);
                 */
            }
            s = nextS.toString();

        }
        return s;
    }

    public static void main(String[] args) {
        assert new Solution().digitSum("11111222223", 3).equals("135");
    }

}