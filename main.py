from flask import *  

import pandas as pd
import numpy as np
import os

import pickle
import cv2
import glob
#import tensorflow as tf
from keras.models import load_model
from random import randint

height = 240
width = 256
dim = (width, height)


IMAGE_FOLDER = 'static/'

app = Flask(__name__)  
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')  
def upload():
	return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])
def success():
	if request.method == 'POST':
		f = request.files['file']
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
		full_filename = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
		image_ext = cv2.imread(full_filename)
		initial_image = np.copy(image_ext)
		imag = cv2.resize(initial_image, dim, interpolation = cv2.INTER_AREA)
		model = load_model("model.h5")
		imag = np.expand_dims(imag, axis=0)
		pred = model.predict(imag)
		pred_0 = pred[0][0]
		pred_1 = pred[0][1]
		pred_2 = pred[0][2]
		pred_3 = pred[0][3]
		pred_4 = pred[0][4]
		value = max(pred_0, pred_1, pred_2, pred_3, pred_4)
		if(value==pred_0):
			txt = "Ajoba Temple, Goa"
			desc = "Located at the entrance of Keri (or Querim) beach in Goa. It is a small temple but quite interesting on the sands of the beach. Keri beach is the northernmost beach of Goa. Thereafter Goa ends and Maharastra starts."
			made = "A beautiful temple painted in turquoise and orange, located on the shores of Keri beach in Pernem. The much-famed jatra of Ajoba devasthan at Keri-Pernem happens in the first week of February. Devotees from Goa and neighbouring states, throng to the temple to witness this."
		elif(value==pred_1):
			txt = "Shanta Durga Temple, Goa"
			desc = "Shri Shantadurga Temple is a Private temple complex belonging to Goud Saraswat Brahmin community. It is 30 km from Panaji at the foothill of Kavalem village in Ponda Taluka, Goa, India. H.H.Shrimad Swamiji of ShriKavale Math is Spiritual head Of Shree Shantadurga Saunsthan, Kavale."
			made = "Located at the foothills of Kavlem village in Ponda district of Goa, the Shree Shantadurga temple is one of the popular pilgrimage centers in Goa. The temple was initially located at Cavelossim but when it was being destroyed by the Portuguese in 1564, the deity was shifted to Kavlem. A small laterite mud shrine was built and the deity was installed here and was converted into a beautiful temple in the next few years."
		elif(value==pred_2):
			txt = "Aguada Fort, Goa"
			desc = "Fort Aguada is a well-preserved seventeenth-century Portuguese fort, along with a lighthouse, standing in Goa, India, on Sinquerim Beach, overlooking the Arabian Sea."
			made = "The old Portuguese lighthouse, which stands in the middle of Fort Aguada, was built in 1864 and once housed the great bell from the Church of St Augustine in Old Goa, before it was moved to the Church of Our Lady of the Immaculate Conception in Panaji. It’s the oldest of its sort in Asia, but is usually not open to the public."
		elif(value==pred_3):
			txt = "Our Lady of the Immaculate Conception Church, Goa"
			desc = "The Our Lady of the Immaculate Conception Church is located in Panjim, Goa, India. The Church conducts mass every day in English, Konkani, and Portuguese. The colonial Portuguese Baroque style church was first built in 1541 as a chapel on a hill side overlooking the city of Panjim."
			made = "Not all of Goa’s ancient churches are concentrated in Velha Goa. A notable exception is the Our Lady of Immaculate Conception Church which is located in Panjim. True to its name, the façade of this church is painted an immaculate, sparkling white. To the untrained eye, this might even believe the actual age and antiquity of this church that goes back to 500+ years."
		elif(value==pred_4):
			txt = "Viceroys Arch, Goa"
			desc = "Brick & stone archway dating to 16th century, built over a road leading from river to town."
			
		final_text = 'Results after Detecting Monument in Input Image'
		return render_template("success.html", name = final_text, img = full_filename, out_1 = txt, out_2 = desc, out_3 = made)
		

@app.route('/info', methods = ['POST'])  
def info():
	return render_template("info.html")  


if __name__ == '__main__':  
	app.run(host="127.0.0.1",port=8080,debug=True)  






