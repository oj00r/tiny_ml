import random
import librosa
import numpy as np
import soundfile as sf
import os

def add_white_noise(signal, noise_percentage_factor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noise_percentage_factor
    return augmented_signal

def time_stretch(signal, time_stretch_rate):
    return librosa.effects.time_stretch(signal, rate=time_stretch_rate)

def pitch_scale(signal, sr, num_semitones):
    return librosa.effects.pitch_shift(y=signal, sr=sr, n_steps=num_semitones)

def random_gain(signal, min_factor=0.1, max_factor=0.12):
    gain_rate = random.uniform(min_factor, max_factor)
    augmented_signal = signal * gain_rate
    return augmented_signal

def invert_polarity(signal):
    return signal * -1

if __name__ == "__main__":

    folder_path = os.path.join('data', 'method_2', 'ringtone')
    new_path = os.path.join('data', 'method_2', 'ringtone')

    for file in os.listdir(folder_path):
        file_name = file
        
        try:
            signal, sr = librosa.load(os.path.join(folder_path, file_name), sr =16000)
            new_name = (file_name[:-4])
            print(signal, sr)
            
            random_factor = random.uniform(0.002, 0.01)
            augmented_signal = add_white_noise(signal, random_factor)
            sf.write(f"{new_path}/{new_name}_add_white_noise.wav", augmented_signal, sr)

            # random_factor = random.uniform(1.2, 1.7)
            # augmented_signal = time_stretch(signal, 1.5)
            # sf.write(f"{new_path}/{new_name}_time_stretch.wav", augmented_signal, sr)

            random_factor = random.randint(1, 3)
            augmented_signal = pitch_scale(signal, sr, 2)
            sf.write(f"{new_path}/{new_name}_pitch_scale.wav", augmented_signal, sr)

            augmented_signal = invert_polarity(signal)
            sf.write(f"{new_path}/{new_name}_invert_polarity.wav", augmented_signal, sr)
            
            
            augmented_signal = random_gain(signal)
            sf.write(f"{new_path}/{new_name}.wav", signal, sr)
        except Exception as e:
            print(f"Error processing {file_name}: {e}")