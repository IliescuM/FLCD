# https://github.com/IliescuM/FLCD
import SymbolTable
import sys
import re
from finite_automata import *

reserved_words = ["ifGo","elseGo","not" ,"or" ,"whileGo", "and", "print", "for", "False", "True" ,"readFrom" ,"writeFrom","int" ,"char", "string" ]

reserved_ops =["+" ,"-" ,"*" ,"/" ,"%" ,"&", "|", "==", "!=" , ">", "<", ">=" ,"<=", ";","=", '"' ]

reserved_separators = [" ",";","{","}","(",")",","]

check_token_type_const = FA("finite_automataConst.json")
check_token_type_INT = FA("finite_automataINT.json")

class PIF:
    def __init__(self):
        self.__data = []

    def __setitem__(self, key, pos):
        self.__data.append((key, pos))

    def __str__(self):
        return "\n".join(map(str, self.__data))

    def tokens(self):
        return list(map(lambda x: x[0], self.__data))




class LexicalScanner:
    def __init__(self,filename):
        self.symblTable = SymbolTable.SymbolTable(1000)
        self.pif = PIF()
        self.filename = filename
    
# check if token is constant or identifier with regex
    def check_token_type(self,token):
        if token in reserved_words or token in reserved_ops or token in reserved_separators or token =="":
            return 0
            # match from beginning to end any character that  start with one char of [a-zA-Z_] and continue with any alpha-numeric char or underscore
            # if the return of re.match() is not None means that we have a match and the token is an identifier
        if check_token_type_const.check(token) or check_token_type_INT.check(token):
            return 3

        # if re.match(r'^[a-zA-Z_][a-zA-Z_0-9]*$',token) is not None:
        #     return 1 # identifier
        #     # match for negative/positive numbers taking in account that numbers that start with 0 are invalid (e.g: 0123) and only digit 0 is correct.
        #     # if the return of re.match() is not None means that we have a match and the token is a constant
        # if re.match(r'^(-+)?[1-9][0-9]*$|0',token) is not None :
        #     return 2 # constant

# short description of lexicalScanner() function:
# after opening the file we parse line by line and take the tokens to verify what kinf of tokens we have 
# only if the token is an identifier or a constant we add it to the SymbolTable
# the pif is the Program Internal Form in which we have tha array of pairs (token, position in SymbolTable) ( if the token is reserved word/ operator/ separator it will have the pos -1)
#  
    def lexicalScanner(self):
        zero = 1
        
        with open(self.filename) as f:
            line_i = 1
            line = f.readline()
            while line:
               
                splitL = line.split() # spliting the line into tokens 
                #print(splitL,"\n")
                for token in splitL:
                    tokenType = self.check_token_type(token)
                    #print(str(tokenType) + "tipul de token",'\n')
                    if tokenType == 0:
                        self.pif[token] = -1
                    elif tokenType == 1 or tokenType ==2 or tokenType ==3:
                        index = self.symblTable.add(token)
                        self.pif[token] = index

                    else:
                        # tokenError = token
                        # lineError = line_i
                        raise Exception("Lexical error. Invalid token: '{}' on line {}".format(token,line_i))
                        # zero = 0
                line = f.readline()
                line_i += 1

        return self.symblTable,self.pif

    

if __name__ == "__main__":
    lScanner=LexicalScanner("p3.txt")
    try:
        symbTable,pif = lScanner.lexicalScanner()
        print("\n Lexical correct!!!!!!! \n")
        original_stdout = sys.stdout
        with open("PIF.out",'w') as f:
            sys.stdout = f
            print(pif)
            sys.stdout = original_stdout 
        with open("ST.out",'w') as f:
            sys.stdout = f
            print(symbTable)
            sys.stdout = original_stdout     
        print(str(symbTable),"\n")
        print(pif)
    except Exception as e:
        print(e)
    



        
