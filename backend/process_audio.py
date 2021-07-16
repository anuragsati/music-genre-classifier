import json
import os
import math
import librosa
from pathlib import Path

SAMPLE_RATE = 22050
TRACK_DURATION = 30 # 30s 
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION


def get_mfcc(DATASET_PATH, num_mfcc=13, n_fft=2048, hop_length=512, num_segments=10):
	# dictionary to store MFCCs
	data = {
		"mfcc": []
	}

	samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
	num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)

	# load audio file from DATASET_PATH
	signal, sample_rate = librosa.load(DATASET_PATH, sr=SAMPLE_RATE)

	# process all segments of audio file
	for d in range(num_segments):

		# calculate start and finish sample for current segment
		start = samples_per_segment * d
		finish = start + samples_per_segment

		# extract mfcc
		mfcc = librosa.feature.mfcc(signal[start:finish], sample_rate, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
		mfcc = mfcc.T

		# store only mfcc feature with expected number of vectors
		if len(mfcc) == num_mfcc_vectors_per_segment:
			data["mfcc"].append(mfcc.tolist())

	
	# return data 
	return data
	