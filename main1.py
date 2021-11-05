import streamlit as st
import pandas as pd
import subprocess
from PIL import Image


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


global img
def main():
	"""Simple Login App"""
	img = Image.open("image/data.jpg")
	st.title("Visualization App For BI")
	st.sidebar.title("Menu")

	menu = ["Home","Login","SignUp"]
 
	choice = st.sidebar.selectbox("Select",menu,key='1')
     

	if choice == "Home":
		st.header("Home")
		st.subheader("About Visualization")
		st.markdown("Data visualization is the graphical representation of information and data. By using visual elements like charts,graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.")
		st.image(img,width = 800)
       
        
        
	elif choice == "Login":
		st.subheader("Login Section")

		username = st.text_input("User Name")
		password = st.text_input("Password",type='password')
		
		if st.button("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				st.write("Data Visualization App opens in new tab please wait")
				
				subprocess.Popen(["streamlit", "run", "ex5.py"])


			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Create Password",type='password')
		confirm_password = st.text_input("Confirm Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password),make_hashes(confirm_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()
    
