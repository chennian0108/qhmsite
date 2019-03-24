#开发人员  ：chennian
#开发时间  ：2019/3/17  14:52
#文件名称  ：WeCharPay.PY
#开发工具  ：PyCharm
#pay=input("请输入消费金额 ：\n")
#print("付款金额为： "+pay)
#print("付款成功，对方已收款！")
import time

#struct_time = time.strptime("30 Nov 00", "%d %b %y")
#print("返回的元组: %s" % struct_time)
import time
struct_time=time.strptime("30 Nov 00","%d %b %y")
print("返回的元组："+str(struct_time))