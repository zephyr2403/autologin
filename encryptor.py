
from string import letters
from random import choice
'''
CLASS THAT HELPS TO ENCRYPT AND DECRYPT DETAILS BEFORE INSERTING IN THE DATABASE
'''
class Encryptor(object):
    
    random_ = letters + '0123456789'

    def encrypt(self,string):
        string = bytearray(string)

        for i in range(len(string)):
            if string[i] > 96 and string[i] < 123:
                if string[i] > 118:
                    val = string[i] - 118   + 64
                    string[i] = val
                else:
                    string[i] = string[i] - 28
            elif string[i] > 64 and string[i] < 91:
                if string[i] > 86:
                    val = string[i] - 86   + 96
                    string[i] = val
                else:
                    string[i] = string[i] + 36
            elif string[i] > 47 and string[i] < 58:
                if string[i] > 53:
                    val = string[i] - 53 + 47
                    string[i] = val 
                else:
                    string[i] = string[i] + 4

        string = str(string) 
        string = list(string)
        string = [choice(self.random_) + letter + choice(self.random_) for letter in string]
        string = ''.join(string)
        return str(string)

    def decrypt(self,string):
       
        string = [string[i:i+3] for i in range(0,len(string),3)]
        print string
        string = [item[1] for item in string]
        string = ''.join(string)
        string = bytearray(string)

        for i in range(len(string)):
            if string[i] > 64 and string[i] < 91 :
                if string[i] <  69 :
                    string[i] = string[i] - 64   + 118
                else:
                    string[i] = string[i] + 28

            elif string[i] > 96 and string[i] < 123:
                if string[i] < 101:
                    string[i] = string[i] - 96 + 86
                else:
                    string[i] = string[i] - 36
            elif string[i] > 47 and string[i] < 58:
                if string[i] < 52:
                    string[i] = string[i] - 47 + 53
                else :
                    string[i] = string[i] - 4
        
        return str(string)
