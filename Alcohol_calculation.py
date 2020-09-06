# 测试酒精质量和剂量

# 计算身体水含量
def TotalBodyWater(gender, age, height, weight):
    if gender == 'M':
        tbw = 2.117 - 0.09516 * age + 0.1074 * height + 0.3362 * weight
    elif gender == 'F':
        tbw = -2.097 + 0.1069 * height + 0.2466 * weight
    return tbw 

# 计算酒精质量
def alcohol_kg(bal, tbw, ddp, mr=0.015, tpb=0.5):
    '''
    input:
        BAL-Blood-Alcohol Level: 目标血液中酒精浓度 g/100ml
        TBW-Total Body Water: 身体含水量
        MR-Metabolism Rate: 代谢率，一般定为0.015g/100ml/hr
        DDP-Duration of the Drinking Period: 喝酒时间
        TPB-Time to Peak BAL: 到达BAL的时间，常设为0.5hr
    output:
        g-gram: 酒精质量
    formula:
        酒精剂量(g) = [(10 x BAL x TBW) / 0.8] + 10 x MR x (DDP + TPB) x (TBW / 0.8)
    '''
    ddp = ddp / 60
    return ((10 * bal * tbw)/0.8) + 10 * mr * (ddp + tpb) * (tbw / 0.8)

# 计算饮酒剂量
def alcohol_ml(aq, ac):
    '''
    input:
        AQ-Alcohol Quality: 酒精质量
        AC-Alcohol Concetration: 酒精浓度
    output:
        ml-milliliter: 酒精毫升
    '''
    return aq / 0.8 / (ac / 100)


if __name__ == "__main__":
    print("友情提示：***请确定饮用酒的密度，及时更改程序中的密度值***")
    sublist = list(input("请分别输入年龄，身高(cm)，体重(kg)，空格分隔：").split())
    age, height, weight = [float(sublist[i]) for i in range(len(sublist))]
    gender = input("输入性别(男性为M，女性为F): ")
    sublist2 = list(input("输入目标血液酒精浓度BAL(g/100ml)和饮酒时间DDP(minutes)，空格分隔：").split())
    bal, ddp = [float(sublist2[i]) for i in range(len(sublist2))]
    ac = int(input("请输入酒精浓度值："))

    tbw = TotalBodyWater(gender, age, height, weight)
    aq = alcohol_kg(bal, tbw, ddp)
    ml = alcohol_ml(aq, ac)
    print("当前被试的饮酒质量为：%.2f g" % aq)
    print("当前被试的饮酒剂量为：%.2f ml" % ml)


