line=1
data=True
with open("sample.txt","r") as f:
    line=1
    data=True
    while data:
        data=f.readline()
        if("python" in data):
         print(f"word found at line  {line}")
         break

        line+=1
