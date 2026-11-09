# 각 종류 옷 하나 씩 착용
# 서로 다른 옷의 조합의 수 리턴하기
# 아무것도 안 입는거 -1

def solution(clothes):
    
    answer = 1
    d = {}
    
    # 딕셔너리에 추가
    for clothe_name, clothe in clothes:
            d[clothe] = d.get(clothe, 0) + 1
            
    # 루프 돌면서 모든 경우의 수 곱하기    
    for value in d.values():
        answer = answer * (value + 1)
    
    # 안입는 경우의 수 빼기
    return answer -1