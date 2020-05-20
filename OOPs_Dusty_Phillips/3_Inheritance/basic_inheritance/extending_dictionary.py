class LongestKey(dict):
    def longest_key(self):
        longest = None
        print(self)
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


l = LongestKey()
l['ckjldfbvdfouvblidf'] = 1
l['kdjbvsdjbvlsdiu'] = 2
l['ksdfjhvbdfvjdhvksfdhvkdhvkj'] = 3
print(l.longest_key())
l2 = LongestKey()
print(l2.longest_key())