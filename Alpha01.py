"""
This module has funtions and methods 
to tokenize an input string
"""
class Tokenizer(object):
    """This class has method to tokenize an input string"""
    def tokenize(self,s):
    """This function divides a string in a list of alphabetical substrings."""
        i = 0
        result = [] 
        if len(s) == 0:
            result = []
        else:
            # check if obj is/isn`t alpha
            for a,b in enumerate(s):

                if b.isalpha():
                    # the beginning of the substring
                    # can be the first char in string
                    # or if not, the first alpha
                    # that code can find in string
                    # (previous is not alpha)

                    if a == 0 or not s[a-1].isalpha():
                        i = a
                else:
                    i = a + 1
                # if it is not the last char in the string
                if (a+1 <= len(s)-1):
                    # code finds the end of substring
                    # and adds it to list
                    if b.isalpha() and not s[a+1].isalpha():
                        result.append(s[i:a+1])
            # code goes till the end of the string
            # and if the last one is alpha adds it
            if b.isalpha():
                result.append(s[i:])

        return result

def main():
    t = Tokenizer()
    s = input()
    print(t.tokenize(s))

if __name__== '__main__':
    main()
