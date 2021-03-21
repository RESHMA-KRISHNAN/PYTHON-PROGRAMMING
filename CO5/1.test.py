str= "I felt happy \n because I saw the others were happy \n and because I knew I should feel happy \n but I was not really happy.""\n"
fw=open("Dict.txt","w")
fw.write(str)
fw.close()

fr=open("Dict.txt","r")
str1=fr.readlines()
print("Dict.txt contains:\n",str1)