# 4개지 지표 각각 두 유형 중 하나 16(=2 x 2 x 2 x 2) 종류
# 검사지에는 총 n개의 질문 7개 선택지 0 ~ 3 높은 유형 선택 
# 전자 1 ~ 3 모름 4 5 ~ 7 후자
# 단, 하나의 지표에서 각 성격 유형 점수가 같으면 사전 순으로
# 

# 판단 지표 리스트 # 선택한 선택지 리스트
def solution(survey, choices):
    
    # 딕셔너리
    score = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0
    }

    answer = ''
    
    # for 문 리스트를 돌면서 어디에 점수 줄지 판단 
    for idx, mbti in enumerate(survey):
        
        # 선택지 변수
        choice = choices[idx]
        
        # 추가할 점수 선언
        plus = 0
        
        if choice == 1:
            plus = 3
        elif choice == 2:
            plus = 2
        elif choice == 3:
            plus = 1
        elif choice == 4:
            plus = 0
        elif choice == 5:
            plus = 1
        elif choice == 6:
            plus = 2
        elif choice == 7:
            plus = 3
        
        # 1 ~ 3이면 전자 mbti[0]
        if 1 <= choice <= 3:
            score[mbti[0]] = score[mbti[0]] + plus
            
            
            
        # 4면 넘어가기 continue
        if choice == 4:
            score[mbti[0]] = score[mbti[0]] + plus
            
        # 5 ~ 7이면 후자 mbti[0]
        if 5 <= choice <=7:
            score[mbti[1]] = score[mbti[1]] + plus
    
    # for 돌면서 대비 되는거로 최종 mbti 구하기
    for first, second in ['RT', 'CF', 'JM', 'AN']:
        
        # answer에 추가하기
        if score[first] >= score[second]:
            answer = answer + first
        else:
            answer = answer + second
    

    return answer