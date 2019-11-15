#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：张健兴
日期：2019 11 15
"""

import random#调用random模块
number=random.randint(0,4)#利用randint方法产生0-4之间的随机整数
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

def answer_to_name(number):#将其随机输入的数字转化为字符串
	"""
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
	if number==0:
		return ("石头")
	elif number==1:
		return ("史波克")
	elif number==2:
		return ("布")
	elif number==3:
		return ("蜥蜴")
	elif number==4:
		return ("剪刀")

def rpsls(player_choice,number): # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
	"""
	用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

	"""
	if player_choice==0 and (number==4 or number==3):
		print("您的选择为：石头")
		print("计算机的选择为：%s"%(com))# 在屏幕上显示计算机选择的随机对象
		print("您赢了！")
	if player_choice==0 and (number==2 or number==1):
		print("您的选择为：石头")
		print("计算机的选择为：%s"%(com))
		print("您输了")
	if player_choice==0 and number==0:
		print("您的选择为：石头")
		print("计算机的选择为：%s"%(com))
		print("您和计算机出的一样呢")
	if player_choice==1 and (number==4 or number==0):
		print("您的选择为：史波克")
		print("计算机的选择为：%s"%(com))
		print("您赢了！")
	if player_choice==1 and (number==2 or number==3):
		print("您的选择为：史波克")
		print("计算机的选择为：%s"%(com))
		print("您输了")
	if player_choice==1 and number==1:
		print("您的选择为：史波克")
		print("计算机的选择为：%s"%(com))
		print("您和计算机出的一样呢")
	if player_choice==2 and (number==1 or number==0):
		print("您的选择为：布")
		print("计算机的选择为：%s"%(com))
		print("您赢了！")
	if player_choice==2 and (number==3 or number==4):
		print("您的选择为：布")
		print("计算机的选择为：%s"%(com))
		print("您输了")
	if player_choice==2 and number==2:
		print("您的选择为：布")
		print("计算机的选择为：%s"%(com))
		print("您和计算机出的一样呢")
	if player_choice==3 and (number==1 or number==2):
		print("您的选择为：蜥蜴")
		print("计算机的选择为：%s"%(com))
		print("您赢了！")
	if player_choice==3 and (number==4 or number==0):
		print("您的选择为：蜥蜴")
		print("计算机的选择为：%s"%(com))
		print("您输了")
	if player_choice==3 and number==3:
		print("您的选择为：蜥蜴")
		print("计算机的选择为：%s"%(com))
		print("您和计算机出的一样呢")
	if player_choice==4 and (number==3 or number==2):
		print("您的选择为：剪刀")
		print("计算机的选择为：%s"%(com))
		print("您赢了！")
	if player_choice==4 and (number==1 or number==0):
		print("您的选择为：剪刀")
		print("计算机的选择为：%s"%(com))
		print("您输了")
	if player_choice==4 and number==4:
		print("您的选择为：剪刀")
		print("计算机的选择为：%s"%(com))		
		print("您和计算机出的一样呢")
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择：")	# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
name=input()
player_choice=name_to_num(name)
com=answer_to_name(number)
print(rpsls(player_choice,number))
print("游戏结束")
