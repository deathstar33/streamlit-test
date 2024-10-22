import streamlit as st
import numpy as np
import pandas as pd
from urllib.error import URLError
import os
import glob

# st.set_page_config(page_title="Map", page_icon="", layout="wide")

def run_info_map_all():
    
    st.subheader('상품서비스 Map (전체)')
    st.info('Directions : 상품서비스 전체 현황을 보여주는 Page')


    def service_data(selected_file):
        
        df = pd.read_excel(selected_file, sheet_name='서비스 MAP_24년')
        df.fillna('No Data', inplace=True)
        df.dropna(how='all', inplace = True)
        df.reset_index(drop=True, inplace = True)

        return df.set_index("서비스명")
    
    directory_path = f'C:/MyProject/streamlit-test/files/'
    selected_files = glob.glob(os.path.join(directory_path, '*.xlsx'))

    selected_files.sort(reverse=True)
    default_file = glob.glob(os.path.join(directory_path, '*.xlsx'))

    selected_file = st.selectbox("데이터 파일을 선택하세요", selected_files, index=0 if default_file else -1)

    # if st.button("데이터 조회") or default_file : 
    if default_file :
        try:
            df = service_data(selected_file)

            file_name = os.path.basename(selected_file)
            date = file_name[:8]

            st.success(f"데이터 조회 완료 => 기준 일자 : {date}")

            num_rows = df.shape[0]
            height = min(1000, 35 * num_rows)
            # st.dataframe(df, height=1000)
            st.dataframe(df, height=height)
            # st.dataframe(df)
            

        except URLError as e:
            st.error(
                """
                **Required internet access.**
                Connection error: %s
            """
                % e.reason
        )
        
    