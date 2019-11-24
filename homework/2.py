d = dict(xixi=170,haha=180,hoho=190)
name = input("输入姓名：")
for key in d.keys():
    if d[key] > d[name]:
        print (key, d[key])
