# Silly_Anonymizer

A simple Python package created as part of an online tutorial on packaging Python Modules into Package.

## Modules

1. idfier: contains one function `randomIdfier()`. It takes a list of strings and assigns randomly generated numbers as unique IDs.
2. stringProcess: contains one function `stringSplit()`. It takes a string as input and split it based on the separator to produce a list with the splitted sections.

## Example

### stringProcess
import Anonymizer.StringOperation.stringProcess as sp
names = sp.stringSplit(string="Arafath, Samuel, Tiara, Nathan, Moez", separator=",")
print(names)

### idfier
import Anonymizer.NonStringOperation.idfier as idf
idf.randomIdfier(names)

## Version
1.0.0
