#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��Ž���
���ڣ�2019 11 15
"""

import random#����randomģ��
number=random.randint(0,4)#����randint��������0-4֮����������
def name_to_num(name):#�����������ַ���ת��Ϊ����
	if name=="ʯͷ":
		return 0
	elif name=="ʷ����":
		return 1
	elif name=="��":
		return 2
	elif name=="����":
		return 3
	elif name=="����":
		return 4
	else:
		print("Error: No Correct Name")

def answer_to_name(number):#����������������ת��Ϊ�ַ���
	"""
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
	if number==0:
		return ("ʯͷ")
	elif number==1:
		return ("ʷ����")
	elif number==2:
		return ("��")
	elif number==3:
		return ("����")
	elif number==4:
		return ("����")

def rpsls(player_choice,number): # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

	"""
	if player_choice==0 and (number==4 or number==3):
		print("����ѡ��Ϊ��ʯͷ")
		print("�������ѡ��Ϊ��%s"%(com))# ����Ļ����ʾ�����ѡ����������
		print("��Ӯ�ˣ�")
	if player_choice==0 and (number==2 or number==1):
		print("����ѡ��Ϊ��ʯͷ")
		print("�������ѡ��Ϊ��%s"%(com))
		print("������")
	if player_choice==0 and number==0:
		print("����ѡ��Ϊ��ʯͷ")
		print("�������ѡ��Ϊ��%s"%(com))
		print("���ͼ��������һ����")
	if player_choice==1 and (number==4 or number==0):
		print("����ѡ��Ϊ��ʷ����")
		print("�������ѡ��Ϊ��%s"%(com))
		print("��Ӯ�ˣ�")
	if player_choice==1 and (number==2 or number==3):
		print("����ѡ��Ϊ��ʷ����")
		print("�������ѡ��Ϊ��%s"%(com))
		print("������")
	if player_choice==1 and number==1:
		print("����ѡ��Ϊ��ʷ����")
		print("�������ѡ��Ϊ��%s"%(com))
		print("���ͼ��������һ����")
	if player_choice==2 and (number==1 or number==0):
		print("����ѡ��Ϊ����")
		print("�������ѡ��Ϊ��%s"%(com))
		print("��Ӯ�ˣ�")
	if player_choice==2 and (number==3 or number==4):
		print("����ѡ��Ϊ����")
		print("�������ѡ��Ϊ��%s"%(com))
		print("������")
	if player_choice==2 and number==2:
		print("����ѡ��Ϊ����")
		print("�������ѡ��Ϊ��%s"%(com))
		print("���ͼ��������һ����")
	if player_choice==3 and (number==1 or number==2):
		print("����ѡ��Ϊ������")
		print("�������ѡ��Ϊ��%s"%(com))
		print("��Ӯ�ˣ�")
	if player_choice==3 and (number==4 or number==0):
		print("����ѡ��Ϊ������")
		print("�������ѡ��Ϊ��%s"%(com))
		print("������")
	if player_choice==3 and number==3:
		print("����ѡ��Ϊ������")
		print("�������ѡ��Ϊ��%s"%(com))
		print("���ͼ��������һ����")
	if player_choice==4 and (number==3 or number==2):
		print("����ѡ��Ϊ������")
		print("�������ѡ��Ϊ��%s"%(com))
		print("��Ӯ�ˣ�")
	if player_choice==4 and (number==1 or number==0):
		print("����ѡ��Ϊ������")
		print("�������ѡ��Ϊ��%s"%(com))
		print("������")
	if player_choice==4 and number==4:
		print("����ѡ��Ϊ������")
		print("�������ѡ��Ϊ��%s"%(com))		
		print("���ͼ��������һ����")
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��")	# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
name=input()
player_choice=name_to_num(name)
com=answer_to_name(number)
print(rpsls(player_choice,number))
print("��Ϸ����")
