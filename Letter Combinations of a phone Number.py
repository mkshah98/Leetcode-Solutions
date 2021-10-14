class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters=[""]
        if len(digits)==0:
            return []
        for i in digits:
            letter=[]
            if i=='2':
                for i in letters:
                    letter.append(i+'a')
                    letter.append(i+'b')
                    letter.append(i+'c')
            elif i=='3':
                for i in letters:
                    letter.append(i+'d')
                    letter.append(i+'e')
                    letter.append(i+'f')
            elif i=='4':
                for i in letters:
                    letter.append(i+'g')
                    letter.append(i+'h')
                    letter.append(i+'i')
            elif i=='5':
                for i in letters:
                    letter.append(i+'j')
                    letter.append(i+'k')
                    letter.append(i+'l')
            elif i=='6':
                for i in letters:
                    letter.append(i+'m')
                    letter.append(i+'n')
                    letter.append(i+'o')
            elif i=='7':
                for i in letters:
                    letter.append(i+'p')
                    letter.append(i+'q')
                    letter.append(i+'r')
                    letter.append(i+'s')
            elif i=='8':
                for i in letters:
                    letter.append(i+'t')
                    letter.append(i+'u')
                    letter.append(i+'v')
            elif i=='9':
                for i in letters:
                    letter.append(i+'w')
                    letter.append(i+'x')
                    letter.append(i+'y')
                    letter.append(i+'z')
            else:
                letter.append([])
            letters=letter
        return letters
