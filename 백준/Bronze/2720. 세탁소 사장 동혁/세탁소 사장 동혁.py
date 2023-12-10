N = int(input())
Q = 25
D = 10
Ni = 5
Pen = 1
for _ in range(N):
    C = int(input())
    Q_out = C//Q
    left = C%Q
    D_out = left//D
    left = left%D
    Ni_out = left//Ni
    left = left%Ni
    Pen_out = left//Pen
    print(Q_out, D_out, Ni_out, Pen_out)