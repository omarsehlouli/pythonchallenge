import zipfile
import re

varia="90052"
txt=".txt"
comments = []

zf = zipfile.ZipFile('level6.zip', 'r')
L=zf.namelist()
for i in range(len(L)-1):
  comments.append(zf.getinfo(str(varia) + ".txt").comment)
  with zf.open(varia+txt) as myfile:
    for line in myfile:
      if re.search("\d+", str(line)):
        varia = re.findall("\d+", str(line))
        varia = "".join(varia)
for i in range(len(comments)):
  comments[i]=comments[i].decode("utf-8")
  
print("".join(comments))


    

