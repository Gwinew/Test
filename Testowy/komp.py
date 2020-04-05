import os
a = input("Podaj nazwe katalogu w ktorym bedzie plik exe: ")
b = input("Podaj nazwe skryptu (.py) do skompilowania: ")
c = "FreezePython --install-dir"+" "+a+" "+b
os.system(c)
