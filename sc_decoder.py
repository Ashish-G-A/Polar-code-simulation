# def f(arr, l):
# 	out = []
# 	l = l // 2
# 	for i in range(0, l):
# 		a = arr[i]
# 		b = arr[i + l]
# 		sign = lambda x : 1 if x >0 else -1 if x < 0 else 0
# 		out.append(min(abs(a), abs(b)) * sign(a) * sign(b))

# 	return out

def f(arr, l):
	out = []
	l = l // 2
	# sign = lambda x : 1 if x >0 else -1 if x < 0 else 0
	for i in range(0, l):
		a = arr[i]
		b = arr[i + l]
		sn_a = 1
		sn_b = 1
		if a < 0:
			a = -a
			sn_a = -1
		if b < 0:
			b = -b
			sn_b = -1

		mini = b
		if a < b:
			mini = a

		out.append(mini * sn_a * sn_b)
	return out


def g(arr, bit_arr, l):
	out = []
	l = l // 2
	for i in range(0, l):
		a = arr[i]
		b = arr[i + l]
		c = bit_arr[i]
		out.append(b + ((1 - 2 * c) * a))

	return out



def up(a, b):
	c = []
	for i in range(len(a)):
		c.append(a[i] ^ b[i])
	c.extend(b)
	return c



def decoder(r, channel_states, decoded_message, l):
	# l = len(r)

	if l == 1:
		if channel_states[0]:
			if r[0] >= 0:
				decoded_message.append(0)
				channel_states.pop(0)
				return [0]
			else:
				decoded_message.append(1)
				channel_states.pop(0)
				return [1]
		else:
			channel_states.pop(0)
			return [0]

	
	a = decoder(f(r, l), channel_states, decoded_message, l // 2)
	b = decoder(g(r, a, l), channel_states, decoded_message, l // 2)
	return up(a, b)


#############################################################

# channel_states = [0, 0, 0, 1, 0, 1, 1, 1]
# decoded_message = []



# x_arr = [0, 1, 1, 0, 1, 0, 0 ,1]
# bpsk = [1, -1, -1, 1, -1, 1, 1, -1]
# abc = decoder(bpsk, channel_states, decoded_message)
# print(abc)
# print(decoded_message)

