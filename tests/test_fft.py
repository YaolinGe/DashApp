import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Parameters
fs = 1000  # Sampling frequency in Hz
t = np.arange(0, 1, 1/fs)  # Time vector of 1 second

# Frequencies for the example signals
frequencies = [5, 50, 120]  # Hz

# Generate signals with different frequencies and add some noise
signals = []
for f in frequencies:
    signal = np.sin(2 * np.pi * f * t) + np.random.normal(0, 0.5, len(t))
    signals.append(signal)

# FFT analysis
fft_results = []
for signal in signals:
    fft_result = fft(signal)
    fft_results.append(fft_result)

# Frequency bins
freq = np.linspace(0, fs, len(t))

# Plotting
fig, axs = plt.subplots(2, len(signals), figsize=(15, 6))

for i in range(len(signals)):
    # Time-domain signal
    axs[0, i].plot(t, signals[i])
    axs[0, i].set_title(f'Signal with Dominant Frequency {frequencies[i]} Hz')
    axs[0, i].set_xlabel('Time [s]')
    axs[0, i].set_ylabel('Amplitude')

    # Frequency-domain signal
    axs[1, i].plot(freq[:len(t)//2], np.abs(fft_results[i])[:len(t)//2] * 1/len(t))  # Normalize
    axs[1, i].set_title(f'FFT of Signal {i+1}')
    axs[1, i].set_xlabel('Frequency [Hz]')
    axs[1, i].set_ylabel('Amplitude')

plt.tight_layout()
plt.show()










#%%

import numpy as np
import matplotlib.pyplot as plt
import timeit
from numpy.fft import fft as np_fft
from scipy.fft import fft as scipy_fft

# Parameters
fs = 1000  # Sampling frequency in Hz
t = np.arange(0, 1, 1/fs)  # Time vector of 1 second

# Frequencies for the example signals
frequencies = [5, 50, 120]  # Hz

# Generate signals with different frequencies and add some noise
signals = [np.sin(2 * np.pi * f * t) + np.random.normal(0, 0.5, len(t)) for f in frequencies]

# Define functions for performance comparison
def np_fft_func():
    [np_fft(signal) for signal in signals]

def scipy_fft_func():
    [scipy_fft(signal) for signal in signals]

# Measure performance
np_fft_time = timeit.timeit(np_fft_func, number=100)
scipy_fft_time = timeit.timeit(scipy_fft_func, number=100)

print(f"NumPy FFT Time: {np_fft_time} seconds")
print(f"SciPy FFT Time: {scipy_fft_time} seconds")

# Continue with plotting using whichever FFT you prefer
# Example: Plotting the first signal and its FFT using numpy
signal = signals[0]
fft_result = np_fft(signal)
freq = np.fft.fftfreq(t.shape[-1], 1/fs)

plt.figure(figsize=(12, 6))

# Time-domain plot
plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.title('Time Domain Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Frequency-domain plot
plt.subplot(1, 2, 2)
plt.plot(freq[:len(t)//2], np.abs(fft_result)[:len(t)//2] * 1/len(t))  # Normalize
plt.title('FFT of the Signal')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

