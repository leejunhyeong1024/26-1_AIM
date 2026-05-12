#문자열 입력받은 후 대문자로 정리
a = input().upper() 

# 중복 제거된 알파벳 리스트
unique_lst = list(set(a)) 
# 각 문자가 나온 횟수
cnt = []              

# 각 알파벳의 개수를 순서대로 추가
for i in unique_lst:
    cnt.append(a.count(i)) 

# 가장 많이 나온 문자가 몇 번인지 찾기
max_val = max(cnt)

# 가장 많이 나온 문자가 리스트에 몇 개 있는지 확인
if cnt.count(max_val) > 1:
    print('?')
else:
    # 가장 많이 나온 문자가 하나라면 그 문자 출력
    max_index = cnt.index(max_val)
    print(unique_lst[max_index])