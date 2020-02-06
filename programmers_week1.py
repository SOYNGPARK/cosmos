# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:29:28 2020

@author: soug9
"""


########## 1. 기능개발 ##########

def solution(progresses, speeds):
    answer = []
    
    todo = [100 - i for i in progresses]
    days = [int(i / j) + 1 if i%j != 0 else int(i / j) for i, j in zip(todo, speeds)]
    
    now = 0
    schd = list()
    _break = False
    while True :
        if _break :
            break
        
        release = list()
        for i in range(now, len(days)) :
            
            front = days[i]
            
            release.append(front)
            now += 1
            
            if i == len(days)-1 : 
                _break = True
                break
            
            else :
                end = days[i+1]
                if (front < end) and (release[0] < end) :
                    break
                else :
                    pass
        
        schd.append(release)
                
                
    answer = [len(s) for s in schd]
                
    return answer


progresses, speeds = [40,93,30,55,60,65], [60,1,30,5,10,7] #[1,2,3] 

solution(progresses, speeds)



########## 2. 탑 ##########

def solution(heights):
    answer = [0]*len(heights)
    
    for i in range(len(heights)-1, 0, -1) :
        print(i)
        
        right = heights[i]
        lefts = heights[:i]
        
#        print('right', right)
#        print('lefts', lefts)
        
        for j in range(len(lefts)-1, -1, -1) :
            if lefts[j] > right :
                answer[i] = j+1
                break
        
#        print('answer', answer[i])
            
    return answer


heights = [4,5,2,6,7] # [0,0,2,0,0]
heights = [11,5,3,6,7,6,5] # [0,1,2,1,1,5,6]

solution(heights)


########## 3. 멀쩡한 사각형 ##########

def solution(w,h):
    
    a = (w*w + h*h)**0.5 / w
    b = (a*a - 1)**0.5
    
    hs = [int(h - i*b) for i in range(1, w+1)]
    
    answer = sum(hs) * 2
    
    return answer



def solution(w,h):
    
    import math
    
    def gcd(w,h) :
        
        if w < h :
            temp = w
            w = h
            h = temp
        
        if h == 0 :
            return w
        else :
            return gcd(h, w%h)
        
    ## end of inner function gcd()
    
    gcd = gcd(w,h)
    ww, hh = w/gcd, h/gcd
    
    slope = hh/ww
    
    remove = sum([math.ceil((i+1)*slope) - int(i*slope) for i in range(int(ww))])
           
    answer = w*h - gcd*remove
    
    return answer

w, h = 8, 12

solution(w,h)



########## 4. 다리를 지나는 트럭 ##########

def solution(bridge_length, weight, truck_weights):
    
    answer = 0   
    trucks_on_bridge = list()
    trucks_passed_length = list()
    
    while True :
        
        # break
        if (len(truck_weights) == 0) and (len(trucks_on_bridge) == 0) :
            break
        
        # out
        if bridge_length in trucks_passed_length :
            if len(trucks_on_bridge) != 0 :
#                print('out', trucks_on_bridge[0])
                del trucks_on_bridge[0]
    
        # in
        if len(truck_weights) != 0 :
            if (sum(trucks_on_bridge) + truck_weights[0] <= weight) and (len(trucks_on_bridge) + 1 <= bridge_length) :
#                print('in', truck_weights[0])
                trucks_on_bridge.append(truck_weights[0])
                trucks_passed_length.append(0)
                del truck_weights[0]
                
        answer += 1
        trucks_passed_length = [tpl + 1 for tpl in trucks_passed_length]
        
#        print('answer', answer)
#        print('trucks_on_bridge', trucks_on_bridge)
#        print()
        
    return answer
    
bridge_length, weight, truck_weights = 2, 10, [7,5,4,6] # 7
bridge_length, weight, truck_weights = 100, 100, [10]	# 101
bridge_length, weight, truck_weights = 100, 100, [10,10,10,10,10,10,10,10,10,10]	#110

solution(bridge_length, weight, truck_weights)



########## 5. 스킬트리 ##########

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees :
        skill_tree = list(skill_tree)
        skill_tree_idx = [skill_tree.index(s) if s in skill_tree else '*' for s in skill]
        print(skill_tree_idx)
        
        if '*' in skill_tree_idx :
            star = skill_tree_idx.index('*')
            if (skill_tree_idx[star:] == ['*'] * len(skill_tree_idx[star:])) and (sorted(skill_tree_idx[:star]) == skill_tree_idx[:star]) :
                answer +=1
        else :
            if sorted(skill_tree_idx) == skill_tree_idx :
                answer += 1
        
    return answer

skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA", "AEBC"]	#2
solution(skill, skill_trees)



########## 6. 프린터 ##########

def solution(priorities, location):
    answer = 0
    
    def firstOut(element, sequence) :
        
        temp = sequence[element]
        del sequence[element]
        sequence.append(temp)
        
        return sequence
    
    
    priorities_loc = [i for i in range(len(priorities))]
    _break = False


    while True :
        if _break :
            break
        
        for i, p in enumerate(priorities) :   
#            print(i)
#            print('priorities', priorities)
#            print('priorities_loc', priorities_loc)
            if len([p for p in priorities[i:] if p>priorities[i]]) > 0 :
                priorities = firstOut(i, priorities)
                priorities_loc = firstOut(i, priorities_loc)
                break
            elif i == len(priorities) - 1 :
                _break = True

    answer = priorities_loc.index(location) + 1
    
    return answer


priorities, location = [2, 1, 3, 2], 2   # 1
priorities, location = [1, 1, 9, 1, 1, 1], 0 # 5
priorities, location = [4,2,3,0,9,9,6,3], 1 # 7

solution(priorities, location)



########## 7. 쇠막대기 ##########

def solution(arrangement):
    answer = 0
 
    nums =list()
    _iter = iter(range(len(arrangement)))
    arrangement_num = list()
    
    
    for i, a in enumerate(arrangement) :
        if a == "(" :
            arrangement_num.append(next(_iter))
            nums.append(arrangement_num[-1])
        elif a == ")" :
            if arrangement[i-1] == "(" :
                nums.remove(arrangement_num.pop())
                arrangement_num.append('*')      
            else :
                arrangement_num.append(max(nums))
                nums.remove(arrangement_num[-1])
        else : # a == '*'
            arrangement_num.append("*")
    

    for s in range(len(arrangement)) :
        idx_pair = [i for i, an in enumerate(arrangement_num) if an == s]
        if len(idx_pair) != 0 :
            answer += len([an for an in arrangement_num[idx_pair[0]:idx_pair[1]] if an == '*'])+1
        
            print(s)
            print(arrangement_num[idx_pair[0]:idx_pair[1]])
            print(len([an for an in arrangement_num[idx_pair[0]:idx_pair[1]] if an == '*']))
            print()

    return answer


arrangement = "()(((()())(())()))(())" #	17

solution(arrangement)

























