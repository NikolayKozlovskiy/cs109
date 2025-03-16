import numpy as np

PATH_TO_DATA = '...'
bats = np.genfromtxt(PATH_TO_DATA, delimiter=',', names=None, dtype=bool)

t_column =  bats[:, 5]
gen_dict = {i:bats[:,i] for i in range(0,5)}
num_rows = bats.shape[0]

# part a
t_prob = np.sum(t_column)/num_rows
print(f'P(T) = {t_prob}')

# part b, c, d, and f
total_num_of_expressed_genes = 0
for i, gen_col in enumerate(gen_dict.values()):
    num_bats_with_gen = np.sum(gen_col)
    total_num_of_expressed_genes += num_bats_with_gen
    gen_prob = num_bats_with_gen /num_rows
    print(f'P(G_{i+1})={gen_prob}\n')

    prob_t_and_g = np.sum(gen_col * t_column) /num_rows
    prob_t_mult_g = t_prob * gen_prob
    print(f'P(T and G_{i+1}) = {prob_t_and_g}')
    print(f'P(T) * P(G_{i+1}) = {prob_t_mult_g}')

    if prob_t_and_g == prob_t_mult_g:
        print(f'G_{i+1} and T are independent')
    else:
        # G_1 and G_2 have really low influence on T, the difference between prob_t_and_g and prob_t_mult_g is due to rounding errors
        # maybe better to round to 2 decimal places
        print(f'G_{i+1} and T are dependent')
        print(f'P(T|G_{i+1}) = {prob_t_and_g/gen_prob}')
    print('\n')

    # INTERPRETATION
    # all genes increase the probability of T, but G_1 and G_2 have the lowest influence on T (I would say even neglectable)
    # G_3 and G_5 have the highest influence on T 

# I hope that I correclty interpreted the task description, the LLMs told me that 
# E[K] is the expected number of expressed genes in a bat on average
print(f'E[K] = {total_num_of_expressed_genes/num_rows}')

# part e, tried to be a hero, 
# but didn't find any conditinal independence between T and some G, conditioned on another G
# but there are still plenty of conditional independencies to check - be above and beyond
for i, gen_1 in enumerate(gen_dict.values()):
    print(f'Codnitioning on G_{i+1}')
    for j, gen_2 in enumerate(gen_dict.values()):
        if i != j:

            t_given_gen_1_prob = t_column[gen_1].sum() / num_rows
            gen_2_given_gen_1_prob = gen_2[gen_1].sum() / num_rows
            t_mult_gen_2_given_gen_1_prob = t_given_gen_1_prob * gen_2_given_gen_1_prob

            t_and_gen_2_given_gen_1_prob = np.all(bats[gen_1][:, [5, j]], axis=1).sum() / num_rows

            print(f"P(T|G_{i+1}) * P(G_{j+1}|G_{i+1}) = {t_mult_gen_2_given_gen_1_prob}")
            print(f"P(T, G_{j+1}|G_{i+1}) = {t_and_gen_2_given_gen_1_prob}")

            if t_mult_gen_2_given_gen_1_prob == t_and_gen_2_given_gen_1_prob:
                print(f'G_{j+1} and T are independent given G_{i+1}')
            
            print("\n")
    print("\n")


if __name__ == "__main__":
    pass