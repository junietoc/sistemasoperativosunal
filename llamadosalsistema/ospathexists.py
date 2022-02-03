import os
#os.path.exists retorna booleano True, False el cual indica si el path indicado existe

#retorna True
print(os.path.exists(os.getcwd()))

#retorna False
unexistentPath = os.path.join(os.getcwd(),"unexistentDir")
print(os.path.exists(unexistentPath))