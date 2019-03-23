from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    sum = 0
    Student = namedtuple('Student', input())
    for _ in range(n):
        att1, att2, att3, att4 = input().split()
        stu = Student(att1, att2, att3, att4)
        sum += int(stu.MARKS)
    print("%.2f" % (sum / n))
