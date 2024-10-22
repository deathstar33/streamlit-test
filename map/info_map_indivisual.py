import streamlit as st
import numpy as np
import pandas as pd
from urllib.error import URLError

# st.set_page_config(page_title="Map", page_icon="", layout="wide")

def run_info_map_indivisual():
    
        # pd.set_option('display.max_columns', None)

    # st.markdown("## [개별] Service Information Map")
    # st.sidebar.header("[개별] Service Information Map")


    st.subheader('상품서비스 Map (개별)')
    st.info('Directions : 서비스명과 조건 검색으로 조회하는 Page')

    # st.write(
    #     """
    #     <span style="font-size : 20px; color:Orange; font-weight : bold;">
    #     Directions : 
    #     1) 서비스명 기준 조회 2) 필터 기준 조회 상품서비스 현황 보여주는 Page
    #     </span>
    #     <br><br>
    #     """,
    #     unsafe_allow_html=True
    # )


    def service_data():
        file_path = f'C:/files/1234.xlsx'
        df = pd.read_excel(file_path, sheet_name='서비스 MAP_24년')
        df.fillna('No Data', inplace=True)
        return df.set_index("서비스명")

    def filterd_data(df, column, value):
        filterd_df = df[df[column] == value]
        return filterd_df
        
    try:
        # st.write("###### 1) 서비스명 기준 조회")

        st.write(
        """
        <span style="font-size : 18px; color:DarkBlue; font-weight : bold;">
        1) 서비스명 기준 조회
        </span>
        """,
        unsafe_allow_html=True
    )



        df = service_data()
        servies = st.multiselect(
            " 서비스를 고르세요", list(df.index), ["T 월드", "T ID"]
        )


        if not servies:
            st.error("최소 1개 이상의 서비스를 선택하세요.")


        else  : 
            data = df.loc[servies]
            st.write("##### 조회 결과", data.sort_index())


    

    except URLError as e:
        st.error(
            """
            **Required internet access.**
            Connection error: %s
        """
            % e.reason
        )
        

    try : 
        # st.write("###### 2) 필터 기준 조회")
        
        st.write(
        """
        <span style="font-size : 18px; color:DarkBlue; font-weight : bold;">
        2) 필터 기준 조회
        </span>
        """,
        unsafe_allow_html=True
    )



        column_list = ['ISMS 인증 대상', '재위탁 여부', '위탁사', '재수탁사', 'IDC\nCloud',
        '정보처리형태', '상품서비스 구분', '대외 오픈 여부', '보유건수', '주민등록번호', '고유식별정보', '신용카드번호',
        '계좌정보', '생체인식정보', '비밀번호', '성명', '생년월일', '아이디', '이메일', '주소', '이동전화번호',
        '단말기 정보', '위치정보 취급 여부']

        selected_column = st.selectbox('필터할 컬럼을 선택하세요', column_list)
            
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox('필터할 값을 선택하세요', unique_values)

        if not selected_column or not selected_value : 
            st.error("필터 컬럼과 값을 선택하세요") 
        
        else :
            filterd_df = filterd_data(df, selected_column, selected_value)
            num_services = len(filterd_df)
            if filterd_df.empty : 
                st.write("#### 조회 조건에 맞는 데이터가 없습니다. ")
            else : 
                st.write("##### 조회 결과 : 총 {} 개의 서비스가 검색되었습니다.".format(num_services))
                st.write(filterd_df.index.tolist())

    except URLError as e:
        st.error(
            """
            **Required internet access.**
            Connection error: %s
        """
            % e.reason
        )
        