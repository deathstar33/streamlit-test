import streamlit as st
from streamlit_option_menu import option_menu
from map.info_map_all import run_info_map_all
from map.info_map_indivisual import run_info_map_indivisual
from manage.check_schedule import run_check_schedule
from manage.partners_list import run_partners_list
from manage.event_list import run_event_list

# 페이지 설정
st.set_page_config(
    page_title="[상품서비스 상시 관리]",
    page_icon="👋",
    layout="wide"
)

def main():
    with st.sidebar:
        # 상위 메뉴
        main_menu = option_menu(
            'Main Menu',
            ['현황', '진단관리'],
            icons=['bar-chart', 'clipboard'],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "#fafafa"},
                "icon": {"color": "#243746", "font-size": "25px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#ef494c"},
            }
        )

        sub_menu = None

        # 하위 메뉴
        if main_menu == '현황':
            sub_menu = option_menu(
                '현황',
                ['상품서비스 Map(전체)', '상품서비스 Map(개별)'],
                icons=['map', 'map'],
                menu_icon="cast",
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#fafafa"},
                    "icon": {"color": "#243746", "font-size": "25px"},
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#ef494c"},
                }
            )

        elif main_menu == '진단관리':
            sub_menu = option_menu(
                '진단관리',
                ['수탁사 진단일정 관리', '수탁사 현황 관리', '이벤트 관리'],
                icons=['calendar', 'people','file-earmark'],
                menu_icon="cast",
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#fafafa"},
                    "icon": {"color": "#243746", "font-size": "25px"},
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#ef494c"},
                }
            )
    
    if sub_menu == '상품서비스 Map(전체)':
        run_info_map_all()
    elif sub_menu == '상품서비스 Map(개별)':
        run_info_map_indivisual()

    if sub_menu == '수탁사 진단일정 관리':
        run_check_schedule()
    elif sub_menu == '수탁사 현황 관리':
        run_partners_list()
    elif sub_menu == '이벤트 관리':
        run_event_list()

if __name__ == '__main__':
    main()