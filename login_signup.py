import streamlit as st
import pandas as pd
import sqlite3 

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
conn = sqlite3.connect('data12.db', check_same_thread=False)
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT, contact1 INTEGER,contact2 INTEGER,contact3 INTEGER)')


def add_userdata(username,password,contact1,contact2,contact3):
	c.execute('INSERT INTO userstable(username,password,contact1,contact2,contact3) VALUES (?,?,?,?,?) ' ,(username,password,contact1,contact2,contact3))
	c.execute('')
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def view(username,password):
	c.execute('SELECT contact1,contact2,contact3 FROM userstable WHERE username=? AND password = ?',(username,password))
	data = c.fetchall()
	return data



		
