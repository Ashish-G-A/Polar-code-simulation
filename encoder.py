import json

def polar_transform(code, length):
    if length == 2:
        return ((code[0] ^ code[1]) << 1) | code[1]
    
    a = polar_transform(code[ : length // 2], length // 2)
    b = polar_transform(code[length // 2 : ], length // 2)
    r = length // 2
    return ((a ^ b) << r) | b

def channel_states(reliablility_sequence, N, k):
	out = [False] * N
	for i in reliablility_sequence[N - k : ]:
		out[i] = True
	return out


def encoder(message, N, k):
	with open('d:/DOCS/4 TH YEAR PROJECT/New folder/reliability sequence.json') as f:
		arr = json.load(f)

	reliablility_sequence = []
	for x in arr:
		if x < N:
			reliablility_sequence.append(x)

	code = [0]	* N
	pointer = 0
	seq = reliablility_sequence[N - k : ]
	seq.sort()
	for i in seq:
		code[i] = message[pointer]
		pointer += 1

	output = polar_transform(code, N)
	output = bin(output)[2 : ]
	if len(output) < N:
		output = '0' * (N - len(output)) + output

	output = [int(x) for x in output]

	return output, channel_states(reliablility_sequence, N, k)


# message = [0,0,1,0,0,1,0,0]
# N, k = 16, 8
# a = encoder(message, N, k)
# print(a)