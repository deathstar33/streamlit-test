import streamlit as st
import numpy as np
import pandas as pd
from urllib.error import URLError

# st.set_page_config(page_title="Map", page_icon="", layout="wide")

def run_info_map_all():
    

# pd.set_option('display.max_columns', None)

    # st.markdown("## [전체] Service Information Map")
    # st.sidebar.header("[전체] Service Information Map")
    # st.write(
    #     """
    #     <span style="font-size : 20px; color:Orange; font-weight : bold;">
    #     Directions : 
    #     상품서비스 전체 현황 보여주는 Page
    #     </span>
    #     <br><br>
    #     """,
    #     unsafe_allow_html=True
    # )
    
    st.subheader('상품서비스 Map (전체)')
    st.info('Directions : 상품서비스 전체 현황을 보여주는 Page')

    def service_data():
        file_path = f'C:/MyProject/streamlit-test/files/1234.xlsx'
        df = pd.read_excel(file_path, sheet_name='서비스 MAP_24년')
        df.fillna('No Data', inplace=True)
        return df.set_index("서비스명")


    try:
        df = service_data() 
    
        st.dataframe(df, height=1000)
        # st.dataframe(df)
        

    except URLError as e:
        st.error(
            """
            **Required internet access.**
            Connection error: %s
        """
            % e.reason
    )