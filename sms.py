import requests
import random
import streamlit as st
def msg():
	ph=st.text_input("Enter your registered phone number")
	ph=int(ph)
	S = random.randint(100000,1000000)
	sp = str(S)
	A = []
	B = "sender_id=FSTSMS&message="
	C = "Your OTP is #"
	D = "&language=english&route=p&numbers="
	E = str(ph)
	A.append(B)
	A.append(C)
	A.append(sp)
	A.append(D)
	A.append(E)
	X = ''.join(A)
	url = "https://www.fast2sms.com/dev/bulk"
	headers = {
	'authorization': "m4ZXAwltQrbEKR3jd2hIOnUF9gp6qP1CsLf70zH5u8NTcvxaDJ9rstiGh8muJzV6CyDAp5k3F0Zcgx7W",
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=X, headers=headers)

	r = requests.get('https://docs.google.com/spreadsheets/d/1gyxlNyIpuSOkNrj_IEnVdxDJ9bw7VTu-_mexPGqCDEs/export?format=csv&id=1gyxlNyIpuSOkNrj_IEnVdxDJ9bw7VTu-_mexPGqCDEs&gid=895350126')
	data = r.content
	df = pd.read_csv(BytesIO(data),error_bad_lines=False)
	rslt_df=df.loc[df['Phone_Number']==ph]
	a=rslt_df['Phone_Number']
	if a.item()==ph:
		pwd=st.text_input("Enter the OTP")
		if S==pwd:
			st.write('Successfully logged in')

	else:
		st.warning("This phone number is not registered.If you are new to this app,please sign up")


	


