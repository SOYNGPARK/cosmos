# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:05:19 2020

@author: soug9
"""


########## 더 맵게 ##########

'''
heapq의 발견


'''

# heapq로 구현
def solution(scoville, K):
    answer = 0
    
    def mix(m, n) :
        return m + 2*n
    
    import heapq
    
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        if len(scoville) < 2 :
            answer = -1
            break
        
        heapq.heappush(scoville, mix(heapq.heappop(scoville), heapq.heappop(scoville)))
        answer += 1
        
    return answer

scoville, K = [1, 2, 3, 9, 10, 12], 7 # 2

solution(scoville, K)



########## 전화번호 목록 ##########

def solution(phone_book):
    answer = True
    
    phone_book = sorted(phone_book, key=len)
    
    for i, h in enumerate(phone_book) :
        if len([p for p in phone_book[i+1:] if h == p[:len(h)]]) > 0 :
            answer = False
            break
    
    return answer

phone_book = ['119', '97674223', '1195524421'] # false
phone_book = ['123', '412356', '789'] # true
phone_book = ['12', '123', '1235', '567', '88'] # false

solution(phone_book)




########## H-Index ##########

def solution(citations):
    answer = 0
    
    for h in range(len(citations), -1 , -1) :
        if len([c for c in citations if c >= h]) >= h :
            answer = h
            break

    return answer


citations = [3, 0, 6, 1, 5]	# 3 
citations = [4, 2, 3, 0, 9, 9, 6, 3]	# 4
citations = [4, 3, 3] # 3
citations = [1, 1] # 1

solution(citations)



########## 2 X n 타일링 ##########


'''
%1000000007을 return에서가 아닌 for문 안에 넣으면 효율성 통과
'''


def solution(n):
    
    answers = [0,1,2]

    if n > 2 :
        for i in range(3, n+1) :
            answers.append((answers[-1] + answers[-2])%1000000007)
        
    return answers[n]

n = 4 # 5

solution(n)



########## N으로 표현 ##########

'''
N이 1~8개 일 때, 만들 수 있는 숫자 중 number가 있는 지 확인
N의 개수 = a+b로 표현할 때, N이 a개 일 때 만들 수 있는 숫자와 N이 b일 때 만들 수 있는 숫자를 사칙연산
ex. 5 = 1+4 = 2+3
'''

def solution(N, number):
    answer = -1
    
    if N == number :
        answer == 1
    
    combi = [[-1]] * 9
    
    combi[1] = [N]
    
    for i in range(2, 9) :
        for j in range(1, 1+ int(i/2)) :
            x, y = combi[i-j], combi[j] # x >= y
            
            for xx in x :
                for yy in y :
                    combi[i] = combi[i] + [xx+yy, xx-yy, xx*yy, int(str(N)*i)]
                    if yy != 0 :
                            combi[i].append(int(xx/yy))
        
        del combi[i][0]
        combi[i] = list(set(combi[i]))
        
        if number in combi[i] :
            answer = i
            break
    
    return answer


N, number = 5, 12 # 4
N, number = 2, 11 # 3

solution(N, number)



























