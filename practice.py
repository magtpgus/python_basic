n = int(input())
han = 0
for i in range(1, n + 1):
    if i < 100:
        han += 1
    else:

        ns = list(str(i))
        print(ns)
        # if ns[0] - ns[1] == ns[1] - ns[2]:
        #     han += 1
print(han)


N = int(input())
mul = 1
for i in range(1,N+1):
    mul *=i
print(mul)


N = int(input())

A = []
B= []
for i in range(1, 10001):
    z = i//1000
    a= i //100
    b = i // 10
    c = i % 10
    e = i + b + c +a+z
    A.append(e)
    B.append(i)
C = set(A)
D = set(B)
E = list(D-C)
E.sort()
for i in E:
    print(i)

numbers = set(range(1, 10000))
remove_set = set()  # 생성자가 있는 숫자 set
for num in numbers :
    for n in str(num):
        num += int(n)
    remove_set.add(num)  # add: 집합에 요소를 추가할 때

self_numbers = numbers - remove_set  # set의 '-' 연산자로 차집합을 구함
for self_num in sorted(self_numbers):  # sorted 함수로 정렬
    print(self_num)

import sys
N =int(sys.stdin.readline())
for i in range(N):
    A ,B =map(int,sys.stdin.readline().split())
    print(A+B)
A =int(sys.stdin.readline())
B =int(sys.stdin.readline())
print(A+B)


N = int(input())
lst=[]
num = 0
for i in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key =lambda x:(x[1],x[0]) )
for i in lst:
    print(i[0],i[1])

N = int(input())
lst=[]
num = 0
for i in range(N+1):
    if len(lst)==0:
        num = 0
        lst.append(num)
    elif len(lst)==1:
        num = 1
        lst.append(num)
    else:
        num = lst[i-1]+lst[i-2]
        lst.append(num)
    #print(num)
print(num)
N = int(input())
lst =[]
for i in range(N):
    lst.append(input())
slst =list(set(lst))
slst.sort(key = lambda x:(len(x),x))
for i in slst:
    print(i)
lst.sort()
print(lst)
import sys
N = int(sys.stdin.readline())
A=[]
stack =[]
for i in range(N):
    A=sys.stdin.readline().strip().split()
    if A[0]=='push':
         stack.append(A[1])
    elif A[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif A[0] =='size':
        print(len(stack))
    elif A[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif A[0] =='top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
print(A)

N = int(input())
count = N

for _ in range(N):
    word = input()

    for i in range(len(word)-1):
        if word.find(word[i]) > word.find(word[i+1]): #앞에 있었다.!
            count -= 1
            break
print(count)


import sys
from collections import Counter
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
nums_s = Counter(nums).most_common()
print(round(sum(nums) / n))
print(nums[n // 2])
if nums_s[0][1] == nums_s[1][1]:
    print(nums_s[1][0])
else:
    print(nums_s[0][0])
print(nums[-1] - nums[0])


n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = [0,0]
arr.sort()
for i in set(arr):              #최빈값(빈도수) 체크
    if cnt[0] < arr.count(i):
        cnt[0] = arr.count(i)
        cnt[1] = i
        #이게 안되는 이유 : list.count는 시간복잡도 n, arr이 n개 일테니까 n^2이 된다다
print(int(round(sum(arr)/n,0))) # 소수점 첫째자리에서 반올림
print(arr[n//2])
print(cnt[1])
print(max(arr)-min(arr))


A = int(input())
B = input()
C = int(input())
D = list(input().split())
for i in D:
    if B.find(i)==-1:
        print(0)
    else:
        print(1)



A = int(input())
for i in range(A):
    B,C = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1, B,C,B+C))
A = int(input())
for i in range(A):
    k = int(input())
    n = int(input())
    people = [i for i in range(1,n+1)] # 1,2,3,4,...i
    for j in range(k): # 층
        for m in range(1,n): # 리스트 방 접근
            people[m]+= people[m-1] # 이전 방 수 더하기

        #내가원하는 층까지 반복
    print(people[-1])
A = int(input())
line =0
n =0 # 라인의 마지막 인덱스
while n < A:
    line +=1
    n += line
#print(line, n)
th = n -A
if line %2 ==0:
    top = line - th
    bot = th+1
else:
    top = th+1
    bot = line-th

print("%d/%d"%(top,bot))

import sys

A = int(sys.stdin.readline())
B =[]
for i in range(A):
    B.append(int(sys.stdin.readline()))
B.sort()
for i in B:
    print(i)



N = int(input())
count = N

for _ in range(N):
    word = input()

    for i in range(len(word)-1):
        if word.find(word[i]) > word.find(word[i+1]): #앞에 있었다.!
            count -= 1
            break
print(count)


A = ['c=','c-','dz=','d-','lj','nj','s=','z=']

B = input()
#print(B)
for i in A:
    B= B.replace(i,'@')
print(len(B))

A = int(input())
B =[]
for i in range(A):
    B.append(int(input()))
B.sort()
for i in B:
    print(i)


A = int(input())
cnt = 1
n =1 #방숫자
while n<A:
    n +=6*cnt
    cnt +=1
print(cnt)

A,B,V = map(int, input().split())
n = 0
while True:
    V -= A
    n+=1
    if V <=0:
        break
    V +=B
print(n)


num_list = []



A = int(input())
B =[]
for i in range(A):
    B.append(int(input()))
B.sort()
for i in B:
    print(i)



A,B = map(int, input().split())

n =[]
#for i in range(A,B+1):
n = [i for i in range(A,B+1) if i>4]
#for i in range(1,11):
print(n)
A = int(input())
print(A //5 + (A%5)//3)



asc = input()
print(ord(asc))

string = input()
#alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in alphabet:
#     print(string.find(i), end = ' ')
for i in range(97,123):
    print(string.find(chr(i)), end = ' ')


n = int(input())
for _ in range(n):
    B = list(input().split())
    #print(B)
    N = int(B[0])
    #print(type(B[1]))
    A = list(B[-1])
    #print(A)
    for i in A:
        print(i*N, end='')
    print()


num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else :
    print(num2)

A = int(input())
B = list(map(int,input()))
print(sum(B))

A = list(input().upper())
print(A)
B = list(set(A))
cnt = []
for i in B:
    cnt.append(A.count(i))

if cnt.count(max(cnt))>1:
    print('?')
else:
    print(B[cnt.index(max(cnt))])

A = int(input())
for i in range(A):
    B = list(map(str, input()))
    print(B)


B = list(map(str, input().split()))
print(len(B))

A = int(input())
B = list(map(int, input().split()))

max = max(B)
sum =0
for i in B:
    sum+=i/max*100
print(sum/A)

B=[]
for i in range(10):
    B.append(int(input())%42)

A = set()
A = set(B)
print(len(A))


B = B
print(B)
A = int(input())
B = int(input())
C = int(input())

result = list(str(A*B*C))
for i in range(10):
    print(result.count(str(i)))

B=[]
for i in range(9):
    B.append(int(input()))

print(max(B))
print(B.index(max(B))+1)


while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
lst = []
for i in range(A):
    B = list(map(int, input().split()))
    lst.append(B)
for idx, content in enumerate(lst):
    print("Case #{}: {}".format(idx+1, content[0] + content[1]))

A= int(input())

for i in range(A+1,1,-1):
    print(i)

get  = int(input())
A = get
cnt=0
while True:
    N= A%10+int(A/10)

    S = (A%10)*10+(N%10) #새로만든수 오른쪽 끝
    cnt+=1
    A = S
    if S==get:
        break

print(cnt)

A  = int(input())

sum = 0
for i in range(1,A+1):
    sum+=i
print(sum)

A,B = map(int,input().split())
numbers = list(map(int, input().split()))
num = [number for number in numbers]
print(num)

A= int(input())

for i in range(1,A+1):
    print('*'*i.rjust(A))

A, B = (1,1)
print(A, B)
while A!=0 and B!=0:
    A, B = map(int,input().split())
    print(A+B)


A= int(input())

for i in range(A):
    A, B = map(int,input().split())
    print(A+B)

A= int(input())
B=[4]
B = map(int,input().split())
print(B)

A= int(input())

for i in range(1,10):
    print("{0}*{1}={2}".format(A,i,A*i))

A, B = map(int,input().split())

H = A%24
M = B%60

if M < 45 :	# 분단위가 45분보다 작을 때
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1
        M += 60

print(H, M-45)
if M-45 <0:
    H-=1
    M=M-45+60
    if H-1<0:
        H=23
else:
    M-=45
print(H,M)


A = int(input())

if (A%4 ==0 and A%100!=0) or A%400==0:
    print(1)
else:
    print(0)

A, B = map(int,input().split())

if A>B:
    print(">")
elif B>A:
    print("<")
else:
    print("==")

##################

print(5>10)
print('z'*10)

sentence = "나는 소년이고" \
           "파이썬은 쉬워요"
sentence2 = """나는 소년이고 
파이썬은 쉬워요"""
print(sentence2)

dog = '''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\__|'''
print(dog)

print("나는 %d 살 입니다."%20)

subway = ["유재석","조세호","박명수"]
print(subway.index('유재석'))

t = (1,2,3,4)
print(type(t))

v = (1,"korea",3.5)
print(type(v))

tuple([1,2,3,4,5])
print(tuple([1,2,3,4,5]))

print("{:1>10}".format(500))

# A = int(input())
# B = int(input())
# print(A+B)
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

#(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

#(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

A = int(input())
B = input()
print(A*int(B[-1]))
print(A*int(B[-2]))
print(A*int(B[-3]))
print(A*int(B))