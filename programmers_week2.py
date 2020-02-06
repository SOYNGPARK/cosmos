# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:18:56 2020

@author: soug9
"""

########## 124 나라의 숫자 ##########

'''
301 = (3**1 + 3**2 + 3**3 + 3**4) + 2*(3**4) + 0*(3**3) + 2*(3**2) + 0*(3**1) + 1

1. n을 a=3, r=3인 등비수열의 합과 그 나머지로 표현
2. 나머지를 자연수 * (3**k)의 합과 그 나머지로 표현 :
    k = 1 ~ 등비수열의 항수, 나머지 < 3
3. (자연수+1)의 값들을 순서대로 이어붙임, 단 3은 4로 변경

'''

def solution(n):
    answer = ''
    
    import math
    
    # 1
    digit = 1
    sum_of_gp = 0
    
    while True :
        sum_of_gp += 3**digit
        if n <= sum_of_gp :
            sum_of_gp -= 3**digit
            digit -= 1
            break
        else :
            digit += 1
      
    # 2
    n = n - sum_of_gp
    
    numbers = list()

    if digit > 0 :
        numbers.append(math.ceil(n/3**digit))
        
        for d in range(digit-1,0,-1) :
            n = n - 3**(d+1)*(numbers[-1]-1)
            numbers.append(math.ceil(n/3**d))

    numbers.append(n%3)
    
    # 3
    numbers = ['4' if number == 3 or number == 0 else str(number) for number in numbers] 
    
    answer = ''.join(numbers)
    
    return answer

solution(301)



########## 큰 수 만들기 ##########
    
def solution(number, k):
    lst = list()
    
    for n in list(number) :
        while(len(lst) != 0 and lst[-1] < n and k != 0) :
            k -= 1
            lst.pop()
        lst.append(n)
        print(lst)
    
    # number가 내림차순으로 주어졌을 때 예외 처리
    if k != 0 :
        lst = lst[:(len(lst)-k)]
        
    answer = ''.join(lst)
    
    return answer


number, k = '1924', 2  # 94
number, k = '1231234', 3   # 3234
number, k = '4177252841', 4   # 775841
number, k = '987654321', 2
number, k = '775841', 1

solution(number, k)






########## 조이스틱 ##########

'''
1. 위/아래 조작 :
    알파벳 숫서로 된 리스트에서 해당 알파벳의 index값(위로 조작) 또는 (리스트 크기(=알파벳 갯수)-index 값)(아래로 조작) 중 작은 값
2. 왼/오른쪽 조작 :
    왼/오른쪽 끝에서 시작하는 A의 개수, 중간에 있는 A의 최대 개수 계산
    2-1. 오른쪽(뒤쪽)에서 시작하는 A의 개수가 가장 클 때 :
        오른쪽으로 조작
    2-2. 왼쪽(앞쪽)에서 시작하는 A의 개수가 가장 클 때 :
        왼쪽으로 조작
    2-3. 중간에 있는 A의 최대 개수가 가장 클 때 :
        2-3-1. 만약 '중간에 있는 A의 최대 개수'가 2개 이상 이라면, 왼쪽이든 오른쪽이든 더 끝 쪽에 가까이 있는 것을 선택
        2-3-2. 오른쪽으로만 조작 / 오론쪽 -> 왼쪽 으로 조작 / 왼쪽 -> 오른쪽 으로 조작 중 가장 작은 값 선택
'''

def solution(name):
    answer = 0
    
    import string, re
    
    # 1
    alphabets = list(string.ascii_uppercase)
    
    for i, letter in enumerate(name) :
        answer += min(alphabets.index(letter), len(alphabets) - alphabets.index(letter))
        
    # 2
    left = re.compile('A+').match(name).end() if re.compile('A+').match(name) else 0
    
    right = re.compile('A+').match(name[::-1]).end() if re.compile('A+').match(name[left:][::-1]) else 0
        
    middle = max([len(a) for a in re.compile('A+').findall(name[left:(len(name)-right)])]) if len([len(a) for a in re.compile('A+').findall(name[left:(len(name)-right)])]) != 0 else 0

    # 2-1
    if max(left, right, middle) == right :
        answer += len(name) - right - 1

    # 2-2
    elif max(left, right, middle) == left :
        answer += len(name) - left  
        
    # 2-3
    else : # max(left, right, middle) == middle
        idx_start = name.find('A'*middle)
        idx_end = len(name) - name[::-1].find('A'*middle) - 1
        
        # 2-3-1
        if idx_end - idx_start + 1 != middle :
            if idx_start < (len(name)-idx_end-1) :
                idx_end = idx_start + middle - 1
            else :
                idx_start = idx_end - middle + 1
        
        # 2-3-2
        answer += min((len(name)-right-1), ((idx_start-1)*2 +len(name)-idx_end-1), ((len(name)-idx_end-1)*2+idx_start-1))
            
    return answer

name = 'JEROEN' #56
name = 'JAN'   #23
name = 'ABB'
name = 'AAA'
name = 'BBAA'

solution(name)



########## 가장 큰 수 ##########
'''
sorted의 어트리뷰트 key에 사용할 수 있는 functools.cmp_to_key의 발견,,!
'''

def solution(numbers):

    from functools import cmp_to_key
    
    answer = ''
    
    def compare(x, y) :
        x, y = str(x), str(y)
        if int(x+y) < int(y+x) : return 1
        else : return -1
    
    numbers = sorted(numbers, key=cmp_to_key(compare))
    
    answer = ''.join([str(n) for n in numbers])
   
    if answer[0] == '0' :
        answer = '0'
    
    return answer


numbers = [6, 10, 2] # 6210
numbers = [3, 30, 34, 5, 9] # 9534330

numbers = [0,0,0]
numbers = [20,200,20]

solution(numbers)


########## 괄호변환 ##########

def solution(p):
    
    def isCorrect(w) :
        
        _open, close = 0, 0 
        for _w in w :
            
            if _w =='(' :
                _open += 1
            else :
                close += 1
                
            if close > _open :
                return False
        
        return True
    
    def reverseBracket(w) :
        return ''.join([')' if _w == '(' else '(' for _w in w])
    
    
    def splitToBalanced(w) :
        
        u = ''
        _open, close = 0, 0
        for _w in w :
            u += _w
            
            if _w =='(' :
                _open += 1
            else :
                close += 1
                
            if _open == close :
                break

        v = w[len(u):]
            
        return u, v
    
    def BalancedToCorrect(w) :
        
        # 1
        if w == '' :
            return ''
        
        # 2
        u, v = splitToBalanced(w)
        
        # 3
        if isCorrect(u) :
            return u + BalancedToCorrect(v)
        
        #4
        else :
            return '(' + BalancedToCorrect(v) + ')' + reverseBracket(u[1:-1])
        
    
    answer = BalancedToCorrect(p)
    
    return answer


p = "(()())()"   # "(()())()"
p = ")("   # "()"
p = "()))((()"   # "()(())()"


solution(p)



########## 종이접기 ##########

'''
1. 규칙 찾기 :
    n번 접은 종이의 굴곡의 모양은 (n-1)번 접은 종이의 굴곡의 모양의 0, 2, 4 ..., (2**n-2)번째에 각각 2**(n-2)개의 0과 1을 번갈아서 넣은 값과 같다.
2. 재귀 함수를 이용
'''

# 재귀함수 사용
def solution(n):
    
    answer = list()
    
    if n == 1 :
        answer = [0]
    
    else :  
        new = [1, 0]*(2**(n-2))
        
        for s in solution(n-1) :
            answer.append(new.pop())
            answer.append(s)
            
        answer.append(new.pop())
            
    return answer


# for문 사용
def solution(n):
    
    results = list()
    
    for i in range(n) :
        if i == 0 :
            results.append([0])
        else :
            results.append([])
            new = [1, 0] * (2**i)
            
            for r in results[i-1] :
                results[i].append(new.pop())
                results[i].append(r)
                
            results[i].append(new.pop())
                
    answer = results[n-1]
            
    return answer

n=1 # [0]
n=2 # [0,0,1]
n=3 # [0,0,1,0,0,1,1]
n=4 # [0,0,1,0,0,1,1,0,0,0,1,1,0,1,1]

solution(n)



########## 추석 트래픽 ##########
    
'''
1. 트래픽 시작 시간과 종료 시간 계산 : 
    (처리시간 - 0.001) 만큼 차이
2. 각 트래픽의 종료 시간부터 0.999초 까지의 시간을 기준으로 처리량 계산 : 
    종료 시간을 기준으로 오름차순 정렬이므로 (i+1) 번째 트래픽 부터 확인하면 된다
    break 조건 (선택) - 기준으로 부터 해당 트래픽의 종료 시간이 3.999초 이상일 때, 다음 트래픽 부터는 더 이상 확인할 필요가 없다
    continue 조건 (필수) - 기준으로 부터 해당 트래픽의 시작 시간이 0.999초 초과일 때, 해당 트래픽을 세지 않는다.
3. 계산한 처리량 중 최댓값으로 answer를 업데이트
'''


def solution(lines):
    
    answer = 0
    
    from dateutil.parser import parse
    from datetime import datetime as dt
    from datetime import timedelta as td
    from operator import itemgetter

    # 1
    traffics = list()
    
    for line in lines :
        a, b, c = line.split()
        traffics.append((parse(b) - td(seconds=float(c[:-1]) - 0.001), parse(b)))
        
    # 2
    for i in range(len(traffics)) :
        s, e = traffics[i]
        temp = 1
        for j in range(i+1, len(traffics)) :
            l, r = traffics[j]
            if r-e >= td(seconds=4-0.001) : break 
            if l-e > td(seconds=1-0.001) : continue
            temp += 1
        # 3
        answer = max(answer, temp)
    
    return answer

 
lines = ['2016-09-15 20:59:57.421 0.351s', '2016-09-15 20:59:58.233 1.181s',
         '2016-09-15 20:59:58.299 0.8s','2016-09-15 20:59:58.688 1.041s',
         '2016-09-15 20:59:59.591 1.412s','2016-09-15 21:00:00.464 1.466s',
         '2016-09-15 21:00:00.741 1.581s','2016-09-15 21:00:00.748 2.31s',
         '2016-09-15 21:00:00.966 0.381s','2016-09-15 21:00:02.066 2.62s'] # 7




########## 소수 찾기 ##########

def solution(numbers):
    answer = 0
    
    from itertools import permutations
      
    def isPrimeNumber(n) :
        if n < 2 :
            return False
        
        for i in range(2, int(n/2)) :
            if n%i == 0 : 
                return False
        return True
    
    numbers = list(numbers)
        
    for i in range(1, len(numbers)+1) :
#        print('i', i)
        for j in list(set(permutations(numbers, i))) :
            if j[0] != '0' :
#                print(j)
                if isPrimeNumber(int(''.join(j))) :
#                    print(int(''.join(j)))
                    answer += 1
        
    return answer

numbers = "17" # 3
numbers = "011" # 2


solution(numbers)













