def operation(x, y, op):
    if op == "U":
        y += 1
    elif op == "D":
        y -= 1
    elif op == "R":
        x += 1
    elif op == "L":
        x -= 1
    return x, y

def isValid(x, y):
    if x < 0 or x > 10 or y < 0 or y > 10: # 벗어난다면
        print("벗어났습니다.")
        return False
    return True

def solution(str):
    ans = 0
    x, y = 5, 5
    road = set() # 방문처리


    for direction in str:
        nx, ny = operation(x, y, direction) # 해당 방향으로 이동할 수 있느냐, 없느냐를 따져야하므로 nx ny를 먼저 구해야함

        if isValid(nx, ny) == False: # 새로운 좌표가 벗어났으면 무시함. (현재 좌표를 넣고 비교하는 건 의미 없음. 현재는 valid해서 이미 도달한 거니까)
            continue
        if (x, y, nx, ny) not in road and (nx, ny, x, y) not in road:
            road.add((x, y, nx, ny))
            road.add((nx, ny, x, y))
            ans += 1 # 새로운 길이니까 추가
        x, y = nx, ny # 새로운 좌표값으로 업데이트

    return ans


print(solution("ULURRDLLU")) # 7
print(solution("LULLLLLLU")) # 7