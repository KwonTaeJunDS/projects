# 학생 데이터를 저장할 리스트
students = []

# 학점 계산 함수
def assign_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# 학생 데이터 불러오기 함수
def call(filename='students.txt'):
    global students
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split('\t')
                student = {
                    'id': data[0],
                    'name': data[1],
                    'midterm': int(data[2]),
                    'final': int(data[3]),
                    'average': (int(data[2]) + int(data[3])) / 2,
                    'grade': assign_grade((int(data[2]) + int(data[3])) / 2)
                }
                students.append(student)
        print("학생 데이터를 성공적으로 불러왔습니다.")
    except FileNotFoundError:
        print(f"파일 {filename} 을(를) 찾을 수 없습니다.")

# 학생 데이터 출력 함수
def show_function():
    if not students:
        print("학생 데이터가 없습니다. 파일을 먼저 불러오세요.")
        return

    print(f"{'ID':<10}{'Name':<15}{'Midterm':<10}{'Final':<10}{'Average':<10}{'Grade':<5}")
    print("-" * 60)
    for student in sorted(students, key=lambda x: x['average'], reverse=True):
        print(f"{student['id']:<10}{student['name']:<15}{student['midterm']:<10}{student['final']:<10}{student['average']:<10.2f}{student['grade']:<5}")

# 특정 학생 검색 함수
def search():
    student_id = input("검색할 학생의 학번을 입력하세요: ")
    for student in students:
        if student['id'] == student_id:
            print(f"ID: {student['id']}, Name: {student['name']}, Midterm: {student['midterm']}, Final: {student['final']}, Average: {student['average']:.2f}, Grade: {student['grade']}")
            return
    print("해당 학생을 찾을 수 없습니다.")

# 새로운 학생 추가 함수
def add():
    student_id = input("학번: ")
    if any(student['id'] == student_id for student in students):
        print("이미 존재하는 학번입니다.")
        return

    name = input("이름: ")
    midterm = int(input("중간고사 점수: "))
    final = int(input("기말고사 점수: "))

    average = (midterm + final) / 2
    grade = assign_grade(average)

    students.append({
        'id': student_id,
        'name': name,
        'midterm': midterm,
        'final': final,
        'average': average,
        'grade': grade
    })
    print("학생이 성공적으로 추가되었습니다.")

# 학생 점수 변경 함수
def changescore():
    student_id = input("점수를 변경할 학생의 학번을 입력하세요: ")
    for student in students:
        if student['id'] == student_id:
            print(f"현재 중간 점수: {student['midterm']}, 기말 점수: {student['final']}")
            exam_type = input("수정할 시험을 선택하세요 (midterm/final): ").lower()
            if exam_type == 'midterm':
                student['midterm'] = int(input("새로운 중간고사 점수: "))
            elif exam_type == 'final':
                student['final'] = int(input("새로운 기말고사 점수: "))
            else:
                print("잘못된 입력입니다.")
                return

            student['average'] = (student['midterm'] + student['final']) / 2
            student['grade'] = assign_grade(student['average'])
            print("점수가 성공적으로 변경되었습니다.")
            return
    print("해당 학생을 찾을 수 없습니다.")


def main():
    while True:
        print("\n[1] 데이터 불러오기 (call)\n[2] 데이터 출력 (show)\n[3] 학생 검색 (search)\n[4] 학생 추가 (add)\n[5] 점수 변경 (changescore)\n[6] 종료 (quit)")
        choice = input("선택: ")

        if choice == '1':
            call()
        elif choice == '2':
            show_function()
        elif choice == '3':
            search()
        elif choice == '4':
            add()
        elif choice == '5':
            changescore()
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
