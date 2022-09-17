class CheckStringUniqueness:
    def __init__(self) -> None:
        pass

    def validateBySet(self, text):
        if self.isUniqueBySet(text):
            print('OK')
        else:
            print('NO')

    def isUniqueBySet(self, text):
        if len(text) > 256:
            return False

        chars = set()
        for x in text:
            chars.add(x)
        
        if len(text) == len(chars):
            return True
        
        return False

    def validateByArray(self, text):
        if self.isUniqueByArray(text):
            print('OK')
        else:
            print('NO')

    def isUniqueByArray(self, text):
        if len(text) > 256:
            return False

        chars = [False] * 256

        for x in text:
            val = ord(x)
            if chars[val] == True:
                return False
            chars[val] = True

        return True

    def validateByBit(self, text):
        if self.isUniqueByBit(text):
            print('OK')
        else:
            print('NO')

    def isUniqueByBit(self, text):
        if len(text) > 26:
             return False

        checker = 0

        for x in text:
            val = ord(x) - ord('A')
            if checker & (1 << val) > 0:
                return False
            checker |= 1 << val
        
        return True

    def validateBySort(self, text):
        if self.isUniqueBySort(text):
            print('OK')
        else:
            print('NO')

    def isUniqueBySort(self, text):
        sorted_text = sorted(text)
        for i in range(len(text)-1):
            if sorted_text[i] == sorted_text[i+1]:
                return False
        
        return True



csu = CheckStringUniqueness()
csu.validateBySet('ABCDEF')
csu.validateBySet('ABCCDEFF')
csu.validateBySet('ZFEDCBA')

csu.validateByArray('ABCDEF')
csu.validateByArray('ABCCDEFF')
csu.validateByArray('ZFEDCBA')

csu.validateByBit('ABCDEF')
csu.validateByBit('ABCCDEFF')
csu.validateByBit('ZFEDCBA')

csu.validateBySort('ABCDEF')
csu.validateBySort('ABCCDEFF')
csu.validateBySort('ZFEDCBA')