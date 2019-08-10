# complexity is linear time

class KMP(object):
    def __init__(self, pattern, text):
        self.text = text
        self.pattern = pattern
        self.text_len = len(text)
        self.pat_len = len(pattern)
        self.lps = [0]*self.pat_len
    
    def compute_LPS(self):
        len = 0
        self.lps[0] = 0
        i = 1

        while i < self.pat_len:
            if self.pattern[i] == self.pattern[len]:
                len += 1
                self.lps[i] = len
                i += 1

            elif len != 0:
                len = self.lps[len - 1]
            
            else:
                self.lps[i] = 0
                i += 1
    
    def KMPSearch(self):
        i, j = 0, 0
        self.compute_LPS()

        while j < self.text_len:
            if self.pattern[i] == self.text[j]:
                i += 1
                j += 1
            
            if i == self.pat_len:
                print(f"Found pattern at index: {j-i}")
            
            elif i < self.text_len and self.pattern[i] != self.text[j]:
                if i != 0:
                    i = self.lps[i - 1]
                else:
                    j += 1
    
if __name__ == "__main__":
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    kmpsearch = KMP(pat, txt)
    kmpsearch.KMPSearch()
