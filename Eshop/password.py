# email a@gmail.com
# password Nitin

# email bb@gmail.com
#password Nitin


# # Start=[2,4,1,6,6]
# # End=[3,5,6,8,10]
# # n=0
# # for i in range(len(Start)-1):
# #     if End[i]<Start[i+1]:
# #         n+=2
# # print(n)


# # def findEvenNumbers(digits) :
# #         l=[]
# #         # for i in range():
# #         n=str(288)
# #         m=0
# #         for j in range(len(n)):
# #             if n[j] in digits:
# #                 m=+1
# #                 print(m)
# #             if m==3:
# #                 l.append(n)
# #         return l
# # digits=[2,2,8,8,2]
# # print(findEvenNumbers(digits))

# # def dividetoZero(num):
# #     m=0
# #     for i in range(len(num)):
# #         if len(num)%2!=0:
# #             n=len(num)-1
# #         else:
# #             n=len(num)
# #         n=n-n/2
# #         m+=1
# #         if n==0:
# #            break
# #     return m

# # num='1458'
# # print(dividetoZero(num))
# from collections import Counter
# m=[1,2,2,1,2,3]
# print(Counter(m))

# def intersect( nums1, nums2):
#         inter_counter = Counter(nums1) & Counter(nums2)
#         print(Counter(nums1))
#         print(Counter(nums2))
#         print(inter_counter)
#         inters = []
#         for x in inter_counter:
#             for y in range(inter_counter[x]):
#                 inters.append(x)
#         return inters

# nums1=[1,2,2,1]
# nums2=[2]
# print(intersect(nums1,nums2))

# if 'b' in "bella":
#     print('HH')

import collections


# # lis = collections.deque()
# l='abcdefd'
# listt = list(l)
# lis=[]
# li=[]
# ch='d'
# for i in range(len(listt)):
#     if listt[i]==ch:
#         lis=listt[i::-1]
#         print(lis)
#         for j in range(len(listt)):
#             if j<len(lis):
#                  li.append(lis[j])
#             else:
#                 li.append(listt[j])
#         break


# print(''.join(li))
# w=['3','5','4','2','7']
# w='35427'
# w='1234'
# def nn(num):
#      if not num:
#         return num

#      i = len(num) - 1
#      while i >= 0:
#         if int(num[i]) % 2 != 0:
#             break
#         i -= 1

#      return num[: i+1]
# print(nn(w))

# n1=100
# n2=200
# l=[i for i in range(n1,n2+1)]
# # print(l)
# n=0
# for i in l:
#    s=set(str(i))
#    ll=list(str(i))
#    if len(s)==len(ll):
#       n+=1

# print(n)


# def find(N):
#     l = []
#     flag = 0
#     while(N>0):
#         l.append(N%10)
#         N = N//10
#     #print(l)
#     for i in l:
#         if l.count(i)>1:
#             flag = 1
#             break
#     return flag

# start, end = list(map(int,input().split()))
# count = 0
# for i in range(start,end+1):
#     t = find(i)
#     if t == 0:
#         count += 1
# print(count)


# class Solution:
#     def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
#         d=(sum(A)-sum(B))//2 ; A=set(A) ; B=set(B)
#         return [[x, x-d] for x in A if x-d in B][0]
# Another Solution
# def fair(A,B):
#     d=(sum(A)-sum(B))//2 ; A=set(A) ; B=set(B)
#     for x in A:
#         if x-d in B:
#             return [x,x-d]
# print(fair([1,2],[2,3]))
# l=[]
# def search(num,t):
#     for i in range(len(num)):
#         if t==num[i]:
#             l.append(i)
# search([3,3,3],3)
# print(l)
# l=collections.Counter()
# print(l)
# def findJudge(n, trust):
#         trustCount = collections.Counter()
#         trustedCount = collections.Counter()

#         for a, b in trust:
#             trustCount[a] += 1
#             trustedCount[b] += 1
#         print(trustCount)


#         print(trustedCount)
#         for i in range(1, n+1):
#             if trustCount[i] == 0 and trustedCount[i] == n - 1:
#                 return i

#         return -1
# findJudge(3,[[1,3],[2,3],[3,1]])
# print('Helo')

# def makeGood(s):
#         #Self done
#     stack = []
#     for i in s:
#         if len(stack)==0:
#             stack.append(i)
#             continue
#         if stack[-1]==i.swapcase():
#             stack.pop()
#         else:
#             stack.append(i)
#     print("".join(stack))
#     # return "".join(stack)
# # makeGood('aBbAcC')
# print(makeGood("aBbAcC"))
# x = '021'
# print(abs(-21))
# l = ['0','0', '1']
# n=0
# while(n<len(l)):
#     if int(l[n])==0:
#         l.remove(l[n])
#     elif int(l[n])>0:
#         break
#     n+=1
# print(l)
# l = ['0','0', '1']
# n=0
# while(n<len(l)):
#     if int(l[n])==0:
#         l.remove(l[n])
#     elif int(l[n])>0:
#         break
# print(l)

# print(int('-23'))
     
# def clamp(num, min_value, max_value):
#    return max(min(num, max_value), min_value)
# print(clamp(-91283472332, -2**31, 2**31-1))



# def findAndReplacePattern( w, p):
#    lp=len(p)
#    ans,l=[],[]
#    d={}
#    for i in p:
#       if i in d:
#          d[i]+=1
#       else:
#          d[i]=1
#          l.append(d[i])
#       print(d)
#       for i in w:
#          f,k={},[]
#          for j in i:
#             if j in f:
#                f[j]+=1
#             else:
#                f[j]=1
#             k.append(f[j])
#          print(k)
            
#          if l==k:
#             flag=True
#             for j in range(lp):
#                if d[p[j]]!=f[i[j]]:
#                   flag=False
#                   break
#                if flag:
#                   ans.append(i)
#    return ans
# findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb")
# print(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb"))

# print('00000000000000000000000000001011')
# print(ord('A'))
# print(ord('G')-ord("A"))

# def small_digit(n):
#     l=[]
#     for i in range(1,n):
#         if n%i==0:
#             l.append([(n//i),i])
#     return l
# print(small_digit(556))


# def funn(a,b):
#     x=0
#     while(x<=b):
#         x+=a
#         print(x)
#         if (x==b):
#             return print("Possible")
#     return print("nnPossible")
# funn(4,16)
# print(funn(4,17))
# nums=[2,2,3,4]
# for i in range(len(nums)-1, 1,-1): 
#     print(nums[i],i)
# 			# fix = nums[i] # Fix a number
# 			# strt = 0
# 			# end = i-1

# def findPairs(nums,k):
#     h, c, result = {}, set(), 0
        
#     for i in range(len(nums)):
#         s = nums[i] + k
#         if s not in h:
#             h[s] = i
# 	# print(h)
	   
#     for i in range(len(nums)):
#         if nums[i] in h and h[nums[i]] != i:    
#             c.add(nums[i])
#             result += 1
	
# 	# print(result)        
#     return c
# print(findPairs([3,1,4,1,5],2))

# def printNGE(arr):
#     l=[]
#     for i in range(0, len(arr), 1):
  
#         next = -1
#         for j in range(i+1, len(arr), 1):
#             if arr[i] < arr[j]:
#                 next = arr[j]
#                 break
              
#         # print(str(arr[i]) + " -- " + str(next))
#         l.append(next)
#     print(l)
  
# # Driver program to test above function
# arr = [11,13,21,3]
# printNGE(arr)
# print(2>2)

# class Node():
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class ll():
#     def __init__(self):
#         self.head=None

#     def printall(self):
#         if self.head is None :
#             return -1
#         while self.head :
#             print(self.head.data)
#             self.head=self.head.next
    
#     def insert_at_first(self,val):
#         vall=Node(val)
#         vall.next=self.head
#         self.head=vall
    
#     def insert_after_a_node(self,nod,val):
#         vall=Node(val)
#         temp=self.head
#         while temp.data!=nod:
#             temp=temp.next
#         vall.next=temp.next
#         temp.next=vall
#     def insert_at_last(self,val):
#         vall=Node(val)
#         if self.head is None :
#             return -1
#         temp=self.head
#         while temp.next :
#             temp=temp.next
#         temp.next=vall

#     def delet_node(self,val):
#         temp=self.head
#         while temp:
#             if temp.next.data==val:
#                 break
#             temp=temp.next
#         temp.next=temp.next.next
        


# hd=ll()
# first=Node(10)
# hd.head=first
# second=Node(20)
# first.next=second
# third=Node(30)
# second.next=third
# # print(first.next.data)
# hd.insert_at_first(1000)
# hd.insert_at_first(120)
# hd.insert_at_last(100000)
# hd.insert_after_a_node(10,30000)
# hd.insert_after_a_node(10,800)
# hd.delet_node(30)
# hd.printall()
# hd.insert_at_last(2000)

# hd.printall()

# s="234 44 thr"
# n = len(s)
# for i in range(n):
#     if s[i] != " ":
#         print(i)
#         s = s[i:]
#         print(s)
#         break
# print(s)

# print(111%83)