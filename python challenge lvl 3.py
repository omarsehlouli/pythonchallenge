from pathlib import Path
txt = Path('level3.txt').read_text()
txt = txt.replace('\n', '')
result=""
for i in range(3,len(txt)-3):
  sum=0;
  if(txt[i].islower()==True):
      for j in range(1,4):
        if (txt[i+j].isupper()==True):
          sum+=1
        if (txt[i-j].isupper()==True):
         sum+=1
  if(sum==6 and txt[i-4].islower() and txt[i+4].islower()) : result+=txt[i]
print(result)
