#!/usr/bin/env python
# coding: utf-8

# ### 오름차순만(내림차순 포함은 밑에)

# In[74]:


import random
import string

# 학생 정보 생성 함수
def generate_students(n=30):
    students = []
    for _ in range(n):
        name = ''.join(random.choices(string.ascii_uppercase, k=2))  # 두 글자 이름
        age = random.randint(18, 22)  # 나이: 18~22
        score = random.randint(0, 100)  # 성적: 0~100
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 학생 정보 출력 함수
def print_students(students):
    print("\n=== 학생 정보 ===")
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")

# 선택 정렬 
def selection_sort(students, key):
    print("\n[선택 정렬 과정]")
    n = len(students)
    for i in range(n - 1):
        selected_index = i
        for j in range(i + 1, n):
            if students[j][key] < students[selected_index][key]:  # 오름차순 정렬만 적용
                selected_index = j
        students[i], students[selected_index] = students[selected_index], students[i]
        print(f"Step {i + 1}: {students}")

# 삽입 정렬 
def insertion_sort(students, key):
    print("\n[삽입 정렬 과정]")
    for i in range(1, len(students)):
        current = students[i]
        j = i - 1
        while j >= 0 and students[j][key] > current[key]:  # 오름차순 정렬만 적용
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = current
        print(f"Step {i}: {students}")

# 퀵 정렬 
def quick_sort(students, left, right, key):
    print("\n[퀵 정렬 과정]")
    if left < right:
        pivot_index = partition(students, left, right, key)
        quick_sort(students, left, pivot_index - 1, key)
        quick_sort(students, pivot_index + 1, right, key)

def partition(students, left, right, key):
    pivot = students[left]
    low = left + 1
    high = right
    while True:
        while low <= high and students[low][key] <= pivot[key]:  # 오름차순 정렬만 적용
            low += 1
        while low <= high and students[high][key] > pivot[key]:  # 오름차순 정렬만 적용
            high -= 1
        if low <= high:
            students[low], students[high] = students[high], students[low]
        else:
            break
    students[left], students[high] = students[high], students[left]
    print(f"Step: {students}")
    return high

# 기수 정렬 
def radix_sort(students, key):
    print("\n[기수 정렬 과정]")
    max_score = max(students, key=lambda x: x[key])[key]
    exp = 1
    while max_score // exp > 0:
        counting_sort(students, key, exp)
        exp *= 10
        print(f"Step (exp={exp}): {students}")

def counting_sort(students, key, exp):
    output = [None] * len(students)
    count = [0] * 10

    # 각 성적의 자릿수를 계산하여 카운팅
    for student in students:
        index = student[key] // exp % 10
        count[index] += 1

    # 누적 합을 계산하여 위치를 정확히 맞춰줌
    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(students) - 1, -1, -1):  # 항상 오름차순 정렬
        index = students[i][key] // exp % 10
        output[count[index] - 1] = students[i]
        count[index] -= 1

    # 정렬된 결과를 원본 리스트에 복사
    for i in range(len(students)):
        students[i] = output[i]

# 정렬 알고리즘 선택 및 실행
def sort_students(students, key, algorithm):
    if algorithm == "선택 정렬":
        selection_sort(students, key)
    elif algorithm == "삽입 정렬":
        insertion_sort(students, key)
    elif algorithm == "퀵 정렬":
        quick_sort(students, 0, len(students) - 1, key)
    elif algorithm == "기수 정렬":
        radix_sort(students, key)

# 프로그램 메인 함수
def main():
    students = generate_students()
    
    # 학생 성적 정보 출력
    print_students(students)

    while True:
        print("\n=== 학생 성적 관리 프로그램 ===")
        print("1. 이름 기준으로 정렬")
        print("2. 나이 기준으로 정렬")
        print("3. 성적 기준으로 정렬")
        print("4. 프로그램 종료")
        
        try:
            choice = int(input("원하는 기능을 선택하세요 (1/2/3/4): "))
        except ValueError:
            print("잘못된 입력입니다. 다시 선택하세요.")
            continue
        
        if choice == 4:
            print("프로그램을 종료합니다.")
            break

        if choice not in [1, 2, 3]:
            print("잘못된 선택입니다. 다시 입력하세요.")
            continue
        
        print("\n정렬할 알고리즘을 선택하세요:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬")
        
        try:
            algo_choice = int(input("원하는 알고리즘을 선택하세요 (1/2/3/4): "))
        except ValueError:
            print("잘못된 입력입니다. 다시 선택하세요.")
            continue
        
        if algo_choice not in [1, 2, 3, 4]:
            print("잘못된 선택입니다. 다시 입력하세요.")
            continue
        
        # 기수 정렬은 성적 기준으로만 사용 가능
        if (choice != 3 and algo_choice == 4):
            print("기수 정렬은 성적 기준으로 정렬 할 때만 선택 가능합니다.")
            continue
        
        # 선택된 정렬 알고리즘 실행
        algorithm = ["선택 정렬", "삽입 정렬", "퀵 정렬", "기수 정렬"][algo_choice - 1]
        
        if choice == 1:
            print("\n정렬 전 학생 정보:")
            print_students(students)
            sort_students(students, "이름", algorithm)
        elif choice == 2:
            print("\n정렬 전 학생 정보:")
            print_students(students)
            sort_students(students, "나이", algorithm)
        elif choice == 3:
            print("\n정렬 전 학생 정보:")
            print_students(students)
            sort_students(students, "성적", algorithm)
        
        # 정렬 후 학생 정보 출력
        print("\n정렬된 학생 정보:")
        print_students(students)

if __name__ == "__main__":
    main()


# ### 내림차순 포함

# In[70]:


import random
import string

# 학생 정보 생성 함수
def generate_students(n=30):
    students = []
    for _ in range(n):
        name = ''.join(random.choices(string.ascii_uppercase, k=2))  # 두 글자 이름
        age = random.randint(18, 22)  # 나이: 18~22
        score = random.randint(0, 100)  # 성적: 0~100
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 학생 정보 출력 함수
def print_students(students):
    print("\n=== 학생 정보 ===")
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")

# 선택 정렬 
def selection_sort(students, key, reverse=False):
    print("\n[선택 정렬 과정]")
    n = len(students)
    for i in range(n - 1):
        selected_index = i
        for j in range(i + 1, n):
            if (students[j][key] < students[selected_index][key] if not reverse else students[j][key] > students[selected_index][key]):
                selected_index = j
        students[i], students[selected_index] = students[selected_index], students[i]
        print(f"Step {i + 1}: {students}")

# 삽입 정렬 
def insertion_sort(students, key, reverse=False):
    print("\n[삽입 정렬 과정]")
    for i in range(1, len(students)):
        current = students[i]
        j = i - 1
        while j >= 0 and (students[j][key] > current[key] if not reverse else students[j][key] < current[key]):
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = current
        print(f"Step {i}: {students}")

# 퀵 정렬 
def quick_sort(students, left, right, key, reverse=False):
    print("\n[퀵 정렬 과정]")
    if left < right:
        pivot_index = partition(students, left, right, key, reverse)
        quick_sort(students, left, pivot_index - 1, key, reverse)
        quick_sort(students, pivot_index + 1, right, key, reverse)

def partition(students, left, right, key, reverse):
    pivot = students[left]
    low = left + 1
    high = right
    while True:
        while low <= high and (students[low][key] <= pivot[key] if not reverse else students[low][key] >= pivot[key]):
            low += 1
        while low <= high and (students[high][key] > pivot[key] if not reverse else students[high][key] < pivot[key]):
            high -= 1
        if low <= high:
            students[low], students[high] = students[high], students[low]
        else:
            break
    students[left], students[high] = students[high], students[left]
    print(f"Step: {students}")
    return high

# 기수 정렬 
def radix_sort(students, key, reverse=False):
    print("\n[기수 정렬 과정]")
    max_score = max(students, key=lambda x: x[key])[key]
    exp = 1
    while max_score // exp > 0:
        counting_sort(students, key, exp, reverse)
        exp *= 10
        print(f"Step (exp={exp}): {students}")

def counting_sort(students, key, exp, reverse=False):
    output = [None] * len(students)
    count = [0] * 10

    # 각 성적의 자릿수를 계산하여 카운팅
    for student in students:
        index = student[key] // exp % 10
        count[index] += 1

    # 누적 합을 계산하여 위치를 정확히 맞춰줌
    for i in range(1, 10):
        count[i] += count[i - 1]

    if reverse:
        for i in range(len(students)):
            index = students[i][key] // exp % 10
            output[count[index] - 1] = students[i]
            count[index] -= 1
    else:
        for i in range(len(students) - 1, -1, -1):
            index = students[i][key] // exp % 10
            output[count[index] - 1] = students[i]
            count[index] -= 1

    # 정렬된 결과를 원본 리스트에 복사
    for i in range(len(students)):
        students[i] = output[i]

# 정렬 알고리즘 선택 및 실행
def sort_students(students, key, algorithm, reverse=False):
    if algorithm == "선택 정렬":
        selection_sort(students, key, reverse)
    elif algorithm == "삽입 정렬":
        insertion_sort(students, key, reverse)
    elif algorithm == "퀵 정렬":
        quick_sort(students, 0, len(students) - 1, key, reverse)
    elif algorithm == "기수 정렬":
        radix_sort(students, key, reverse)

# 프로그램 메인 함수
def main():
    students = generate_students()
    
    # 학생 성적 정보 출력
    print_students(students)

    while True:
        print("\n=== 학생 성적 관리 프로그램 ===")
        print("1. 이름 기준으로 정렬")
        print("2. 나이 기준으로 정렬")
        print("3. 성적 기준으로 정렬")
        print("4. 프로그램 종료")
        
        try:
            choice = int(input("원하는 기능을 선택하세요 (1/2/3/4): "))
        except ValueError:
            print("잘못된 입력입니다. 다시 선택하세요.")
            continue
        
        if choice == 4:
            print("프로그램을 종료합니다.")
            break

        if choice not in [1, 2, 3]:
            print("잘못된 선택입니다. 다시 입력하세요.")
            continue
        
        print("\n정렬할 알고리즘을 선택하세요:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬")
        
        try:
            algo_choice = int(input("원하는 알고리즘을 선택하세요 (1/2/3/4): "))
        except ValueError:
            print("잘못된 입력입니다. 다시 선택하세요.")
            continue
        
        if algo_choice not in [1, 2, 3, 4]:
            print("잘못된 선택입니다. 다시 입력하세요.")
            continue
        
        # 기수 정렬은 성적 기준으로만 사용 가능
        if (choice != 3 and algo_choice == 4):
            print("기수 정렬은 성적 기준으로 정렬 할 때만 선택 가능합니다.")
            continue
        
        reverse = input("오름차순 (1) / 내림차순 (2): ")
        reverse = True if reverse == "2" else False
        
        # 선택된 정렬 알고리즘 실행
        algorithm = ["선택 정렬", "삽입 정렬", "퀵 정렬", "기수 정렬"][algo_choice - 1]
        
        if choice == 1:
            print("\n정렬 전 학생 정보:")
            print_students(students)
            sort_students(students, "이름", algorithm, reverse)
        elif choice == 2:
            print("\n정렬 전 학생 정보:")
            print_students(students)
            sort_students(students, "나이", algorithm, reverse)
        elif choice == 3:
            print("\n정렬 전 학생 정보:")
            print_students(students)
            sort_students(students, "성적", algorithm, reverse)
        
        # 정렬 후 학생 정보 출력
        print("\n정렬된 학생 정보:")
        print_students(students)

if __name__ == "__main__":
    main()

