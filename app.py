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
import PlayAudio, Chapters


st.set_page_config(layout='wide',page_title="Babuji Ki Duniya")
st.set_option('deprecation.showPyplotGlobalUse', False)


#translator = google_translator()  
i_page= option_menu(menu_title= None, 
                        options= ['Home', 'Chapters', 'Contact'],
                        icons=['house-door-fill', 'book-fill', 'person-lines-fill'] ,
                        default_index=0, 
                        menu_icon= 'cast', 
                        orientation= 'horizontal')


if i_page== 'Home':
    col1, col2= st.columns(2)
    i_lang=col1.selectbox("Language", ['English', 'Hindi'])
    if i_lang== 'English':
        i_lang='en'
    elif i_lang== 'Hindi':
        i_lang='hi'
    
    
    #col2.markdown('##')
    #play_button = col2.button("Play")
    
    
    
    
    if i_lang=='en':
        page_context='''
                                  A Word
    
            All three parts on 
        'THE MASTER, THE MISSION AND THE METHOD' 
        have constituted the book 'BABUJI'. 
        First part of it presented to BABUJI on 30.4.1979 
        deals with his life history and Mission. 
        Second part which was presented to him on 26.1.1985 
        explains as to how easily and effortlessly one can 
        reach BABUJI'S FEET. 
        The third part which is being presented to 
        "BABUJI'S FEET" today, the 30th April 1985 
        at the occasion of His 86th Birth ANNIVERSARY 
        being celebrated at his birth place Shahajahanpur 
        which would be the source of light to every 
        soul of the universe describing the 
        'Satpad' as spoken and stated from 
        time to time by the MASTER.
    
        	Further this book consists of 
        "BABUJI'S PARISH DECLARATION" and 
        "BABUJI'S UNIVERSE". 
        "BABUJI'S PARIS DECLARATION" indicates 
        his future plan of Mission's work. 
        And "BABUJI'S Universe" where in religion 
        and spirituality have been described as 
        the MASTER described which has been recorded 
        by one of our organisers Shri U.N. Poddar, 
        for the readers' interest. 
        
        	My father is very grateful to 
        shri Raghavendra Rao and 
        Shri Khoosalbhai Patel for their inspiring 
        letters enabling him to compile this book.
    
                                                					
                            DR. RAMESH KUMAR SAXENA,                                                                                 
                            RADIOLOGIST,                                                                               
                            RAMKRISHNA MISSION HOSPITAL,                                                                               
                            ITANAGAR’ARUNACHAL PRADESH.
    
        
        '''
    
    
    elif i_lang=='hi':
        page_context= '''
        
                    शब्द
            
                    तीनों भाग
                'गुरु, मिशन और विधि'
                'बाबूजी' पुस्तक का गठन किया है।
                इसका पहला भाग 30.4.1979 को बाबूजी को प्रस्तुत किया गया
                उनके जीवन इतिहास और मिशन से संबंधित है।
                दूसरा भाग जो उन्हें 26.1.1985 को प्रस्तुत किया गया था
                यह बताता है कि कोई कितनी आसानी और सहजता से कर सकता है
                "बाबूजी के पैर" तक पहुंचें।
                तीसरा भाग जो प्रस्तुत किया जा रहा है
                "बाबूजी के पैर" आज, 30 अप्रैल 1985
                उनकी 86वीं जयंती के अवसर पर
                उनके जन्म स्थान शाहजहांपुर में मनाया जा रहा है
                जो सबके लिए प्रकाश का स्रोत होगा
                ब्रह्मांड की आत्मा का वर्णन
                'सतपद' जैसा बोला और कहा गया है
                समय-समय पर मास्टर द्वारा।
            
                इसके अलावा इस पुस्तक में शामिल हैं
                "बाबूजी की पैरिश घोषणा" और
                "बाबूजी का ब्रह्मांड"।
                "बाबूजी की पेरिस घोषणा" इंगित करती है
                मिशन के काम की उनकी भविष्य की योजना।
                और "बाबूजी का ब्रह्मांड" जहाँ धर्म में
                और आध्यात्मिकता के रूप में वर्णित किया गया है
                मास्टर वर्णित है जो दर्ज किया गया है
                हमारे आयोजकों में से एक श्री यूएन पोद्दार द्वारा,
                पाठकों के हित के लिए।
                
                मेरे पिता बहुत आभारी हैं
                श्री राघवेंद्र राव और
                श्री ख़ूसलभाई पटेल उनकी प्रेरणा के लिए
                पत्र उन्हें इस पुस्तक को संकलित करने में सक्षम बनाते हैं।
            
                                                        
                                    डॉ। रमेश कुमार सक्सेना,
                                    रेडियोलॉजिस्ट,
                                    रामकृष्ण मिशन अस्पताल,
                                    ईटानगर अरुणाचल प्रदेश।    
        
        
        
        
        
        '''
   
    
    #page_context = GoogleTranslator(source='en', target= i_lang).translate(page_context)
    st.text(page_context)
    
    #if play_button:
        #PlayAudio.save_audio(page_context, 'a_word', i_lang)
        
   
    #filename= 'audio/' + 'a_word_'+ i_lang + '.mp3'
    #audio_file = open(filename, 'rb')
    #audio_bytes = audio_file.read()
    audio_bytes= PlayAudio.play_sound('a_word', i_lang)
    col1.audio(audio_bytes, format='audio/mp3')
    
    
if i_page== 'Chapters':
    i_lang=st.selectbox("Language", ['English', 'Hindi'])
    if i_lang== 'English':
        i_lang='en'
    elif i_lang== 'Hindi':
        i_lang='hi'
    i_chapter= st.selectbox("Chapter", ['The Goal of life', 
                                        'Sadhna', 
                                        'Practice of medidation for beginners', 
                                        'Ten commandments of Sahaj Marg'])
    
    if i_chapter == 'The Goal of life':
        audio_bytes= PlayAudio.play_sound('goal_of_life', i_lang)
        st.audio(audio_bytes, format='audio/mp3')
        
        page_context= Chapters.chapter_goal_of_life(i_lang)
        
        st.text(page_context)
        
        # play_button = st.button("Play")
        # if play_button:
        #     PlayAudio.save_audio(page_context, 'goal_of_life', i_lang)
            
    elif i_chapter == 'Sadhna': 
        page_context= Chapters.chapter_sadhna(i_lang)
        
        audio_bytes= PlayAudio.play_sound(i_chapter, i_lang)
        st.audio(audio_bytes, format='audio/mp3')
        
        
        st.text(page_context)
        
        # play_button = st.button("Play")
        # if play_button:
        #     PlayAudio.save_audio(page_context, i_chapter, i_lang)
            
       
        
    elif i_chapter == 'Practice of medidation for beginners':
        page_context= Chapters.chapter_practiice_meditation(i_lang)
        
        audio_bytes= PlayAudio.play_sound(i_chapter, i_lang)
        st.audio(audio_bytes, format='audio/mp3')
        
        st.text(page_context)
        
        # play_button = st.button("Play")
        # if play_button:
        #     PlayAudio.save_audio(page_context, i_chapter, i_lang)
            
        
        
        
    elif i_chapter == 'Ten commandments of Sahaj Marg':
        page_context= Chapters.chapter_ten_commandments(i_lang)
        
        audio_bytes= PlayAudio.play_sound(i_chapter, i_lang)
        st.audio(audio_bytes, format='audio/mp3')
        st.text(page_context)
        
        # play_button = st.button("Play")
        # if play_button:
        #     PlayAudio.save_audio(page_context, i_chapter, i_lang)
            
        
        
        
        
        
            
        
   
    
    
    
        
        
        
    
    