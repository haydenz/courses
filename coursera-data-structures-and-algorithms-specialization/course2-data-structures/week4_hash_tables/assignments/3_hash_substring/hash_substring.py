# python3

''' Hints
∙ Beware of integer overflow. Use long long type in C++ and long type in Java where appropriate. 
  Take everything (mod 𝑝) as soon as possible while computing something (mod 𝑝), so that the numbers 
  are always between 0 and 𝑝 − 1.
∙ Beware of taking negative numbers (mod 𝑝). In many programming languages, (−2)%5 ̸= 3%5. Thus you can 
  compute the same hash values for two strings, but when you compare them, they appear to be different. 
  To avoid this issue, you can use such construct in the code: 𝑥 ← ((𝑎%𝑝) + 𝑝)%𝑝 instead of just 𝑥 ← 𝑎%𝑝.
∙ Use operator == in Python instead of implementing your own function AreEqual for strings, 
  because built-in operator == will work much faster.
∙ In C++, method substr of string creates a new string, uses additional memory and time for that, 
  so use it carefully and avoid creating lots of new strings. When you need to compare pattern with a 
  substring of text, do it without calling substr.
∙ In Java, however, method substring does NOT create a new String. Avoid using new String where it is 
  not needed, just use substring.
'''


def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # print(output)
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

class RobinKarp:
    _prime = 100000003
    _multiplier = 5

    def __init__(self, pattern, text):
        self.text = text
        self.pattern = pattern
        self.text_len = len(text)
        self.pattern_len = len(pattern)
        self.hash_l = [-1] * (self.text_len - self.pattern_len + 1)
        # self.result

    def precompute_hash(self):
        str_tmp = self.text[(self.text_len - self.pattern_len):self.text_len]
        self.hash_l[self.text_len - self.pattern_len] = self.poly_hash(str_tmp)
        y = 1
        for i in range(1, self.pattern_len + 1):
            y = (y * self._multiplier) % self._prime
        for i in range(self.text_len - self.pattern_len - 1, -1, -1):
            self.hash_l[i] = (self._multiplier*self.hash_l[i+1]+ord(self.text[i])
                              -y*ord(self.text[i+self.pattern_len])) % self._prime
   
    def poly_hash(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime # ord() returns Unicode char
        return ans

    def pattern_recognition(self):
        self.precompute_hash()
        result = []
        pHash = self.poly_hash(self.pattern)
        for i in range(0, self.text_len - self.pattern_len + 1):
            tHash = self.hash_l[i]
            if pHash != tHash:
                continue
            if self.pattern == self.text[i:(i+self.pattern_len)]:
                result.append(i)
        return result


if __name__ == '__main__':
    print_occurrences(RobinKarp(*read_input()).pattern_recognition())
    # print_occurrences(get_occurrences(*read_input()))

