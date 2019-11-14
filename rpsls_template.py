#coding:gbk
"""
RPSLS游戏
作者：张健兴
2019 11 14
"""

import random#调用random模块
answer=random.randint(0,4)#利用randint方法产生0-4之间的随机整数
print("请输入你的选择：")
name=input()
def name_to_num(name):#将玩家输入的字符串转化为数字
	if name=="石头":
		return 0
	elif name=="史波克":
		return 1
	elif name=="布":
		return 2
	elif name=="蜥蜴":
		return 3
	elif name=="剪刀":
		return 4
	else:
		print("Error: No Correct Name")

def answer_to_name(answer):#将其随机输入的数字转化为字符串
	if answer==0:
		return ("石头")
	elif answer==1:
		return ("史波克")
	elif answer==2:
		return ("布")
	elif answer==3:
		return ("蜥蜴")
	elif answer==4:
		return ("剪刀")

fin=name_to_num(name)
com=answer_to_name(answer)
if fin==0 and (answer==4 or answer==3):
	print("您的选择为：石头")
	print("计算机的选择为：%s"%(com))
	print("您赢了！")
if fin==0 and (answer==2 or answer==1):
	print("您的选择为：石头")
	print("计算机的选择为：%s"%(com))
	print("您输了")
if fin==0 and answer==0:
	print("您的选择为：石头")
	print("计算机的选择为：%s"%(com))
	print("平局")
if fin==1 and (answer==4 or answer==0):
	print("您的选择为：史波克")
	print("计算机的选择为：%s"%(com))
	print("您赢了！")
if fin==1 and (answer==2 or answer==3):
	print("您的选择为：史波克")
	print("计算机的选择为：%s"%(com))
	print("您输了")
if fin==1 and answer==1:
	print("您的选择为：史波克")
	print("计算机的选择为：%s"%(com))
	print("平局")
if fin==2 and (answer==1 or answer==0):
	print("您的选择为：布")
	print("计算机的选择为：%s"%(com))
	print("您赢了！")
if fin==2 and (answer==3 or answer==4):
	print("您的选择为：布")
	print("计算机的选择为：%s"%(com))
	print("您输了")
if fin==2 and answer==2:
	print("您的选择为：布")
	print("计算机的选择为：%s"%(com))
	print("平局")
if fin==3 and (answer==1 or answer==2):
	print("您的选择为：蜥蜴")
	print("计算机的选择为：%s"%(com))
	print("您赢了！")
if fin==3 and (answer==4 or answer==0):
	print("您的选择为：蜥蜴")
	print("计算机的选择为：%s"%(com))
	print("您输了")
if fin==3 and answer==3:
	print("您的选择为：蜥蜴")
	print("计算机的选择为：%s"%(com))
	print("平局")
if fin==4 and (answer==3 or answer==2):
	print("您的选择为：剪刀")
	print("计算机的选择为：%s"%(com))
	print("您赢了！")
if fin==4 and (answer==1 or answer==0):
	print("您的选择为：剪刀")
	print("计算机的选择为：%s"%(com))
	print("您输了")
if fin==4 and answer==4:
	print("您的选择为：剪刀")
	print("计算机的选择为：%s"%(com))
	print("平局")
	
print("游戏结束")
