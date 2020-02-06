# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:06:29 2020

@author: soug9
"""

########## 타겟 넘버 ##########

'''
DFS로 모든 순회를 돈다
재귀 함수를 사용하는 피보나치 수열과 비교할 때, 피보나치 수열은 f(n)에서 f(n-1), f(n-2)을 부르는데,
타겟 넘버는 f(n)에서 f(n+1)을 부른다. (?)
'''

def solution(numbers, target) :
    answer = 0
    
    def dfs(n) :
        if n < len(numbers) :
            
            dfs(n+1)
            
            numbers[n] *= -1
            dfs(n+1)
        
        else : # 종료 조건 : depth 만큼 탐색 후
            if sum(numbers) == target :
                nonlocal answer
                answer += 1
       
    dfs(0)
    
    return answer
        
        

numbers, target = [5, 3, 1, 1, 1, 1, 1, 1], 2 #27
numbers, target = [1, 1, 1, 1, 1, 2, 2], 3 # 20
solution(numbers, target)



'''
첫번 째로 짠 코드(아래)는 왜 느린지 궁금하다
'''
def solution(numbers, target):
    answer = 0

    from itertools import permutations
    
    for n in range(len(numbers)+1) :
        for l in set(permutations([-1]*n + [1]*(len(numbers)-n), len(numbers))) :
            if sum([i*j for i, j in zip(l, numbers)]) == target :
                answer += 1

    return answer



########## 카펫 ##########
    
'''
* 변수
x = 가로 길이
y = 세로 길이
b = brown 개수
r = red 개수

* 기본 조건
x>=3, y>=3, x>=y

* 도출 식
(1) x*y = r+b
(2) (x-2) * (y-2) = r   
(1)과 (2)를 통해 (3) x+y = (b+4)/2 도출
'''

def solution(brown, red):
    answer = []

    multiply = brown + red
    _sum = int((brown+4)/2)
    
    factors = [i for i in range(int(multiply/2), 2, -1) if multiply % i == 0]
        
    for f in factors :
        x = f
        y = int(multiply/f)
    
        if x>=3 and y>=3 and x>=y :
            if x+y == _sum :
                answer = [x, y]
                break

    return answer


brown, red = 10, 2 # [4, 3]
brown, red = 8, 1	# [3, 3]
brown, red = 24, 24 # [8, 6]

solution(brown, red)



########## 라면공장 ##########

'''
* 문제 접근
1. 재고량이 떨어지는 당일(=stock 일 째) 보다 일찍 공급 받아야 한다.
2. 공급 횟수를 최소화 하려면 회당 최대 개수를 공급 받아야 한다.
=> stock과 같거나 작은 날짜의 supplies를 최댓값부터 내림차순으로 공급 받는다. 

* 구현
heapq -> max heap 응용
list, heapq를 사용했지만, deque를 사용해도 괜찮았을 듯!

*
1. list에서 pop()을 사용하기 위해 dates 기준 내림차순으로 정렬
2. stock이 k보다 크거나 같으면 공급 받을 필요가 없다
3. dates 중 재고량이 떨어지는 당일(=stock일 째) 또는 그보다 빠른 날짜라면, heap에 supplies를 넣어줌
4. max heap 구현
5. heap내에 최댓값을 더하여(=공급받아서) stock 증가

'''
    

def solution(stock, dates, supplies, k):
    answer = 0
    
    import heapq
    
    # 1
    dates.reverse()
    supplies.reverse()
    
    h = list()
    
    while stock < k : # 2
        while dates[-1] <= stock and len(dates) > 0 : # 3
            dates.pop()
            s = supplies.pop()
            heapq.heappush(h, (-s, s)) # 4
        
        # 5
        stock += heapq.heappop(h)[1]
        answer += 1
    
    return answer


stock, dates, supplies, k = 4, [1,2,3,4], [1,1,1,3], 8   # 2

solution(stock, dates, supplies, k)
    






########## 타일 장식물 ##########
def solution(N):
    answer = 0

    f = [1, 1] + [-1]*(N-1)
    
    for n in range(2, N+1) :
        f[n] = f[n-1] + f[n-2]
        
    answer = 2*(f[N] + f[N-1])
    
    return answer

N = 1 #4 
N = 5 #26

solution(N)


########## 자물쇠와 열쇠 ##########

'''
* 주의
- 깊은 복사와 얕은 복사
- function의 parameter를 변경해서 리턴하면 parameter로 할당된 원래 변수도 변경됨
- MOVE 하더라도 본래의 배열을 보관해야 함

* inner function
extendLock(lock) : N x N의 lock 배열을 S x S로 확장시키는 함수, N x N의 lock 배열은 정중앙에 위치해있고, 나머지는 0으로 채움 
rotate(key) : key 배열을 시계 방향으로 90도 회전시키는 함수
extendKey(key) : M x M의 key 배열을 S x S로 확장시키는 함수, M x M의 key 배열은 0~M 위치해있고, 나머지는 0으로 채움
moveToRight(key) : S x S 의 key 배열에서 M x M의 key 배열만 오른쪽으로 한 칸 이동하는 함수
moveToDown(key) : S x S 의 key 배열에서 M x M의 key 배열만 아래쪽으로 한 칸 이동하는 함수
tryToOpen(key, lock) : S x S 의 key로 S x S 의 lock을 열 수 있으면 True 리턴

* tryToOpen(key, lock) 의 True 조건
S x S 의 key와 S x S의 lock의 각 요소를 더한 배열 result 에 
1) result의 정중앙 N x N에 모두 1이 채워졌을 때
'''

def solution(key, lock):
    
    N = len(lock)
    M = len(key)
    S = 2*M + N -2 # size of extended key
    
    def extendLock(lock) :
    
        topNbottom = [[0]*S]*(M-1)
        leftNright = [[0]*(M-1)]*N
        
        extd_lock = list()
        for l, lr in zip(lock, leftNright) :
            extd_lock.append(lr + l + lr)
            
        extd_lock = topNbottom + extd_lock + topNbottom
        
        return extd_lock
    
    import copy
    
    def rotate(key) :
        copyk = copy.deepcopy(key)
        
        for i in range(M) :
            for j in range(M) :
                copyk[i][j] = key[M-j-1][i]
                
        return copyk
    
    def extendKey(key) :
        
        right = [[0]*(S-M)]*M
        bottom = [[0]*S]*(S-M)
        
        extd_key = list()
        for k, r in zip(key, right) :
            extd_key.append(k+r)
            
        extd_key += bottom    
        
        return extd_key
    

    def moveToRight(key) :
        
        copyk = copy.deepcopy(key)
        
        for i in range(S) :
            for j in range(S) :
                copyk[i][j] = key[i][j-1] if j != 0 else 0
                
        return copyk
    
    def moveToDown(key) :
        
        copyk = copy.deepcopy(key)

        for i in range(S) :
            copyk[i] = key[i-1] if i != 0 else [0]*S
                
        return copyk
    
    
    def tryToOpen(key, lock) :
        
        open_ = [[1]*N]*N
        
        result = list()
        
        for i in range(S) :
            temp = list()
            for j in range(S) :
                 temp.append(key[i][j] + lock[i][j])
            result.append(temp)
             
#        print('key')
#        print2d(key)
#        
#        print('result')        
#        print2d(result) 
                
        if [r[M-1:M-1+N] for r in result[M-1:M-1+N]] == open_ :
            return True
        else :
            return False
        
#    def print2d(d) :
#        for line in d :
#            print(line)
#        print()
        
    # end of inner function
    
    extd_lock = extendLock(lock)
#    print2d(extd_lock)
    
    for i in range(4) :
        key = rotate(key)
        extd_key = extendKey(key)
        extd_key_r = copy.deepcopy(extd_key)

        for j in range(N+M-1) :
            extd_key_r = moveToRight(extd_key_r) if j != 0 else copy.deepcopy(extd_key_r)
            extd_key_d = copy.deepcopy(extd_key_r)

            for k in range(N+M-1) :
                extd_key_d = moveToDown(extd_key_d) if k != 0 else copy.deepcopy(extd_key_d)
                
#                print(tryToOpen(extd_key_d, extd_lock))
                
                if tryToOpen(extd_key_d, extd_lock) :
                    return True
                
    return False
                          
key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]] # true
solution(key, lock)




########## 숫자 야구 ##########

def solution(baseball):
    
    def checkStrike(num, b, strike) :
        for i in range(3) :
            if num[i] == b[i] : strike -= 1
            
        if strike == 0 :
            return True
        
        return False
        
    def checkBall(num, b, ball) :
        for i in range(3) :
            if num[i] in b : ball -= 1
            
        if ball == 0 :
            return True
        
        return False
     
    # end of inner function
    
    nums = list()
    for i in range(1,10) :
        for j in range(1,10) :
            for k in range(1,10) :
                if i==j or j==k or i==k : continue
                nums.append(str(i*100 + j*10 +k))
     
    answer = len(nums)           
    
    for num in nums :
        for b in baseball :
            if checkBall(num, str(b[0]), b[1]+b[2]) and checkStrike(num, str(b[0]), b[1]) :
                pass
            else :
                answer -= 1
                break
    
    return answer


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]   # 2
solution(baseball)

















