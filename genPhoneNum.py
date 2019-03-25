# -*- coding: utf-8 -*-

import random

#移动号段(不包含虚拟运营商及物联网卡，下同)
yd=['134','135','136','137','138','139','182','183','184','187','188','150','151','152','157','158','159','147','148','178','198']
#电信号段
dx=['133','153','180','181','189','191','199']
#联通号段
lt=['130','131','132','145','146','155','156','166','175','176','185','186']
#所有号段
all=yd+dx+lt
#生成手机号（参数为运运营商，默认为所有运营商）
def create_phone(tel):
    # 最后八位数字
    suffix = str(random.randint(9999999,100000000))
    # 拼接手机号
    phone=""
    if tel=='yd':
        phone= random.choice(yd)+suffix
    elif tel=='dx':
        phone=random.choice(dx)+suffix
    elif tel=='lt':
        phone=random.choice(lt)+suffix
    else:
        phone=random.choice(all)+suffix
    return phone

# 生成手机号
#参数nums 生成号码数量
#参数tel  运营商名称
def genPhoneNum(nums=10,tel='all'):
    file_abs="phonenum_"+tel+"_"+str(nums)+".txt"
    with open(file_abs,"w") as f:
        for i in range(nums):
            phone = create_phone(tel)
            f.write(phone+'\r')
if __name__=='__main__':
    genPhoneNum(1000000,'yd')
