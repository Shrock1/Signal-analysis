
import numpy as np


transmitted_signal = np.loadtxt("UStransmitter.txt")


received_signal = np.loadtxt("USreceiver.txt")


time_difference = np.argmax(received_signal) - np.argmax(transmitted_signal)


depth = (time_difference * 5 * 10**3) / (2 * 100 * 10**6)


print("Глубина дефекта составляет", depth, "метра.")
