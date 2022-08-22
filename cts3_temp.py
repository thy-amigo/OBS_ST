# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:52:54 2022

@author: WGTS4494
"""

import streamlit as st


def gen(info_dic):
       
    template = []
    
    template.append('Problem Description')
    template.append('='*5)
    template.append(info_dic['Problem Description'])
    template.append('-'*10)
    
    template.append('Call Flow')
    template.append('='*5)
    template.append(info_dic['Call Flow'])
    template.append('-'*10)
    
    template.append('User Details')
    template.append('='*5)
    template.append(info_dic['User Details'])
    template.append('-'*10)
    
    template.append('Device Details')
    template.append('='*5)
    template.append(info_dic['Device Details'])
    template.append('-'*10)
    
    template.append('Troubleshooting Done / Case History')
    template.append('='*5)
    template.append(info_dic['Troubleshooting Done / Case History'])
    template.append('-'*10)
    
    
    return template
        
    
st.header('CTS3 TEMPLATE')

pd = st.text_input(label='Problem Description')

cf = st.text_input(label='Call Flow')

ud = st.text_input(label='User Details')

dd = st.text_input(label='Device Details')

td = st.text_input(label='Troubleshooting Done / Case History')

info_dic = {'Problem Description': pd,
            'Call Flow': cf,
            'User Details': ud,
            'Device Details': dd,
            'Troubleshooting Done / Case History': td}

# st.button(label='GENERATE')

if st.button(label='GENERATE'):
    
    
    temp = gen(info_dic)
    
    s = ''
    
    for i in temp:
        
        s += i+'\n'
        
    st.text_area(label ="",value=s, height=1000)
