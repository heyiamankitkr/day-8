import os 
#read
# f=open("sample.txt","r")# f variable stores the file object (using open we have the file object)
# data=f.read()
# print(data)
# print(type(data))
# data=f.readline()# reads data line by line
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# f.close()

# # #write
# f=open("sample.txt","w")
# f.write("123")
# #append
# f=open("sample.txt","a")
# f.write("\ni am ankit")
# #create new file
# f=open("sample2.txt","x")
# #read and write
# f=open("sample.txt","r+")
# print(f.read())
# f.write("\n i dont know what to do")
# print(f.read())
# #append and write
# f=open("sample.txt","a+")
# print(f.read())
# f.write("\n i dont know what to do")
# print(f.read())
# f.close()
# #with keyword
# with open("sample.txt","r") as f:
#     print(len(f.read()))
#delete file
os.remove("sample2.txt")