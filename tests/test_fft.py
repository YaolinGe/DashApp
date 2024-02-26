import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

print("Hello")


# #%%

# # Parameters
# fs = 1000  # Sampling frequency in Hz
# t = np.arange(0, 1, 1/fs)  # Time vector of 1 second

# # Frequencies for the example signals
# frequencies = [5, 50, 120]  # Hz

# # Generate signals with different frequencies and add some noise
# signals = []
# for f in frequencies:
#     signal = np.sin(2 * np.pi * f * t) + np.random.normal(0, 0.5, len(t))
#     signals.append(signal)

# # FFT analysis
# fft_results = []
# for signal in signals:
#     fft_result = fft(signal)
#     fft_results.append(fft_result)

# # Frequency bins
# freq = np.linspace(0, fs, len(t))

# # Plotting
# fig, axs = plt.subplots(2, len(signals), figsize=(15, 6))

# for i in range(len(signals)):
#     # Time-domain signal
#     axs[0, i].plot(t, signals[i])
#     axs[0, i].set_title(f'Signal with Dominant Frequency {frequencies[i]} Hz')
#     axs[0, i].set_xlabel('Time [s]')
#     axs[0, i].set_ylabel('Amplitude')
    
#     # Frequency-domain signal
#     axs[1, i].plot(freq[:len(t)//2], np.abs(fft_results[i])[:len(t)//2] * 1/len(t))  # Normalize
#     axs[1, i].set_title(f'FFT of Signal {i+1}')
#     axs[1, i].set_xlabel('Frequency [Hz]')
#     axs[1, i].set_ylabel('Amplitude')

# plt.tight_layout()
# plt.show()

# # %%

