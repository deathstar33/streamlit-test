import streamlit as st
import numpy as np
import pandas as pd
from urllib.error import URLError


def run_event_list():
    
    st.subheader('이벤트/프로모션 현황')
    st.info('Directions : 이벤트/프로모션 점검 현황을 보여주는 Page')
