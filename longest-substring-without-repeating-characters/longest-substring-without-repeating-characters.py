class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        hashset = set()

        max_len = 1

        start = 0
        end = 1
        hashset.add(s[0])

        while start <= end and end < len(s):
            if s[end] not in hashset:
                hashset.add(s[end])
                max_len = max(max_len, end - start + 1)
                print(s[start:end+1])
                end += 1


            else:
                while True:
                    hashset.remove(s[start])
                    if s[start] == s[end]:
                        start += 1
                        break
                    start += 1

                hashset.add(s[end])
                end += 1

        return max_len