# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 06:10:28 2022

@author: Sumit
"""

import streamlit as st
from streamlit_option_menu import option_menu
from datetime import date
from gtts import gTTS
from deep_translator import GoogleTranslator


st.set_page_config(layout='wide',page_title="Babuji Ki Duniya")
st.set_option('deprecation.showPyplotGlobalUse', False)


#translator = google_translator()  
i_page= option_menu(menu_title= None, 
                        options= ['Home', 'Chapters', 'Contact Us'],
                        icons=['house-door-fill', 'book-fill', 'person-lines-fill'] ,
                        default_index=0, 
                        menu_icon= 'cast', 
                        orientation= 'horizontal')


if i_page== 'Home':
    col1, col2= st.columns(2)
    i_lang=col1.selectbox("Language", ['en', 'hi', 'de'])
    
    
    col2.markdown('##')
    play_button = col2.button("Play")
    
    
    
    

    page_context='''
                                                            A Word

        All three parts on 'THE MASTER, THE MISSION AND THE METHOD' have constituted the book 'BABUJI'. 
    First part of it presented to BABUJI on 30.4.1979 deals with his life history and Mission. 
    Second part which was presented to him on 26.1.1985 explains as to how easily and effortlessly one can reach "BABUJI'S FEET". 
    The third part which is being presented to "BABUJI'S FEET" today, the 30th April 1985 at the occasion of His 86th Birth ANNIVERSARY 
    being celebrated at his birth place Shahajahanpur which would be the source of light to every soul of the universe describing the 
    'Satpad' as spoken and stated from time to time by the MASTER.

    	Further this book consists of "BABUJI'S PARISH DECLARATION" and "BABUJI'S UNIVERSE". 
    "BABUJI'S PARIS DECLARATION" indicates his future plan of Mission's work. 
    And "BABUJI'S Universe" where in religion and spirituality have been described as 
    the MASTER described which has been recorded by one of our organisers Shri U.N. Poddar, for the readers' interest. 
    	My father is very grateful to shri Raghavendra Rao and Shri Khoosalbhai Patel for their inspiring letters enabling him to compile this book.

                                            					DR. RAMESH KUMAR SAXENA, 
                                                                                RADIOLOGIST,
                                                                                RAMKRISHNA MISSION HOSPITAL,
                                                                                ITANAGAR’ARUNACHAL PRADESH.

    
    '''
   
    
    page_context = GoogleTranslator(source='en', target= i_lang).translate(page_context)
    st.text(page_context)
    
    if play_button:
        output= gTTS(text= page_context, lang= i_lang)
        filename= 'audio/' + 'a_word_'+ i_lang + '.mp3'
        output.save(filename)
        
   
    filename= 'audio/' + 'a_word_'+ i_lang + '.mp3'
    audio_file = open(filename, 'rb')
    audio_bytes = audio_file.read()
    
    col1.audio(audio_bytes, format='audio/mp3')
        
        
        
    
    