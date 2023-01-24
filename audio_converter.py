import matplotlib.pyplot as plt
import librosa
import numpy as np
import sounddevice as sd

# carica il file audio a 10000 Hz
data, rate = librosa.load("test.wav", sr=10000)


# verifico che l'audio riprodotto sia fedele all'originale
sd.play(data, rate)


# normalizzo i valori compresi tra [-1, 1] nell'intervallo [0, 1023]
data = np.interp(data, (data.min(), data.max()), (0, 1023))


data = np.round(data)


# trasformo in interi i valori dell'array
data = data.astype(int)


# crea una stringa vuota
output = "uint16_t array[{}] = {{".format(len(data))
output += ", ".join(str(i) for i in data)
output += "}"
print(output)

print(rate)



# crea il primo sottoplot
plt.subplot(1, 2, 1)
plt.plot(np.linspace(0, len(data)/rate, num=len(data)), data)
plt.xlabel("Tempo(s)")
plt.ylabel("Ampiezze")
plt.title("Campionamento a 10 kHz")

# carica il file audio con la frequenza di campionamento originale
data, rate = librosa.load("test.wav", sr=None)

# crea il secondo sottoplot
plt.subplot(1, 2, 2)
plt.plot(np.linspace(0, len(data)/rate, num=len(data)), data)
plt.xlabel("Tempo(s)")
plt.ylabel("Ampiezze")
plt.title("Campionamento originale")

# mostra la figura
plt.show()

