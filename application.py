import streamlit as st 
import tkinter as tk
import cv2
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import re
import os
import numpy as np
from keras.models import model_from_json
import operator
import time
import sys, os
import matplotlib.pyplot as plt
from string import ascii_uppercase
import hunspell
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
import matplotlib.pyplot as plt
import plotly_express as px
import tqdm
from tqdm._tqdm_notebook import tqdm_notebook
from selenium.webdriver.support.ui import WebDriverWait
import time
import reverse_geocoder as rg 
import pprint 
import pygame
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
import tqdm
from tqdm._tqdm_notebook import tqdm_notebook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import reverse_geocoder as rg
import pprint
import time
import requests
import pandas as pd
import pydeck as pdk
#from tkinter import messagebox
import requests
import base64
import pandas as pd
import pydeck as pdk
import time
from io import BytesIO, StringIO
import login_signup
from login_signup import create_usertable
from login_signup import make_hashes
from login_signup import check_hashes
from login_signup import add_userdata
from login_signup import login_user
from login_signup import view
from login_signup import view_all_users
from loc import loc
from danger import danger
from contactus import contact
def main():
	#st.title("Sign Language Recognition App")
	
	st.title("**Silence shines**")
	st.header('Signs are to eyes what words are to ears')
	#st.title('Signs are to eyes that words are to ears')
	 # you can use st.header() instead, too
	my_bar = st.progress(0)
	for percent_complete in range(100):

		time.sleep(0.01)
		my_bar.progress(percent_complete + 1)
	activities = ["Home","Login","SignUp"]
	choice = st.sidebar.radio("Select Activity",activities,index=0)
	if choice =='Home':
		#img=Image.open('ASL.png')
		#st.image(img,width=300)
		#st.subheader("Intelligent Gesture Recognition System for specially challenged people")
		#st.markdown("<h2 style='text-align:center; color:red;'>Intelligent Gesture Recognition System for specially challenged people</h1>", unsafe_allow_html=True)
		st.write(" ")
		st.write(" ")
		st.info("**PURPOSE**")
		
		st.info("**In order to lower the barrier and to enable dynamic communication,We present an ASL recognition system that uses CNN to translate signs into text. **")
		video_file = open('videos\\video.mp4', 'rb')
		video_bytes = video_file.read()
		st.video(video_bytes) 


	elif choice=='Login':
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):

			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				st.success("Logged In as {}".format(username))
				#phno=view(username,password)
				#st.write(phno)
				a=view(username,check_hashes(password,hashed_pswd))
				ph_no1=a[0][0]
				ph_no2=a[0][1]
				ph_no3=a[0][2]
				activities = ["Sign to text Translator","Emergency SOS","Danger Alarm","Let\'s get Fit","Covid-19 Guidelines","Survey"]
				choice1=st.sidebar.radio("Functionalities",activities)
				if choice1=='Sign to text Translator':
					st.warning('**PURPOSE : **To predict character,word and sentences by converting hand gesture to text')
					if st.button('Click here to allow camera access'):
						st.warning("Turning on your camera.It will take only about 10 seconds⏳.Please wait")
				       
						class Application:
						    def __init__(self):
						        
						        self.directory = 'model'
						        self.vs = cv2.VideoCapture(0)
						        self.current_image = None
						        self.current_image2 = None
						        self.hs = hunspell.Hunspell('C:\\Users\\User\\Downloads\\SignLanguageRecognition\\hunspell-1.3.2-3-w32-bin\\share\\hunspell\\en_US' ,'C:\\Users\\User\\Downloads\\SignLanguageRecognition\\hunspell-1.3.2-3-w32-bin\\share\\hunspell\\en_US.txt')
						        #                          self.hs = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')
						        self.json_file = open(self.directory+'\\'+"model-bw.json")
						        self.model_json = self.json_file.read()
						        self.json_file.close()
						        self.loaded_model = model_from_json(self.model_json)
						        self.loaded_model.load_weights(self.directory+'\\'+"model-bw.h5")

						        self.json_file_dru = open(self.directory+'\\'+"model-bw_dru.json")
						        self.model_json_dru = self.json_file_dru.read()
						        self.json_file_dru.close()
						        self.loaded_model_dru = model_from_json(self.model_json_dru)
						        self.loaded_model_dru.load_weights(self.directory+"\\"+"model-bw_dru.h5")

						        self.json_file_tkdi = open(self.directory+"\\"+"model-bw_tkdi.json" )
						        self.model_json_tkdi = self.json_file_tkdi.read()
						        self.json_file_tkdi.close()
						        self.loaded_model_tkdi = model_from_json(self.model_json_tkdi)
						        self.loaded_model_tkdi.load_weights(self.directory+"\\"+"model-bw_tkdi.h5")

						        self.json_file_smn = open(self.directory+"\\"+"model-bw_smn.json" )
						        self.model_json_smn = self.json_file_smn.read()
						        self.json_file_smn.close()
						        self.loaded_model_smn = model_from_json(self.model_json_smn)
						        self.loaded_model_smn.load_weights(self.directory+"\\"+"model-bw_smn.h5")
						        
						        self.ct = {}
						        self.ct['blank'] = 0
						        self.blank_flag = 0
						        for i in ascii_uppercase:
						            self.ct[i] = 0
						        print("Loaded model from disk")
						        self.root = tk.Tk()
						        #self.root['background']='#856ff8'
						        self.root.title("Sign language to text Translator ")
						        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
						        self.root.geometry("1000x1100")
						        self.panel = tk.Label(self.root)
						        self.panel.place(x = 135, y = 10, width = 640, height = 640)
						        self.panel2 = tk.Label(self.root) # initialize image panel
						        self.panel2.place(x = 460, y = 95, width = 310, height = 310)
						        
						        self.T = tk.Label(self.root)
						        self.T.place(x=80,y = 20)
						        self.T.config(text = "Sign Language Recognition System",font=("Times",36,"bold"))
						        self.panel3 = tk.Label(self.root) # Current SYmbol
						        self.panel3.place(x = 200,y=590)
						        self.T1 = tk.Label(self.root)
						        self.T1.place(x = 10,y = 590)
						        self.T1.config(text="Character :",font=("Courier",20,"bold"))
						        self.panel4 = tk.Label(self.root) # Word
						        self.panel4.place(x = 200,y=620)
						        self.T2 = tk.Label(self.root)
						        self.T2.place(x = 10,y = 620)
						        self.T2.config(text ="Word :",font=("Courier",20,"bold"))
						        self.panel5 = tk.Label(self.root) # Sentence
						        self.panel5.place(x = 350,y=650)
						        self.T3 = tk.Label(self.root)
						        self.T3.place(x = 10,y = 650)
						        self.T3.config(text ="Sentence :",font=("Courier",20,"bold"))

						        self.T4 = tk.Label(self.root)
						        self.T4.place(x = 250,y = 680)
						        self.T4.config(text = "Suggested Words",fg="red",font = ("Courier",20,"bold"))
						        
						        self.bt1=tk.Button(self.root, command=self.action1,height = 0,width = 0)
						        self.bt1.place(x = 26,y=710)
						        #self.bt1.grid(padx = 10, pady = 10)
						        self.bt2=tk.Button(self.root, command=self.action2,height = 0,width = 0)
						        self.bt2.place(x = 125,y=710)
						        #self.panel3.place(x = 10,y=660)
						        # self.bt2.grid(row = 4, column = 1, columnspan = 1, padx = 10, pady = 10, sticky = tk.NW)
						        self.bt3=tk.Button(self.root, command=self.action3,height = 0,width = 0)
						        self.bt3.place(x = 325,y=710)
						        # self.bt3.grid(row = 4, column = 2, columnspan = 1, padx = 10, pady = 10, sticky = tk.NW)
						        self.bt4=tk.Button(self.root, command=self.action4,height = 0,width = 0)
						        self.bt4.place(x = 425,y=710)
						        # self.bt4.grid(row = bt1, column = 0, columnspan = 1, padx = 10, pady = 10, sticky = tk.N)
						        self.bt5=tk.Button(self.root, command=self.action5,height = 0,width = 0)
						        self.bt5.place(x = 625,y=710)
						        
						     
						        self.str=""
						        self.word=""
						        self.current_symbol="Empty"
						        self.photo="Empty"
						        self.video_loop()
						    def video_loop(self):
						        
						        ok, frame = self.vs.read()
						        if ok:
						            cv2image = cv2.flip(frame, 1)
						            x1 = int(0.5*frame.shape[1])
						            y1 = 10
						            x2 = frame.shape[1]-10
						            y2 = int(0.5*frame.shape[1])
						            cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
						            cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)
						            self.current_image = Image.fromarray(cv2image)
						            imgtk = ImageTk.PhotoImage(image=self.current_image)
						            self.panel.imgtk = imgtk
						            self.panel.config(image=imgtk)
						            cv2image = cv2image[y1:y2, x1:x2]
						            gray = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)
						            blur = cv2.GaussianBlur(gray,(5,5),2)
						            th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
						            ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
						            self.predict(res)
						            self.current_image2 = Image.fromarray(res)
						            imgtk = ImageTk.PhotoImage(image=self.current_image2)
						            self.panel2.imgtk = imgtk
						            self.panel2.config(image=imgtk)
						            self.panel3.config(text=self.current_symbol,font=("Courier",20))
						            self.panel4.config(text=self.word,font=("Courier",20))
						            self.panel5.config(text=self.str,font=("Courier",20))
						            predicts=self.hs.suggest(self.word)  
						            if(len(predicts) > 0):
						                self.bt1.config(text=predicts[0],font = ("Courier",20))
						            else:
						                self.bt1.config(text="")
						            if(len(predicts) > 1):
						                self.bt2.config(text=predicts[1],font = ("Courier",20))
						            else:
						                self.bt2.config(text="")
						            if(len(predicts) > 2):
						                self.bt3.config(text=predicts[2],font = ("Courier",20))
						            else:
						                self.bt3.config(text="")
						            if(len(predicts) > 3):
						                self.bt4.config(text=predicts[3],font = ("Courier",20))
						            else:
						                self.bt4.config(text="")
						            if(len(predicts) > 4):
						                self.bt5.config(text=predicts[4],font = ("Courier",20))
						            else:
						                self.bt5.config(text="")                
						        self.root.after(30, self.video_loop)
						        
						    
						    def predict(self,test_image):
						        test_image = cv2.resize(test_image, (128,128))
						        result = self.loaded_model.predict(test_image.reshape(1, 128, 128, 1))
						        result_dru = self.loaded_model_dru.predict(test_image.reshape(1 , 128 , 128 , 1))
						        result_tkdi = self.loaded_model_tkdi.predict(test_image.reshape(1 , 128 , 128 , 1))
						        result_smn = self.loaded_model_smn.predict(test_image.reshape(1 , 128 , 128 , 1))
						        prediction={}
						        prediction['blank'] = result[0][0]
						        inde = 1
						        for i in ascii_uppercase:
						            prediction[i] = result[0][inde]
						            inde += 1
						        #LAYER 1
						        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
						        self.current_symbol = prediction[0][0]
						        #LAYER 2
						        if(self.current_symbol == 'D' or self.current_symbol == 'R' or self.current_symbol == 'U'):
						        	prediction = {}
						        	prediction['D'] = result_dru[0][0]
						        	prediction['R'] = result_dru[0][1]
						        	prediction['U'] = result_dru[0][2]
						        	prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
						        	self.current_symbol = prediction[0][0]

						        if(self.current_symbol == 'D' or self.current_symbol == 'I' or self.current_symbol == 'K' or self.current_symbol == 'T'):
						        	prediction = {}
						        	prediction['D'] = result_tkdi[0][0]
						        	prediction['I'] = result_tkdi[0][1]
						        	prediction['K'] = result_tkdi[0][2]
						        	prediction['T'] = result_tkdi[0][3]
						        	prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
						        	self.current_symbol = prediction[0][0]

						        if(self.current_symbol == 'M' or self.current_symbol == 'N' or self.current_symbol == 'S'):
						        	prediction1 = {}
						        	prediction1['M'] = result_smn[0][0]
						        	prediction1['N'] = result_smn[0][1]
						        	prediction1['S'] = result_smn[0][2]
						        	prediction1 = sorted(prediction1.items(), key=operator.itemgetter(1), reverse=True)
						        	if(prediction1[0][0] == 'S'):
						        		self.current_symbol = prediction1[0][0]
						        	else:
						        		self.current_symbol = prediction[0][0]
						        if(self.current_symbol == 'blank'):
						            for i in ascii_uppercase:
						                self.ct[i] = 0
						        self.ct[self.current_symbol] += 1
						        if(self.ct[self.current_symbol] > 60):
						            for i in ascii_uppercase:
						                if i == self.current_symbol:
						                    continue
						                tmp = self.ct[self.current_symbol] - self.ct[i]
						                if tmp < 0:
						                    tmp *= -1
						                if tmp <= 20:
						                    self.ct['blank'] = 0
						                    for i in ascii_uppercase:
						                        self.ct[i] = 0
						                    return
						            self.ct['blank'] = 0
						            for i in ascii_uppercase:
						                self.ct[i] = 0
						            if self.current_symbol == 'blank':
						                if self.blank_flag == 0:
						                    self.blank_flag = 1
						                    if len(self.str) > 0:
						                        self.str += " "
						                    self.str += self.word
						                    self.word = ""
						            else:
						                if(len(self.str) > 16):
						                    self.str = ""
						                self.blank_flag = 0
						                self.word += self.current_symbol
						    def action1(self):
						    	predicts=self.hs.suggest(self.word)
						    	if(len(predicts) > 0):
						            self.word=""
						            self.str+=" "
						            self.str+=predicts[0]
						    def action2(self):
						    	predicts=self.hs.suggest(self.word)
						    	if(len(predicts) > 1):
						            self.word=""
						            self.str+=" "
						            self.str+=predicts[1]
						    def action3(self):
						    	predicts=self.hs.suggest(self.word)
						    	if(len(predicts) > 2):
						            self.word=""
						            self.str+=" "
						            self.str+=predicts[2]
						    def action4(self):
						    	predicts=self.hs.suggest(self.word)
						    	if(len(predicts) > 3):
						            self.word=""
						            self.str+=" "
						            self.str+=predicts[3]
						    def action5(self):
						    	predicts=self.hs.suggest(self.word)
						    	if(len(predicts) > 4):
						            self.word=""
						            self.str+=" "
						            self.str+=predicts[4]
						   
						    def destructor(self):
						        print("Closing Application...")
						        self.root.destroy()
						        self.vs.release()
						        cv2.destroyAllWindows()
						    
						    def destructor1(self):
						        print("Closing Application...")
						        self.root1.destroy()
						    def destructor2(self):
						        print("Closing Application...")
						        self.root2.destroy()
						        
						    

						    def action_call(self) :
						        
						        self.root1 = tk.Toplevel(self.root)
						        self.root1.title("About")
						        self.root1.protocol('WM_DELETE_WINDOW', self.destructor1)
						        self.root1.geometry("900x900")
						pba = Application()

						pba.root.mainloop()


				elif choice1=='Emergency SOS':
					st.warning('**PURPOSE : **To send the current location of the person in case of an emergency to his SOS contacts through sms.')

					phone_number=[ph_no1,ph_no2,ph_no3]

					loc(phone_number)
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')				
					st.warning('All India Deaf and Dumb Society **HELPLINE NUMBER**:9818099050')



						
				elif choice1=='Danger Alarm':

					
					st.warning("**PURPOSE : ** To alert the people nearby or family members in case if a person needs help. ")
					danger()


				elif choice1=='Let\'s get Fit':
					st.warning('**PURPOSE : ** This includes meditation,yoga and exercise in sign language to encourage people to stay healthy and motivated.')

					menu = ["Meditation","Exercise","Chair Yoga"]
					choice = st.selectbox("Menu",menu)

					if choice=='Meditation':
						video_file = open('videos//meditation.mp4', 'rb')
						video_bytes = video_file.read()
						st.video(video_bytes) 
					elif choice=='Exercise':
						video_file = open('videos//exercise.mp4', 'rb')
						video_bytes = video_file.read()
						st.video(video_bytes) 
					elif choice=='Chair Yoga':
						video_file = open('videos//yoga.mp4', 'rb')
						video_bytes = video_file.read()
						st.video(video_bytes) 

				elif choice1=='Covid-19 Guidelines':


					st.warning('**PURPOSE : ** This includes spreading awareness for wearing mask, social distancing and mental health.')

					menu1 = ["Masks","Social Distancing","How to take care of mental health"]
					choice = st.selectbox("Menu",menu1)

					if choice=='Masks':
						video_file = open('videos//mask.mp4', 'rb')
						video_bytes = video_file.read()
						st.video(video_bytes) 
					elif choice=='Social Distancing':
						video_file = open('videos//socialdistancing.mp4', 'rb')
						video_bytes = video_file.read()
						st.video(video_bytes) 
					elif choice=='How to take care of mental health':
						video_file = open('videos//mentalhealth.mp4', 'rb')
						video_bytes = video_file.read()
						st.video(video_bytes) 	

				elif choice1=='Survey':
					contact()


			else:
				st.warning("Incorrect Username/Password")


	elif choice=='SignUp':
		st.write("")
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')
		contact1=st.text_input("Emergency Contact 1")
		contact2=st.text_input("Emergency Contact 2")
		contact3=st.text_input("Emergency Contact 3")
		valid1=re.search('(0/91)?[7-9][0-9]{9}',contact1)
		valid2=re.search('(0/91)?[7-9][0-9]{9}',contact2)
		valid3=re.search('(0/91)?[7-9][0-9]{9}',contact3)
		if valid1!=None and valid2!=None and valid3!=None:
			if st.checkbox("Signup"):
				create_usertable()
				add_userdata(new_user,make_hashes(new_password),contact1,contact2,contact3)
				st.success("You have successfully created a New Account")
				st.info("Go to login from the main menu")
		else:
			st.warning('enter valid details')




if __name__ == '__main__':


	main()	
