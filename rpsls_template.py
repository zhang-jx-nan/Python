#coding:gbk
"""
RPSLS��Ϸ
���ߣ��Ž���
2019 11 14
"""

import random#����randomģ��
answer=random.randint(0,4)#����randint��������0-4֮����������
print("���������ѡ��")
name=input()
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

def answer_to_name(answer):#����������������ת��Ϊ�ַ���
	if answer==0:
		return ("ʯͷ")
	elif answer==1:
		return ("ʷ����")
	elif answer==2:
		return ("��")
	elif answer==3:
		return ("����")
	elif answer==4:
		return ("����")

fin=name_to_num(name)
com=answer_to_name(answer)
if fin==0 and (answer==4 or answer==3):
	print("����ѡ��Ϊ��ʯͷ")
	print("�������ѡ��Ϊ��%s"%(com))
	print("��Ӯ�ˣ�")
if fin==0 and (answer==2 or answer==1):
	print("����ѡ��Ϊ��ʯͷ")
	print("�������ѡ��Ϊ��%s"%(com))
	print("������")
if fin==0 and answer==0:
	print("����ѡ��Ϊ��ʯͷ")
	print("�������ѡ��Ϊ��%s"%(com))
	print("ƽ��")
if fin==1 and (answer==4 or answer==0):
	print("����ѡ��Ϊ��ʷ����")
	print("�������ѡ��Ϊ��%s"%(com))
	print("��Ӯ�ˣ�")
if fin==1 and (answer==2 or answer==3):
	print("����ѡ��Ϊ��ʷ����")
	print("�������ѡ��Ϊ��%s"%(com))
	print("������")
if fin==1 and answer==1:
	print("����ѡ��Ϊ��ʷ����")
	print("�������ѡ��Ϊ��%s"%(com))
	print("ƽ��")
if fin==2 and (answer==1 or answer==0):
	print("����ѡ��Ϊ����")
	print("�������ѡ��Ϊ��%s"%(com))
	print("��Ӯ�ˣ�")
if fin==2 and (answer==3 or answer==4):
	print("����ѡ��Ϊ����")
	print("�������ѡ��Ϊ��%s"%(com))
	print("������")
if fin==2 and answer==2:
	print("����ѡ��Ϊ����")
	print("�������ѡ��Ϊ��%s"%(com))
	print("ƽ��")
if fin==3 and (answer==1 or answer==2):
	print("����ѡ��Ϊ������")
	print("�������ѡ��Ϊ��%s"%(com))
	print("��Ӯ�ˣ�")
if fin==3 and (answer==4 or answer==0):
	print("����ѡ��Ϊ������")
	print("�������ѡ��Ϊ��%s"%(com))
	print("������")
if fin==3 and answer==3:
	print("����ѡ��Ϊ������")
	print("�������ѡ��Ϊ��%s"%(com))
	print("ƽ��")
if fin==4 and (answer==3 or answer==2):
	print("����ѡ��Ϊ������")
	print("�������ѡ��Ϊ��%s"%(com))
	print("��Ӯ�ˣ�")
if fin==4 and (answer==1 or answer==0):
	print("����ѡ��Ϊ������")
	print("�������ѡ��Ϊ��%s"%(com))
	print("������")
if fin==4 and answer==4:
	print("����ѡ��Ϊ������")
	print("�������ѡ��Ϊ��%s"%(com))
	print("ƽ��")
	
print("��Ϸ����")
