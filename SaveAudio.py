# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 08:41:32 2022

@author: Sumit
"""

from gtts import gTTS

def save_audio(page_context, filename, i_lang):
    output= gTTS(text= page_context, lang= i_lang)
    filename= 'audio/' + filename+ '_' + i_lang + '.mp3'
    output.save(filename)