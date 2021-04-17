import numpy as np

def bpsk(arr):
    out = []
    for i in arr:
        out.append(-1 if i == 1 else 1)
    
    return out

def AWGN(arr, n0):
    out = np.zeros_like(arr)
    out = None
    sd = np.sqrt(n0 / 2)
    noise = np.random.normal(0, sd, size= np.shape(out))
    out = arr + noise
    return list(out)

# a = [1,1,0,0,1,0,1,0]
# b = bpsk(a)
# print(a)
# n0 = 0.5 * (10 ** (- 0.1))
# c = AWGN(b, n0)
# print(c)
