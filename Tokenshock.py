"""
This module has funtions and methods 
to tokenize an input string
"""
def tokenize(s):
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
    
    def defcat(char):
        
        if char.isalpha():
            category = 'alpha'
            
        if char.isspace():
            category = 'space'
            
        if char.isdigit():
            category = 'digit'

        if unicodedata.category(char)[0] == 'P':
            category = 'punct'
            
        else:
            category = 'unk'
            
        return category

    def tokcat(self, string):

        i = 0
        result2 = []
        if len(s) == 0:
            result = []
        else:
            for a,b in enamurate(s):
                category = self.defcat(char)

                if i == 0:
                    index = i
                    prevcat = category

                if (a+1 <= len(s)-1):
                    if category != prevcat:
                        tok = s[index:i]
                        n = Token(tok, category, index, i)
                        result2.append(n)
                        index = i
                        prevcat = category

                tok = s[index:]
                i = i + 1
                n = Token(tok, category, index, i)
                result2.append(n)
            return result2
        
class Token (object):

    def __init__(self, tok, category, firsti, lasti):

        self.firstindex = firsti
        self.lastindex = lasti
        self.token = tok
        self.category = category

    def __repr__(self):

        return '(' + self.token + ':' + self.category + ',[' + str(self.firstindex) + ',' + str(self.leastindex) + '])'

    def __eq__(self, other):
        

    def main():
    t = Tokenizer()
    s = input()
    print(t.tokenize(s))

if __name__== '__main__':
    main()
