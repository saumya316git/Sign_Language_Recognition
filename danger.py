import pygame
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
def danger():
	path = "C:\\Users\\User\\Downloads\\SignLanguageRecognition\\images\\danger.png"
	image1 = Image.open(path)

	for i in range(1): # number of rows in your table! = 2 
		cols=st.beta_columns(3) # number of columns in each row! = 2 # first column of the ith row 
		cols[0].write("",use_column_width=True)
		cols[1].image(image1,use_column_width=True)
		cols[2].write("",use_column_width=True)
	for i in range(1): # number of rows in your table! = 2 
		cols=st.beta_columns(9) # number of columns in each row! = 2 # first column of the ith row 
		cols[0].write("",use_column_width=True)
		cols[1].write("",use_column_width=True)
		cols[2].write("",use_column_width=True)
		cols[3].write("",use_column_width=True)
		if cols[4].button('START',help="Click here to start the alarm"):
			pygame.init()
			mp3='videos\\danger.mp3'
			pygame.mixer.music.load(mp3) #Loading File Into Mixer
			pygame.mixer.music.play() #Playing It In The Whole Device
		cols[5].write("",use_column_width=True)
		cols[6].write("",use_column_width=True)
		cols[7].write("",use_column_width=True)
	for i in range(1): # number of rows in your table! = 2 
		cols=st.beta_columns(9) # number of columns in each row! = 2 # first column of the ith row 
		cols[0].write(" ",use_column_width=True)
		cols[1].write(" ",use_column_width=True)
		cols[2].write(" ",use_column_width=True)
		cols[3].write(" ",use_column_width=True)
		if cols[4].button('STOP',help="Click here to stop the alarm"):

			pygame.mixer.music.stop()
		cols[2].write(" ",use_column_width=True)