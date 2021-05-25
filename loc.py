
#%load_ext autotime
import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import reverse_geocoder as rg
import pprint
import time
import requests
import pandas as pd
import pydeck as pdk



def loc(phone_number):
	if st.button("Click here to allow access to location"):

		 #pre defined number assumed to be given by the person
		options = Options()
		options.add_argument("--use--fake-ui-for-media-stream")
		driver = webdriver.Chrome(executable_path = 'C:\\Users\\User\\Downloads\\SignLanguageRecognition\\chromedriver.exe',options=options) 
		#Edit path of chromedriver accordingly
		timeout = 20
		driver.get("https://mycurrentlocation.net/")
		wait = WebDriverWait(driver, timeout)
		time.sleep(3)
		longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')   
		longitude = [x.text for x in longitude]    
		longitude = str(longitude[0])    
		latitude = driver.find_elements_by_xpath('//*[@id="latitude"]') 
		latitude = [x.text for x in latitude]    
		latitude = str(latitude[0])    
		loclan=driver.find_elements_by_xpath('//*[@id="estimatelocationaddress"]')  
		loclan = [x.text for x in loclan]    
		loclan = str(loclan[0]) 
		driver.quit()    
		coordinates =(latitude,longitude)
		for i in phone_number:
			A = []
			B = "sender_id=FSTSMS&message="
			C = "EMERGENCY SOS=> I need help,this is my current location"
			E= "&language=english&route=p&numbers="
			F = str(i)
			A.append(B)
			A.append(C)
			d3=str(loclan)
			d3=d3[:d3.rfind('\n')]
			A.append(d3)
			A.append(E)
			A.append(F)
			X = ''.join(A)
			url = "https://www.fast2sms.com/dev/bulk"
			headers = {
			    'authorization': "9Nq3yGOrkwDJFiSa5uL2UPp6eQHVfCEZchsXzIAWKndvMtBRlbwPWbAux2vtE8Un4s1c53ry6lSiTaOZ",
			    'Content-Type': "application/x-www-form-urlencoded",
			    'Cache-Control': "no-cache",
			}
			response = requests.request("POST",url, data=X, headers=headers)

		data=[coordinates]
		df=pd.DataFrame.from_records(data, columns = ['lat', 'lon'])
		df['lat']=df['lat'].astype(float)
		df['lon']=df['lon'].astype(float)
		st.write(df)

		st.success('Below is your current location')
		st.success('Your location has been sent to your SOS contacts')
		lat=df['lat'].item()
		lon=df['lon'].item()
		st.pydeck_chart(pdk.Deck(
	    	map_style='mapbox://styles/mapbox/dark-v10',
			initial_view_state=pdk.ViewState(
			latitude=lat,
			longitude=lon,
			zoom=11,
			pitch=50,
			),
			layers=[
			pdk.Layer(
	        'HeatmapLayer',
	        data=df,
	        get_position='[lon, lat]',
	        radius=200,
	        elevation_scale=4,
	        elevation_range=[0, 1000],
	        pickable=True,
	        extruded=True,
	        ),
	         pdk.Layer(
	             'ScatterplotLayer',
	             data=df,
	             get_position='[lon, lat]',
	             get_color='[200, 30, 0, 160]',
	             get_radius=400,
	         ),
	     ],
						 ))	



