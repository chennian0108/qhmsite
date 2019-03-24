#开发人员  ：chennian
#开发时间  ：2019/3/17  13:56
#文件名称  ：3-17-1.PY
#开发工具  ：PyCharm
import datetime
imyear=input("请输入您的出生年份：  ")
nowyear=datetime.datetime.now().year
age=nowyear-int(imyear)
print("您的年龄是: "+str(age )+"岁")
if age<18:
    print("您现在为未成年人 ~@_@~")
if age>=18 and age <66:
    print("您现在为青年人~")
if age>=66 and age<80:
    print("您现在为中年人~")
if age>=80:
    print("您现在为老年人~")
