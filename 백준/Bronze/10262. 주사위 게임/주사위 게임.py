G_a1, G_b1, G_a2, G_b2 = map(int, input().split())
E_a1, E_b1, E_a2, E_b2 = map(int, input().split())
Ga, Gb = G_a1+G_a2, G_b1+G_b2
Ea , Eb = E_a1+E_a2 , E_b1+E_b2
if Ga-Ea + Gb-Eb == 0:
    print("Tie")
elif Ga-Ea + Gb-Eb > 0:
    print("Gunnar")
else:
    print("Emma")