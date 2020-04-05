TXT=["1","2","3"]
print(TXT)
f=open('test2.txt','w')
f.write(TXT[2])
f.close()

a=open('test2.txt').read()
print(a)
