import numpy as np
import random

# 1부터 54까지의 숫자를 무작위로 섞어서 리스트 생성
num_list = list(range(1, 55))
random.shuffle(num_list)

# 18x3 행렬로 재배열
our_matrix = np.reshape(num_list, (18, 3))

# 중복 없이 숫자 7개 뽑기
selected_numbers = random.sample(num_list, 7)

# 같은 행렬 내에서 두 번째 열 값을 선택하면 첫 번째와 세 번째 열 값을 선택하지 못하도록 제한
excluded_rows = set()
excluded_columns = set()

for _ in range(7):
    available_rows = [row for row in range(18) if row not in excluded_rows]
    available_columns = [col for col in range(3) if col not in excluded_columns]

    row = random.choice(available_rows)
    col = random.choice(available_columns)

    # 선택한 행, 열의 숫자를 selected_numbers에 추가
    selected_numbers.append(our_matrix[row, col])

    # 첫 번째 또는 세 번째 열을 선택했을 경우, 두 번째 열을 제외 처리
    if col == 0 or col == 2:
        excluded_columns.add(1)

    # 두 번째 열을 선택했을 경우, 첫 번째와 세 번째 열을 제외 처리
    else:
        excluded_columns.add(0)
        excluded_columns.add(2)

    # 선택한 행을 제외 처리
    excluded_rows.add(row)

# 중복 제거 후 7개만 선택
selected_numbers = random.sample(set(selected_numbers), 7)

# 결과 출력
print("our_matrix:")
print(our_matrix)
print("선택된 숫자:", selected_numbers)
