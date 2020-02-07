alpha = [1, 2, 3]
beta = alpha  # an alias for alpha

print(alpha is beta)  # returns true bcz they have the same reference , same id

beta += [4, 5]  # extends original list with , this will also reflect in alpha

print(alpha, beta, alpha is beta)  # returns true

beta = beta + [6, 7]  # reassigns beta to beta with new list which changes beta but not alpha

print(beta is alpha, beta, alpha)
