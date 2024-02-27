import re

def nfa(i, state):
    ns = state + 1
    return f"{state}-->{i}-->{ns}"
    
def accurance(state):
    ns = state + 1
    return f"{ns}-->e-->{state}"

def check(vc):
    regex  = re.split()
    state = 0
    
    for i in regex:
        if "*" not in i and "/" not in i:
            print(nfa(i,state))
            state += 1
        elif "*" in i:
            starting_node = state
            char = i[:-1]
            ns = state + 1
            print(f"{state}-->e-->{ns}")
            
            state += 1
            print(nfa (char,state))
            print(accurance(state))
            state += 1
            ns = state + 1
            print(f"{state}-->e-->{ns}")
            state += 1
        elif "/" in i:
             char = i.replace("/"," ")
             var =  char.split()
             starting_node = state
             for j in var:
                ns = state + 1
                print(f"{state}-->e-->{ns}")
                state += 1
                print(nfa(j,state))
                state += 1
             ns = state + 1
             print(f"{state}-->e-->{ns}")
             state -= 2
             print(f"{state}-->e-->{ns}")

re = input("Enter regular expression:")
check(re)
