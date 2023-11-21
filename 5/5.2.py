import numpy as np
import matplotlib.pyplot as plt

def daniell_spectrum(data, length, window_width):

    n_segments = length // window_width
    spectra = np.zeros((n_segments, length))

    for i in range(n_segments): 
        start = i * window_width 
        end = start + window_width 
        window = np.hanning(window_width) 
        segment = data[start:end] * window 
        spectrum = np.abs(np.fft.fft(segment)) ** 2 
        
        spectra[i, start:end] = spectrum 

  
    averaged_spectrum = np.mean(spectra, axis=0)


    return averaged_spectrum


data = np.loadtxt('lfp.txt')


spectrum = daniell_spectrum(data, len(data), 256)



plt.plot(spectrum)
plt.xlabel('Частота')
plt.ylabel('Мощность')
plt.show()

