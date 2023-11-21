
ecg = np.loadtxt("ECG_sample_R.txt")
ref = np.loadtxt("ECG.txt")


window_size = len(ref)


ccf = np.correlate(ecg, ref, mode="same")


peaks = np.r_[True, ccf[1:] > ccf[:-1]] & np.r_[ccf[:-1] > ccf[1:], True]


plt.plot(ecg)
plt.plot(peaks, ecg[peaks], 'ro', label='R-peaks')
plt.legend()
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.title('ECG signal with R-peaks')
plt.show()


plt.plot(ccf)
plt.plot(peaks, ccf[peaks], 'ro', label='R-peaks')
plt.legend()
plt.xlabel('Sample index')
plt.ylabel('CCF')
plt.title('CCF with R-peaks')
plt.show()
