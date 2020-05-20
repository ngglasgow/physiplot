import numpy as np
import scipy.signal

print('Detect peaks without any filters.')
indexes = scipy.signal.find_peaks_cwt(
    vector,
    np.arange(1, 4),
    max_distances=np.arange(1, 4)*2
)
indexes = np.array(indexes) - 1
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    np.array(indexes),
    algorithm='scipy.signal.find_peaks_cwt'
)