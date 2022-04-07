# stringProcess module



"""
prints out whether the script is imported as a module or a script
"""
name = "stringProcess"
if __name__ == "__main__":
    print(name, "is used as a script")
else:
    print(name, "is used as a module")

"""
stringSplit - takes a string as input and split it based on the separator to produce a list with the splitted sections
"""
def stringSplit(string, separator):
    outputList = string.split(sep=separator)
    return outputList