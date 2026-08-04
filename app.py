import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="PPACT Simulator",
    layout="wide"
)

# 메인 타이틀
st.title("숭실대학교 차세대반도체학과 - AI 반도체 PPACT 시뮬레이터")
st.markdown("---")

# 사이드바 UI 구성
st.sidebar.header("⚙️ 시뮬레이션 설정")

# 임시 Application 리스트 (시뮬레이터 원본의 주요 항목들로 구성)
dummy_apps = {
    "drone": "Drone (드론 시각 및 장애물 회피)",
    "autonomous_vehicle": "Autonomous Vehicle (자율주행)",
    "industrial_vision": "Industrial Vision (산업용 결함 검사)",
    "smart_camera": "Smart Camera (스마트 카메라)",
    "mobile_ai": "Mobile AI (온디바이스 LLM)",
    "llm_service": "LLM Service (데이터센터 LLM 서비스)"
}

# 드롭다운 메뉴
selected_app_key = st.sidebar.selectbox(
    "Application (응용 분야) 선택", 
    list(dummy_apps.keys()),
    format_func=lambda x: dummy_apps[x]
)

# 실행 버튼과 임시 결과 화면
if st.sidebar.button("▶️ 시뮬레이션 실행"):
    st.subheader(f"📊 [{dummy_apps[selected_app_key]}] 분석 결과")
    st.info("🛠️ 현재 PPACT 시뮬레이터 백엔드 엔진을 웹 서버에 연동하는 작업이 진행 중입니다.\n\n곧 실제 시스템 예산(System Budgets) 차트와 PPACT 효율성(Efficiency) 방사형 차트가 제공될 예정입니다.")
else:
    st.write("👈 왼쪽 사이드바 메뉴에서 응용 분야를 선택하고 시뮬레이션 실행 버튼을 눌러주세요.")
