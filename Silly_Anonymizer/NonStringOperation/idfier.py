# idfier module

"""
Tests if randomIdfier() correctly generates unique IDs
"""
name = "idfier"
if __name__ == "__main__":
    ls = randomIdfier(["name01", "name02"])
    if len(set(ls.values())) == 2:
        print("randomIdfier() is ok.")
        print(ls)
    else: 
        print("randomIdfier() is not ok.")
        print(ls)
        
    
else:
    print(name, "is used as a module")
    
    

"""

"""    
__ids = []
    
import random as rn

def randomIdfier(names):
    global __ids
    outputDict = {}
    for name in names:
        id = rn.randint(1000, 9999) 
        
        while id in __ids:  
            id = rn.randint(1000, 9999)     
        __ids.append(id)
        outputDict[name] = id 

    return outputDict
    

    
