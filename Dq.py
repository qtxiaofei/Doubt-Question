#
'''
Question: 01
Title: 
Disctibution:
    
Input: 

Output:  

Case:
    input:
    output:
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

Case:
    input: 3<CR> -1 -1 -1<CR> 3<CR> -1 -1 1<CR> 3<CR> 1 -1 2<CR> 7<CR> -1 -1 -1 4 5 1 2<CR>
    output: 1<CR> 1<CR> 2<CR> 2<CR>
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


'''
Question: 03
Title: 等差数列 
Disctibution: 长度为n的数列a，可以对数列中每个元素最多增加或者减少1，也可以不操作。
    当前任务是需要知道最少改变了多少元素，使数列a是一个等差数列，若无法让a变成等差数列，则输出-1
    
Input: 第一行，一个正整数T(1<=T<=50)，代表测试数据组数；
    对于每组数据，第一行，一个正整数n(1<=n<=20000);第二行n个正整数，a1,a2,...,an(1<=ai<=10^9)
    数据保证sum(n)<=20000

Output: 输出一行一个整数，代表最少要改变多少个元素，使得数列a为一个等差数列；否则输出-1

Case:
    input: 1<CR> 4<CR> 1 5 6 7<CR>
    output: 3

Doubt: 应该把坐标0单独处理，后面的依次处理；这样比最后一个单独处理要快一些；
    其次，程序也没有考虑到输出-1的情况，主函数的输入程序部分也不完善
'''
def calavg(numlist):
    sum = 0
    for i in range(len(numlist)-1):
        sub = numlist[i+1] - numlist[i]
        sum = sum + sub

    return sum // (len(numlist)-1)

def handle(numlist, num):
    counter = 0
    for i in range(len(numlist)-1):
        if (numlist[i+1] - numlist[i]) != num:
            if (numlist[i] - num) > numlist[i-1] and i > 0:
                numlist[i] -= 1
                counter += 1

            if (numlist[i] + num) < numlist[i+1]:
                numlist[i] += 1
                counter += 1
        else:
            continue
    if (numlist[len(numlist)-1] - num) > numlist[len(numlist)-2]:
        numlist[len(numlist)-1] -= 1
        counter += 1
    elif (numlist[len(numlist)-1] - num) < numlist[len(numlist)-2]:
        numlist[len(numlist)-1] += 1
        counter += 1

    return counter

# if __name__ == "__main__":
#     n = int(input())
#     for i in range(n):
#         m = int(input())
#         numlist = []
#         for j in range(m):
#             numlist.append()

if __name__ == "__main__":
    numlist = [1, 5, 6, 7]
    num = calavg(numlist)
    print(handle(numlist, num))



'''
Question: 04
Title: 询问最短路径
Disctibution: n个城市，编号为1到n，现在地图上有m条双向路径。询问两个城市，问最短路径是多少？询问次数过多，完成此任务
    
Input: 
    输入第一行三个整数n,m,q, 代表n个城市，m个双向路径，q次询问
    接下来m行，每一行输入三个数x,y,l, 代表从x到y有一条距离为l的双向路径
    接下来输入q行，每一行输入两个数a和b，代表询问的两个城市
Output:  
    对每组测试程序，输出一个答案代表查询的是最短路径；若不存在输出为-1
Case:
    input: 5 3 3<CR> 1 2 1<CR> 2 3 1<CR> 3 5 2<CR> 1 2<CR> 2 4<CR> 1 5<CR>
    output: 1<CR> -1<CR> 4<CR>
Doubt: 结果不正确，在startpoint和endpoint，以及a和b这几个参数跟原来的程序不同，需要解决下这里面的问题是什么
'''

def BuildGraph_Matrix(Graph_Matrix, Path_Cost):
	for i in range(1,n):
		for j in range(1,n):
			if i==j:
				Graph_Matrix[i][j]=0
			else:
				Graph_Matrix[i][j]=INF

	i=0
	while i<len(Path_Cost):
		Start_Point=Path_Cost[i][0]-1
		End_Point=Path_Cost[i][1]-1
		Graph_Matrix[Start_Point][End_Point]=Path_Cost[i][2]
		i+=1


def Floyd(Graph_Matrix, distance, vertex_total,INF=999): 
	for i in range(1,vertex_total+1):
		for j in range(i,vertex_total+1):
			distance[i][j]=Graph_Matrix[i][j]
			distance[j][i]=Graph_Matrix[i][j]

	for k in range(1,vertex_total+1):
		for i in range(1,vertex_total+1):
			for j in range(1,vertex_total+1):
				if distance[i][k]+distance[k][j]<distance[i][j]:
					distance[i][j]=distance[i][k]+distance[k][j]


if __name__ == "__main__":
    res=list(input("1:").split())
    n,m,q=[int(res[i]) for i in range(len(res))]
    NUMBER=n-1
    INF=999

    Graph_Matrix=[[0]*n for row in range(n)]
    distance=[[0]*n for row in range(n)]

    Path_Cost = []
    for i in range(m):
       sublist = list(input("2:").split())
       sublist = [int(sublist[i]) for i in range(len(sublist))]
       Path_Cost.append(sublist)

    BuildGraph_Matrix(Graph_Matrix, Path_Cost)
    Floyd(Graph_Matrix, distance, NUMBER)

    for i in range(q):
        sublist2 = list(input("3:").split())
        a, b = [int(sublist2[i]) for i in range(len(sublist2))]
        print(distance[a-1][b-1])
        
