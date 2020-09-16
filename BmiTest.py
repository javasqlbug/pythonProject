def fun_bmi(person,height,weight):
    '''功能：根据身高和体重计算BMI指数
    :param person:姓名
    :param height: 身高，单位：米
    :param weight: 体重，单位：千克
    '''
    print(person + "的身高：" + str(height) + "米 \t 体重："+ str(weight) + "千克")
    bmi = weight/(height*height)                    #用于计算BMI指数，公式为“体重/身高的平方”
    print(person + "的BMI指数为：" + str(bmi))       #输出BMI指数
    #判断身材是否合理
    if bmi < 18.5:
        print("您的体重过轻 ~@_@~")
    if bmi >= 18.5 and bmi < 24.9:
        print("正常范围，注意保持(-_-)")
    if bmi >=24.9 and bmi < 29.9:
        print("您的体重过重 ~@_@~")
    if bmi >= 29.9:
        print("肥胖 ^@_@^")

fun_bmi("匿名",1.76,50)