# # ===================  IMPORTS  ======================
import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
from tensorflow.python.keras.backend import sparse_categorical_crossentropy
from tensorflow.python.keras.engine import input_layer, input_spec
import matplotlib.pyplot as plt
import librosa
import math
import os

import requests
import threading
import time

from process_audio import get_mfcc
from audio_analyser import get_plots



# ===================  CONSTANTS  ======================
DATASET_PATH = './assets/data.json'


# ==================== FLASK =====================

from flask import Flask, jsonify, request, send_file
app = Flask(__name__, static_url_path='/static')




@app.before_first_request
def function_to_run_only_once():

	# ===================  LOAD DATA  ======================
	with open(DATASET_PATH, 'r') as fp:
		data = json.load(fp)

	# convert list to np array
	x = np.array(data['mfcc'])
	y = np.array(data['labels'])



	# ===================  TRAIN TEST SPLIT  ======================

	#train test split
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

	#train validation split
	x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size=0.2)


	x_train = x_train[..., np.newaxis]
	x_validation = x_validation[..., np.newaxis]
	x_test = x_test[..., np.newaxis]

	test_shape = (x_train.shape[1], x_train.shape[2], x_train.shape[3])




	# ===================  BUILDING CNN  ======================

	# build model
	global model
	model = keras.Sequential()

	# 1 conv layer
	model.add(keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=test_shape))
	model.add(keras.layers.MaxPool2D((3,3), strides=(2,2), padding='same'))
	model.add(keras.layers.BatchNormalization())  

	# 2 conv layer
	model.add(keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=test_shape))
	model.add(keras.layers.MaxPool2D((3,3), strides=(2,2), padding='same'))
	model.add(keras.layers.BatchNormalization())  

	# 3 conv layer
	model.add(keras.layers.Conv2D(32, (2,2), activation='relu', input_shape=test_shape))
	model.add(keras.layers.MaxPool2D((2,2), strides=(2,2), padding='same'))
	model.add(keras.layers.BatchNormalization())  

	# flattening 3d array from model to 1d array
	model.add(keras.layers.Flatten())

	# feeding flattend array to dense layer
	model.add(keras.layers.Dense(64, activation='relu'))
	model.add(keras.layers.Dropout(0.3))

	# output layer
	model.add(keras.layers.Dense(10, activation='softmax'))

	# summary
	# print(model.summary())




	# ===================  COMPILING CNN  ======================
	optimizer = keras.optimizers.Adam(learning_rate=0.0001)
	model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])




	# ===================  TRAINING CNN  ======================
	model.fit(x_train, y_train, validation_data=(x_validation, y_validation), batch_size=32, epochs=45)



	# =======check accuracy===========
	test_error, test_accuracy = model.evaluate(x_test, y_test)
	print(f'Test accuracy is : {test_accuracy}\nTest error is : {test_error}')





# ===================  PREDICT OUTPUT  ======================

def predict_genre(audio_mfcc):

	# # convert list to np array
	mfcc = np.array(audio_mfcc['mfcc'])

	mfcc = mfcc[..., np.newaxis]
	mfcc = mfcc[0]
	mfcc = mfcc[np.newaxis, ...]

	# print(mfcc.shape)

	# predict model
	predictions = model.predict(mfcc)
	return predictions




# ===================  ROUTES ======================


# dummy route to start first request
@app.route('/')
def ok():
	return 'ok'


# Function that runs on startup and makes a request so that our model above with @before_first_request runs
def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            print('In start loop')
            try:
                r = requests.get('http://localhost:5000/')
                if r.status_code == 200:
                    print('Server started, quiting start_loop')
                    not_started = False
                print(r.status_code)
            except:
                print('Server not yet started')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()




# ========================== CNN =============================  
# returns json
@app.route('/CNN', methods=['POST'])
def predictGenre():
	res = json.loads(request.data.decode('utf-8'))
	res = res['path'][0]


	audio_mfcc = get_mfcc(res)

	predictions = predict_genre(audio_mfcc).tolist()

	return jsonify({"predictions": predictions})



# ========================== MFCC =============================  


@app.route('/MFCC', methods=['POST'])
def plot():
	res = json.loads(request.data.decode('utf-8'))
	res = res['path'][0]

	plots = get_plots(res)
	return jsonify({"plots" : plots})



# ===================  MAIN  ======================

if __name__ == '__main__':
	start_runner()
	app.run(use_reloader=False)
