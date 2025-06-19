def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1
            
        for c in t:
            count[ord(c) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False

        return True