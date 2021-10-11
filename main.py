import wave
import math
import struct

samplerate = 44100
frequency = 440.0
amplitude = 0.5
duration = 30

def oscillator(frequency):
    data = []
    t = 0
    dt = 1
    while(t < (duration*samplerate)):
        theta = 2 * math.pi * t
        f = math.sin(frequency*theta/samplerate)
        data.append(f)
        t += dt
    return data

def amplitude_modulator(data):
    t = 0
    while(t < len(data)):
        data[t] *= math.cos(math.cos(t/samplerate) * 2 * math.pi * t / samplerate)**2
        t += 1
    return data

with wave.open('cake.wav', 'w') as cake:
    cake.setnchannels(1)
    cake.setsampwidth(2)
    cake.setframerate(samplerate)
    data = amplitude_modulator(oscillator(410))
    for frame in data:
        frame = int( (2**15-1)*frame )
        cake.writeframes(struct.pack('<h', frame))
    cake.close()