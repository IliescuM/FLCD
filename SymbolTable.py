# 1 a 
class SymbolTable:

    def __init__(self, size):
        self.__table = [None] * size
        self.__size = size
    
    # in: key - dicitonary key
    # out : returns a hash code for the key
    def hashfun(self,key):
        return hash(key) % self.__size

    # in: key - dicitonary key
    # out: adds the key to the table and the position of the key is returned
    # to avoid duplicating the pos if x == key : break.
    def add(self,key):
        pos = self.hashfun(key)
        print(pos)
        if self.__table[pos] is None:
            self.__table[pos] = []
            self.__table[pos].append(key)
        else:
            for x in self.__table[pos]:
                if x == key:
                    break
                else:
                    self.__table[pos].append(key)
        return pos

    # in: key - dicitonary key
    # out: value correspoding to the key and None if key is not found 

    def __getItem__(self,key):
        pos = self.hashfun(key)
        if self.__table[pos] is None:
            return None
        else:
            for x in self.__table[pos]:
                if x == key:
                    return pos
            return None
   
   
    # in: key - dicitonary key
    # out: key if deleted from the table otherwise it raises Exception
    def __delitem__(self,key):
        pos = self.hashfun(key)
        if self.__table[pos] is None:
            raise Exception()
        else:
            for i,x in enumerate(self.__table[pos]):
                if x == key:
                    del self.__table[pos][i]
                    break
            else:
                raise Exception()
    
    def __str__(self):
        return str(self.__table)

    
def teste():
    nl="\n"
    table = SymbolTable(30)
    table.add("define")
    table.add("declare")
    table.add("whileGo")
    table.add("writeFrom")
    table.add("ifGo")
    
    print(table,nl)

    table1 = SymbolTable(10)
    table1.add("writeFrom")
    print(table1,nl)
    del table1["writeFrom"]
    print(table1,nl)

    table3 = SymbolTable(1)
    table3.add("define")
    table3.add("declare")
    

    print(table3,nl)

    #fail
    table2 = SymbolTable(10)
    print(table2,nl)
    del table2["writeFrom"]

    




if __name__ == "__main__":
    teste()
    
