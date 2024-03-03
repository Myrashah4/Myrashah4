#Write a program that generates a set of samples of a sine wave. The parameters are as follows: 
#Frequency = last 2 digits of your index number [Hz] (if it is ‘00’ then use ‘01’), Sampling Frequency = 
#48 [kHz], Acquisition time = 2 [s], Amplitude = 2. Hint – use numpy and matplotlib libraries. It should 
#be realized as a class which stores the sine wave, has a method to generate sine wave samples with 
#chosen parameters, plotting the sine wave as well as returning samples of downsampled wave. Plot 
#both sets on one figure for comparison


import numpy as np
import matplotlib.pyplot as plt

class SineWaveGenerator:
    def __init__(self):
        self.samples = None

    def generate_samples(self, frequency, sampling_frequency, acquisition_time, amplitude):
        time_points = np.arange(0, acquisition_time, 1 / sampling_frequency)
        self.samples = amplitude * np.sin(2 * np.pi * frequency * time_points)
        return self.samples

    def plot_wave(self, downsample_factor=None):
        plt.figure(figsize=(10, 6))

        plt.subplot(2, 1, 1)
        plt.plot(self.samples, label='Original Sine Wave')
        plt.title('Original Sine Wave')
        plt.xlabel('Sample Number')
        plt.ylabel('Amplitude')
        plt.legend()

        if downsample_factor:
            downsampled_samples = self.samples[::downsample_factor]

            plt.subplot(2, 1, 2)
            plt.plot(downsampled_samples, label=f'Downsampled Sine Wave (Factor {downsample_factor})')
            plt.title(f'Downsampled Sine Wave (Factor {downsample_factor})')
            plt.xlabel('Sample Number')
            plt.ylabel('Amplitude')
            plt.legend()

        plt.tight_layout()
        plt.show()

# Get user input
frequency = int(input("Enter the frequency of the sine wave [Hz]: "))
downsample_factor = int(input("Enter the downsample factor (integer): "))

# Set other parameters
sampling_frequency = 48000
acquisition_time = 2
amplitude = 2

# Create and use the SineWaveGenerator class
sine_wave_generator = SineWaveGenerator()
sine_wave_generator.generate_samples(frequency, sampling_frequency, acquisition_time, amplitude)

sine_wave_generator.plot_wave(downsample_factor=downsample_factor)
