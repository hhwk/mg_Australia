import streamlit as st
from PIL import Image
from datetime import date, timedelta
import time
import streamlit.components.v1 as components
import json
import os
import pandas as pd
import numpy as np
money=1000
st.set_page_config(
page_title="Мировое господство",
page_icon="🥭",
layout="wide",
initial_sidebar_state="collapsed", #expanded/collapsed
menu_items={
         'Get Help': 'https://www.google.com/',
         'Report a bug': "https://www.google.com/",
         'About': "# Автор MangoVirus"
     })
menu = st.sidebar.selectbox(
     'Меню',
     ('Стартовая страница','Улучшения'))
masiv_up=[0,0,0,0]
masiv_shit=[' ',' ',' ',' ']
masiv_shit1=[0,0,0,0]
if menu=='Улучшения':
    time1=0
    st.write('Деньги:',money)

    st.write('Какие города вы хотите улучшить?')
    up = st.checkbox('Пекин')
    if up:
        masiv_up[0]+=1
        money-=200
    up1 = st.checkbox('Шанхай')
    if up1:
        masiv_up[1] += 1
        money -= 200
    up2 = st.checkbox('Гуанчжоу')
    if up2:
        masiv_up[2] += 1
        money -= 200
    up3 = st.checkbox('Гонконг')
    if up3:
        masiv_up[3] += 1
        money -= 200

    st.write('На какие города установим щиты?')
    shit = st.checkbox('Пекин ')
    if shit:
        masiv_shit[0]+='🛡️'
        masiv_shit1[0]+=1
        money-=400
    shit1 = st.checkbox('Шанхай ')
    if shit1:
        masiv_shit[1]+='🛡️'
        masiv_shit1[1] += 1
        money -= 400
    shit2 = st.checkbox('Гуанчжоу ')
    if shit2:
        masiv_shit[2]+='🛡️'
        masiv_shit1[2] += 1
        money -= 400
    shit3 = st.checkbox('Гонконг ')
    if shit3:
        masiv_shit[3]+='🛡️'
        masiv_shit1[3] += 1
        money -= 400

    number = st.number_input('Сколько ракет делаем?')
    st.write('Вы получите в следующие количество ракет', number)
    money-=500*number
    st.write('Ваш баланс после операции:', money)

    col1, col2, col3,col4= st.columns(4)
    col1.metric('🏠'+masiv_shit[0]+'Пекин','⚙️'+str(60+10*masiv_up[0])+'%'+' 🌳 '+str(72+10*masiv_up[0])+'%',masiv_up[0]*10)
    col2.metric('🏠'+masiv_shit[1]+'Шанхай','⚙️'+str(50+10*masiv_up[1])+'%'+' 🌳 '+str(54+10*masiv_up[1])+'%',masiv_up[1]*10)
    col3.metric('🏠'+masiv_shit[2]+'Гуанчжоу','⚙️'+str(50+10*masiv_up[2])+'%'+' 🌳 '+str(54+10*masiv_up[2])+'%',masiv_up[2]*10)
    col4.metric('🏠'+masiv_shit[3]+'Гонконг','⚙️'+str(40+10*masiv_up[3])+'%'+' 🌳 '+str(36+10*masiv_up[3])+'%',masiv_up[3]*10)

    if st.button('Отправить данные'):
        if money>=0:
            with st.spinner('Wait for it...'):
                with open("MG/new.txt", "w") as file:
                    file.write('Улучшения '+' Пекин: '+str(masiv_up[0])+' Шанхай: '+str(masiv_up[1])+' Гуанчжоу: '+str(masiv_up[2])+' Гонконг: '+str(masiv_up[3]))
                    file.write('\n'+'Щиты '+' Пекин: '+str(masiv_shit1[0])+' Шанхай: '+str(masiv_shit1[1])+' Гуанчжоу: '+str(masiv_shit1[2])+' Гонконг: '+str(masiv_shit1[3]))
                    file.write('\n'+'Производство ракет '+str(number))
                    file.write('\n'+'Деньги '+str(money))
                time.sleep(3)
            st.success('Данные обновлены!')
        else:
            st.error('Деньги ушли в -')

if menu=='Стартовая страница':
    '''# Привет!
    Вы играете за Китай'''

    st.write('🏠  Пекин | ⚙️ - 60 | 🌳 - 72%')
    st.write('🏠  Шанхай | ⚙️ - 50 | 🌳 - 54 %')
    st.write('🏠  Гуанчжоу | ⚙️ - 50 | 🌳 - 54 %')
    st.write('🏠  Гонконг | ⚙️ - 40 | 🌳 - 36 %')
    Graph1=('MG/Graph1.png')
    st.image(Graph1)
    Graph2 = ('MG/Graph2.png')
    st.image(Graph2)
    Graph3 = ('MG/Graph3.png')
    st.image(Graph3)
    Graph4 = ('MG/Graph4.png')
    st.image(Graph4)