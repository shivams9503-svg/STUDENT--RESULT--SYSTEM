print("HEY EVERYBODY WELCOME TO PTM")
print("PLEASE EVERYONE HAVE YOUR SEAT")
print("One by one, come and take your child's result")
print("SO, Let's start it")
print("Firstly come RICKY AND JIYA parents")
TEACHER = input("Teacher, your name: ")
PARENT = input("Parent, my child's name is: ").strip().upper()

Results = {
    "RICKY": {
        "CLASS & SECTION": "4TH & E",
        "SUBJECT": "ENGLISH,HINDI,SST,MATH,SCIENCE",
        "ENGLISH": "98 OUT OF 100",
        "HINDI": "86 OUT OF 100",
        "SST": "80 OUT OF 100",
        "MATH": "100 OUT OF 100",
        "SCIENCE": "90 OUT OF 100",
    },
    "JIYA": {
        "CLASS & SECTION": "4TH & E",
        "SUBJECT": "ENGLISH,HINDI,SST,MATH,SCIENCE",
        "ENGLISH": "99 OUT OF 100",
        "HINDI": "100 OUT OF 100",
        "SST": "100 OUT OF 100",
        "MATH": "98 OUT OF 100",
        "SCIENCE": "99 OUT OF 100",
    },
    "ASHU": {
        "CLASS & SECTION": "4TH & E",
        "SUBJECT": "ENGLISH,HINDI,SST,MATH,SCIENCE",
        "ENGLISH": "98 OUT OF 100",
        "HINDI": "85 OUT OF 100",
        "SST": "90 OUT OF 100",
        "MATH": "89 OUT OF 100",
        "SCIENCE": "87 OUT OF 100",
    },
    "ROSE": {
        "CLASS & SECTION": "4TH & E",
        "SUBJECT": "ENGLISH,HINDI,SST,MATH,SCIENCE",
        "ENGLISH": "98 OUT OF 100",
        "HINDI": "92 OUT OF 100",
        "SST": "70 OUT OF 100",
        "MATH": "89 OUT OF 100",
        "SCIENCE": "87 OUT OF 100",
    },
    "MAX": {
        "CLASS & SECTION": "4TH & E",
        "SUBJECT": "ENGLISH,HINDI,SST,MATH,SCIENCE",
        "ENGLISH": "80 OUT OF 100",
        "HINDI": "70 OUT OF 100",
        "SST": "90 OUT OF 100",
        "MATH": "50 OUT OF 100",
        "SCIENCE": "100 OUT OF 100",
    },
}

if PARENT in Results:
    student = Results[PARENT]
    print(f"NAME : {PARENT}")
    print(f"CLASS & SECTION : {student['CLASS & SECTION']}")
    print(f"SUBJECTS : {student['SUBJECT']}")
    print(f"ENGLISH : {student['ENGLISH']}")
    print(f"HINDI : {student['HINDI']}")
    print(f"SST : {student['SST']}")
    print(f"MATH : {student['MATH']}")
    print(f"SCIENCE : {student['SCIENCE']}")
    print(f"Hello {PARENT}, welcome to the PTM. {TEACHER} will call you soon.")
    print("THANK YOU SIR/MAM, I HOPE YOU LIKE IT. PLEASE GIVE FEEDBACK ON SCHOOL PERFORMANCE.")
   
    print("THANK YOU SIR/MAM FOR COMING AND ATTENDING PTM, PLEASE GIVE SOME POSITIVE GRADE TO OUR STAFF PERFORMANCE.")
    total = (
        int(student["ENGLISH"].split()[0])
        + int(student["HINDI"].split()[0])
        + int(student["SST"].split()[0])
        + int(student["MATH"].split()[0])
        + int(student["SCIENCE"].split()[0])
    )
    percentage = total / 500 * 100
    print(f"TOTAL : {total} OUT OF 500")
    print(f"PERCENTAGE : {percentage:.2f}%")
else:
    print("Please take a seat, your turn is coming. Please wait.")
