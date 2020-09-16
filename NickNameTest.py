def fun_checkout(name):
    nickName = ""
    if name == "邓肯":                            #如果输入的是邓肯
        nickName = "石佛"
    elif name == "吉诺比利":                      #如果输入的是吉诺比利
        nickName = "妖刀"
    elif name == "罗宾逊":                        #若果输入的是罗宾逊
        nickName = "海军上将"
    else:
        nickName = "无法找到您输入的信息"
    return nickName                               #返回球员对应的绰号

while True:
    name = input("请输入NBA球员名称：")            #接收用户输入
    nickname = fun_checkout(name)                 #调用函数
    print("球员：",name,"绰号：",nickname)         #显示球员及对应的绰号