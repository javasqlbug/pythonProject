print("2018年俄罗斯世界杯四强")
team = ["法国","比利时","英格兰","克罗地亚"]
for item in team:
    print(item)

print("打出索引：")
for index,item in enumerate(team):
    print(index + 1,item)

phone = ["摩托罗拉","诺基亚","三星","OPPO"]
len(phone)
phone.append("iPhone")
len(phone)
print(phone)

grade = [98,99,97,100,96,94,89,95,100]
total = sum(grade)
print("Python理论总成绩为：",total)

print("原列表：",grade)
grade.sort()
print("升  序：",grade)

grade.sort(reverse=True)
print("降  序：",grade)

char = ['cat','Tom','Angela','pet']
char.sort()
print("区分字母大小写：",char)
char.sort(key=str.lower)
print("不区分字母大小写：",char)

price = [1200,5330,2988,6200,1998,8888]
sale = [int(x*0.5) for x in price]
print("原价格：",price)
print("打五折的价格：",sale)

saleHigh = [x for x in price if x > 5000]
print("原列表：",price)
print("价格高于5000的：" ,saleHigh)