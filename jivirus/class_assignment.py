class Student:
    
    def __init__(self, name, schoolnum, semester, subject):  #init으로 생성자 생성
        self.name = name    #name 매개변수 값을 Student.name에 저장
        self.schoolnum = schoolnum #schoolNum 매개변수 값을 Student.schoolNum에 저장
        self.semester = semester   #semester 매개변수 값을 Student.semester에 저장
        self.subject = subject     #subject 매개변수 값을 Student.subject에 저장

    def print_name(self):  #이름을 입력하는 메소드
        print(f"이름은 {self.name}입니다.") #포매팅을 사용하여 출력함

    def print_schoolNum(self): #학번으로 소속을 출력하는 메소드
        if self.schoolnum[5:6] == "1":  #학번의 숫자가 1일때 
            print(f"학번은 {self.schoolnum}로 인문융합자율학부 소속입니다.")
        elif self.schoolnum[5:6] == "2": #학번의 숫자가 2일때 
            print(f"학번은 {self.schoolnum}로 사회융합자율학부 소속입니다.")
        elif self.schoolnum[5:6] == "3":  #학번의 숫자가 3일때 
            print(f"학번은 {self.schoolnum}로 미디어자율학부 소속입니다.")
        elif self.schoolnum[5:6] == "4":  #학번의 숫자가 4일때 
            print(f"학번은 {self.schoolnum}로 IT융합자율학부 소속입니다.")   
        else: #학번의 숫자 그외일 때
            print(f"오류입니다.\n")  #오류   

    def print_semester(self): #학기를 출력하는 메소드
        if self.semester <= 3: #3학기 이하
            print(f"{self.name}은 {self.semester}학기차로 전공선택 전입니다.")
        elif self.semester >= 4: #4학기부터
            print(f"{self.name}은 {self.semester}학기차로 전공선택을 마쳤습니다.")
        else:
            print(f"오류입니다.") #오류
    
    def print_subject(self): #수강 과목 출력하는 메소드
        print(f"{self.subject}를 수강합니다.")

    def subject_info(self): #수강 과목을 출력하는 메소드
        print("자세한 수강 목록입니다.")
        for subject, length in subject_dict.items(): #딕셔너리의 요소를 과목명과 과목의 길이을 같이 출력하게 해줌
            print(f"과목명: {subject} / 과목명의 길이: {length}")

    

while True: #반복문
    class_name=[] #반복문에서 class_name을 사용전 null값을 지정해주었습니다
    class_name == input("객체 명을 입력하시오. (단, 영문으로):") #
    if class_name == "종료":
        break

    name = input("이름을 입력하시오. (단, 한글로) ")
    schoolNum = input("학번을 입력하시오: ")
    while len(schoolNum) != 9:
        print("오류입니다.\n")
        schoolNum = input("학번을 입력하시오: ")

    semester = int(input("학기를 입력하시오. (단, 숫자로): "))

    subject_list = []
    subject_dict = {}

    for _ in range(3):
        subject = input("과목을 입력하시오: ")
        subject_list.append(subject)
        subject_dict[subject] = len(subject)

    print()

    class_name = Student(name, schoolNum, semester, subject_list)

    class_name.print_name()
    class_name.print_schoolNum()
    class_name.print_semester()
    class_name.print_subject()
    print()

    class_name.subject_info()
    print()

        