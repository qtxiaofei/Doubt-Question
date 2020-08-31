#
'''
Question: 01
Title: 
Disctibution:
    
Input: 

input:  

Doubt: 
'''


'''
Question: 01
Title: 分割序列 
Disctibution: 现有一序列，长度为n，所有元素均为整数元素。序列中一些元素是确定值，另一些为不确定的。
    该任务为将所有不确定的元素赋予一个正整数值，使得整个序列分割最少的段，每一个段都是一个等差数列。
    特别地，长度为1和2的段都是等差数列
    
Input: 输入多组数据，每组数据第一行包含一个整数n，接下来一行为n个整数，空格隔开。
    如果数为-1，则代表该元素不确定，否则该元素为确定值
input: 输出一行一个数，代表分割后最少的段数，使得每一段都是等差数列 

Doubt: 代码中的step和取余操作这部分不明白，整个程序流程也需要摸清楚 
'''
n = int(input())
a = list(map(int,input().split()))
i = 0
ans = 0
while i<n:
    ans+=1
    il = i
    while il<n and a[il] == -1:
        il+=1
    if il == n:
        break
    i2 = il+1
    while i2<n and a[i2] == -1:
        i2 += 1
    if i2 ==n:
         break
    dist = i2-il
    step =(a[i2] - a[il])//dist
    if (a[i2] - a[il])%dist !=0 or (step>0 and a[il]-(il-i)*step<=0):
        i = i2
        continue
    i3 = i2 +1
    while i3<n:
        nxt = a[i2] +step*(i3-i2)
        if nxt <=0 or (a[i3]!=-1 and a[i3] != nxt):
            break
    i3 += 1
    i = i3
print(ans)



'''
Question: 02
Title: 喜欢不一样的素数
Disctibution: 学完素数之后，小明喜欢上了2,3和5.当然，如果一个数字里只出现2，3和5三个数字，他也喜欢。如：222,2235,233355
    现在他希望能够编写一个程序，快速计算出由2,3和5这三个数字组成的由小到大的第n个数，当然包括2,3和5
Input: 单组输入。每行输入数据占1行，每行输入一个正整数n，n<=1000
Output: 每组输出数据占1行，即满足要求的第n个数

Case: 
    input:  3
    output: 5

Doubt: 为什么初始化序列为523便使得这个程序可以使用，暗含的规律是什么，3的i次方这个规律可以拓展到其他例子么，比如5个不同的数 
'''
def P1():
    n = int(input())
    n1 = ['5', '2', '3']
    num = ''
    i = 0
    while 3**i <= n:
        s = n % 3 **(i + 1)
        r = s // 3**i
        num += n1[r]
        n -= 3**i
        i += 1
        print(num[::-1])
