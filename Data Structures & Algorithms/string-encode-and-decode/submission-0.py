class Solution:

    def encode(self, strs):
        res = ""
        for s in strs: #string by string
            res += str(len(s)) + "#" + s #length of string + delimiter + string itself
        return res

    def decode(self,str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#": #while were at an integer increment j by 1
                j += 1
            length = int(str[i:j]) #the length of the string is given before the delimiter(j)
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

