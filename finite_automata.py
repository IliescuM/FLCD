import json

class FA:
    def __init__(self, file_path):
        with open(file_path) as f:
            self.data = json.load(f)

        self._states = self.data["states"]
        self._alphabet = self.data["alphabet"]
        self._transitions = {}
        self._final_states = self.data["final_states"]

        for key, value in self.data["transitions"].items():
            dictionary = {}
            #print(key)
            for ikey, ivalue in value.items():
                #print(type(ikey))
                for i in ikey:
                    #print(a)
                    if i in dictionary.keys() and dictionary[i] != ikey:
                        raise Exception("Automaton is not deterministic")
                    dictionary[i] = ivalue
                self._transitions[key] = dictionary
                    
        self.__done = False
        self.__menu = {
            "1": self.__display_states,
            "2": self.__display_alphabet,
            "3": self.__display_transitions,
            "4": self.__display_final_states,
            "5": self.__check_sequence,
            "6": self.__close
        }
    
    def __display_states(self):
        print("\n States: \n"+str(self.data["states"])+"\n")

    def __display_alphabet(self):
        print("\n Alphabet: \n"+str(self.data["alphabet"])+"\n")

    def __display_transitions(self):
        print("\n Transitions: \n"+str(self.data["transitions"])+"\n")

    def __display_final_states(self):
        print("\n Final states: \n"+str(self.data["final_states"])+"\n")

    def __close(self):
        self.__done = True

    def menu(self):
        while not self.__done:
            self.__print_menu()
            c = input("Insert option from menu>> ")
            fun = self.__menu[c]
            if c is not None:
                fun()
            else:
                print("Unrecognized input")



    def __print_menu(self):
        print("1. Display states\n"
         "2. Display alphabet\n"
         "3. Display transitions\n"
         "4. Display final states\n"
         "5. Check sequence\n"
         "6. Close\n")

    def __check_sequence(self):
        seq = input("Insert sequence:\n")
        if self.__check(seq):
            print("Valid sequence")
        else:
            print("Invalid sequence")

## short description of __check() function:
# in this function we check if for a DFA , verify if a sequence is accepted by FA
# fisrt we check that the sequence is part of the alphabet
# next stept is to identify the state "type" that we are in 
# and for the last step we check that the last state is part of the final_state set.
    def __check(self, sequence):
        state = "initial"
        for a in sequence:
            if a not in self._alphabet:
                return False
            try:
                next_state = self._transitions[state][a]
                print(next_state)
            except KeyError:
                return False
            state = next_state
        if state not in self._final_states:
            return False
        return True
    
    def check(self, sequence):
        return self.__check(sequence)

if __name__ == "__main__":
    fa = FA("finite_automataConst.json")
    fa.menu()
    