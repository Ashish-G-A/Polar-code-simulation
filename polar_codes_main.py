import encoder
import sc_decoder
import channel
import random
import numpy as np
import matplotlib.pyplot as plt


def sc_main(N, k, total_message_bits, snr):
    error = 0
    for _ in range(total_message_bits // k):
        message = [random.randint(0, 1) for _ in range(k)]
        code, channel_states = encoder.encoder(message, N, k)
        channel_input = channel.bpsk(code)
        n0 = (10 ** (- 0.1 * snr))
        channel_output = channel.AWGN(channel_input, n0)
        recieved_message = []
        sc_decoder.decoder(channel_output, channel_states, recieved_message, N)
        # print(f'message = {message}')
        # print(f'recieved message = {recieved_message}')
        # if message == recieved_message:
        #     print('yes')
        # else:
        #     print(f'message = {message}')
        #     print(f'recieved message = {recieved_message}')
        if recieved_message != message:
            for i in range(k):
                if recieved_message[i] != message[i]:
                    error += 1
            
    return error / total_message_bits


N, k = 256, 128
total_message_bits = k * 500
# print(sc_main(N, k, total_message_bits, 3))

snr_arr = np.arange(1, 5, 1.0)
ber_arr = np.zeros_like(snr_arr)

for i, el in enumerate(snr_arr):
    ber_arr[i] = sc_main(N, k, total_message_bits, el)

# print(ber_arr)


'''plotting'''

plt.plot(snr_arr, ber_arr)
plt.yscale('log')
plt.axis([1, 5, 0.001, 1])
plt.ylabel('BER')
plt.xlabel('Eb/N0 (dB)')
plt.title(f'BER vs SNR  SC ({N}, {k})')
plt.show()


#################   timeit code   ####################

# a = [-1] * 128
# b = [1] * 128
# print(timeit.timeit("g(a, b, 126)", setup="from __main__ import g, a, b", number=62500))