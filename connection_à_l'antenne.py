# paramètres globaux
RATE = 1024000
FREQ = 95100000
# importer la librairie du module SDR
from rtlsdr import RtlSdr
import wavio
import numpy as np

# créer un objet connecté au module SDR
sdr = RtlSdr()
sdr.sample_rate = RATE
sdr.center_freq = FREQ
sdr.gain = 'auto'
# enregistrer des échantillons I/Q en nombres complexes
samples = sdr.read_samples(RATE*10)
sdr.close()
# graphique de la densité spectrale de puissance
import matplotlib.pyplot as plt
# psd = Power Spectral Density
plt.psd(samples, NFFT=2 ** 14, Fs=RATE / 1e6, Fc=FREQ / 1e6)
plt.show()


duréeEnregistrement=10
rafraichissement=44100

phase=np.arctan(samples.imag/samples.real)



# wavio.write('test.wav',samples.real,RATE,sampwidth=2)
