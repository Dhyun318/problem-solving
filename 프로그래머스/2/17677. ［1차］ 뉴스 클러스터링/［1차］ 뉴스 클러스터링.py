# 자카드 유사도 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# 두 글자씩 끊어서 다중 집합 원소로 만들기 (영문 쌍)
# 대소문자 같은 취급

def solution(str1, str2):
    
    answer = 0
    
    s1 = []
    s2 = []
    
    # 1. 다중 집합 원소 만들기
    # for문으로 슬라이싱 하기 [i:i+1]
    for i in range(len(str1)-1):
        
    # 2-1. 영문 쌍 아닌거 지우기
    # .isalpha True 확인
        if str1[i:i+2].isalpha() == True:
            
            # 2-2. 대소문자 같은 취급하기 # upper하고 넣기
            s1.append(str1[i:i+2].upper())
    
    for i in range(len(str2)-1):
        
        if str2[i:i+2].isalpha() == True:
            s2.append(str2[i:i+2].upper()) 
    
    union_list = []
    inter_list = []

    # 3. 교집합, 합집합 구하기
    for item in s1:
        
        # 교집합 + 합집합 처리 (겹치는거)
        if item in s2:
            inter_list.append(item)
            union_list.append(item)
            
            # 중복 추가 방지
            s2.remove(item)
            
        # 합집합 처리 (안 겹치는거)
        else:
            union_list.append(item)
            
    # s2 남은 원소 더하기
    union_list = union_list + s2
    
    # 4. 자카드 유사도 구하기 len() 
    if len(union_list) != 0:
        answer = len(inter_list) / len(union_list)
        
    else:
        answer = 1
    
    # 65536 곱하고 정수만 출력
    return int(answer*65536)