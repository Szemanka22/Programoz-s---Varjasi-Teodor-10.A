#1. fileból lista mátrixkezeléssel

import sys
import os

def filetolist(filename:str) -> list[str]:
    f = open(filename, encoding='utf-8')
    sorok = f.readlines()
    return(sorok)


if len(sys.argv) < 2:
    print("nem létező fájlnév")
elif not os.path.exists(sys.argv[1]):
    print("nem létező fájlév")

else:
    filename = sys.argv[1]
    print(filetolist(filename))
    print(os.path.exists(sys.argv[1]))

