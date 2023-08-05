all_student = [i for i in range(1,31)]
for _ in range(28):
    student = int(input())
    all_student.remove(student)

print(min(all_student))
print(max(all_student))
    