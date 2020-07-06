#This is a QA system developed by Sai Vikas Devisetty as a part of the course work Natural Language Processing by Dr.duoduo Liao of George Mason University
#It will try to answer questions that start with Who, What, When or Where.
#please download mylogfile.txt and qa-system.py files into the same folder
#importing the required packages
import sys
import nltk
import numpy as np
import random
import string # to process standard python strings
import re, string, unicodedata
import pandas as pd
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
import wikipedia as wk
from collections import defaultdict
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only
#creating a definition to return the response
def response(user_response):
    robo_response=''
    x=0
    if(x==0) :
        robo_response = wikipedia_data(user_response)
        return robo_response
    else:
        robo_response = 'I am sorry, I dont know the answer.'
        return robo_response
#definition for wikipedia search
def wikipedia_data(input):
   reg_ex = re.search('(.*)', input)
   try:
        if reg_ex:#using regular expressions to search the question in wikipedia
            topic = reg_ex.group(1)
            ny = wk.summary(topic, sentences = 1)
            mylogfile.write("Answer "+":\n" + ny+ "\n")
            return ny
   except Exception as e:
            #To return the exception message when the program is unable to find the question in wikipedia
            exception='I am sorry, I dont know the answer.'
            mylogfile.write("Answer "+":\n" + exception+ "\n")
            print(exception)
#creating the dummy variable flag to separate the response for exit
flag=True
#creating a logfile to record the questions
mylogfile = open(sys.argv[1], "r+")
mylogfile.truncate(0)
#printing the welcome message onto console
print(" This is a QA system by Team 1. It will try to answer questions that start with Who, What, When or Where. Enter exit to leave the program.")
while(flag==True):
    #taking the input to user_response variable
    user_response = input()
    user_response_input=user_response
    user_response=user_response.lower()
    #if the user enters exit the program enters into this loop
    if(user_response!='exit'):
        #writing the question to logfile
        mylogfile.write("Question" + ":\n"+ user_response_input+ "\n")
        #printing the answer to console
        print(response(user_response))
    else:
        flag=False
        #printing the thanks message to console when the user enters exit
        print("Thank you! GoodBye")
