def approximate_pi(n_terms):
    pi_final = 0
    for i in range(n_terms):
        pi_1 = (-1**i)/(2*i+1)
        pi_final += pi_1
    return (pi_final * 4)
