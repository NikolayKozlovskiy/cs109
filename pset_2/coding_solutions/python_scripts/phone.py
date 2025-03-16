import numpy  as np

PATH_TO_PRIOR = '...'
PATH_TO_CONDITIONAL = '...'

OUTPUT_PATH = './updated_loc_probs.txt'

prior = np.genfromtxt(PATH_TO_PRIOR, delimiter=',', names=None, dtype=float)
conditional = np.genfromtxt(PATH_TO_CONDITIONAL, delimiter=',', names=None, dtype=float)

# the generalised law of total probability
prob_of_observe = (prior * conditional).sum()

updated_loc_probs = np.zeros(prior.shape)

for row in range(prior.shape[0]):
    for col in range(prior.shape[1]):
        prob_loc_given_observe = (conditional[row, col] * prior[row, col]) / prob_of_observe
        updated_loc_probs[row, col] = prob_loc_given_observe

np.savetxt(OUTPUT_PATH, updated_loc_probs, delimiter=",", fmt="%1.3f")

if __name__ == '__main__':
    pass