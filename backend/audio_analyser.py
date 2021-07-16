import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import librosa, librosa.display
import numpy as np


def get_plots(file):
	# URLs array
	plot_url = []

	# load audio file with Librosa
	signal, sample_rate = librosa.load(file, sr=22050)


	# ======================== WAVEFORM
	img = BytesIO()
	librosa.display.waveplot(signal, sample_rate, alpha=0.4)
	plt.xlabel("Time (s)")
	plt.ylabel("Amplitude")
	plt.title("Waveform")
	plt.savefig(img, format='png')
	plt.close()
	img.seek(0)
	plot_url.append(base64.b64encode(img.getvalue()).decode('utf8'))



	# ======================== Power Spectrum
	# FFT -> power spectrum
	# perform Fourier transform
	fft = np.fft.fft(signal)

	# calculate abs values on complex numbers to get magnitude
	spectrum = np.abs(fft)

	# create frequency variable
	f = np.linspace(0, sample_rate, len(spectrum))

	# take half of the spectrum and frequency
	left_spectrum = spectrum[:int(len(spectrum)/2)]
	left_f = f[:int(len(spectrum)/2)]

	# plot spectrum
	img = BytesIO()
	plt.plot(left_f, left_spectrum, alpha=0.4)
	plt.xlabel("Frequency")
	plt.ylabel("Magnitude")
	plt.title("Power spectrum")
	plt.savefig(img, format='png')
	plt.close()
	img.seek(0)
	plot_url.append(base64.b64encode(img.getvalue()).decode('utf8'))




	# ======================== Spectrogram
	# STFT -> spectrogram
	hop_length = 512 # in num. of samples
	n_fft = 2048 # window in num. of samples

	# calculate duration hop length and window in seconds
	hop_length_duration = float(hop_length)/sample_rate
	n_fft_duration = float(n_fft)/sample_rate

	# perform stft
	stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length)

	# calculate abs values on complex numbers to get magnitude
	spectrogram = np.abs(stft)

	# display spectrogram
	img = BytesIO()
	librosa.display.specshow(spectrogram, sr=sample_rate, hop_length=hop_length)
	plt.xlabel("Time")
	plt.ylabel("Frequency")
	plt.colorbar()
	plt.title("Spectrogram")
	plt.savefig(img, format='png')
	plt.close()
	img.seek(0)
	plot_url.append(base64.b64encode(img.getvalue()).decode('utf8'))





	# ======================== Spectrogram (dB)
	# apply logarithm to cast amplitude to Decibels
	log_spectrogram = librosa.amplitude_to_db(spectrogram)

	img = BytesIO()
	librosa.display.specshow(log_spectrogram, sr=sample_rate, hop_length=hop_length)
	plt.xlabel("Time")
	plt.ylabel("Frequency")
	plt.colorbar(format="%+2.0f dB")
	plt.title("Spectrogram (dB)")
	plt.savefig(img, format='png')
	plt.close()
	img.seek(0)
	plot_url.append(base64.b64encode(img.getvalue()).decode('utf8'))




	# ========================  MFCC
	# MFCCs
	# extract 13 MFCCs
	MFCCs = librosa.feature.mfcc(signal, sample_rate, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)

	# display MFCCs
	img = BytesIO()
	librosa.display.specshow(MFCCs, sr=sample_rate, hop_length=hop_length)
	plt.xlabel("Time")
	plt.ylabel("MFCC coefficients")
	plt.colorbar()
	plt.title("MFCCs")
	plt.savefig(img, format='png')
	plt.close()
	img.seek(0)
	plot_url.append(base64.b64encode(img.getvalue()).decode('utf8'))



	return plot_url
