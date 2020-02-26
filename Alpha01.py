class Tokenizer(object):

    def tokenize(self,s):
    
        i = 0
        result = [] 
        if len(s) == 0:
            result = []

        for a,b in enumerate(s):

            if b.isalpha():
                if a == 0 or not s[a-1].isalpha():
                    i = a
            else:
                i = a + 1
        
            if (a+1 <= len(s)-1):
        
                if b.isalpha() and not s[a+1].isalpha():
                    result.append(s[i:a+1])

        if b.isalpha():
            result.append(s[i:])

        return result

def main():
    t = Tokenizer()
    s = input()
    print(t.tokenize(s))

if __name__== '__main__':
    main()
