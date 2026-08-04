import streamlit as st

# 페이지 기본 설정 (와이드 레이아웃)
st.set_page_config(
    page_title="PPACT Simulator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 타이틀 영역 커스텀 디자인 (세련된 라이트 테마 및 타이틀 분리)
st.markdown("""
    <div style='text-align: center; margin-top: 20px; margin-bottom: 30px;'>
        <h3 style='color: #64748b; font-weight: 500; letter-spacing: 1.5px; margin-bottom: 5px;'>
            개발중
        </h3>
        <h1 style='color: #0f172a; font-weight: 800; font-size: 2.8rem; margin-top: 0px;'>
            AI 반도체 PPACT 시뮬레이터
        </h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 사이드바 UI 구성
st.sidebar.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>⚙️ 시뮬레이션 설정</h3>", unsafe_allow_html=True)

# 임시 Application 리스트에 시각적 아이콘 추가
dummy_apps = {
    "drone": "🚁 Drone (드론 시각 및 장애물 회피)",
    "autonomous_vehicle": "🚘 Autonomous Vehicle (자율주행)",
    "industrial_vision": "🏭 Industrial Vision (산업용 결함 검사)",
    "smart_camera": "📷 Smart Camera (스마트 카메라)",
    "mobile_ai": "📱 Mobile AI (온디바이스 LLM)",
    "llm_service": "☁️ LLM Service (데이터센터 LLM 서비스)"
}

# 드롭다운 메뉴
selected_app_key = st.sidebar.selectbox(
    "Application (응용 분야) 선택", 
    list(dummy_apps.keys()),
    format_func=lambda x: dummy_apps[x]
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

# 시뮬레이션 실행 버튼 (사이드바 폭에 맞춤)
run_btn = st.sidebar.button("▶️ 시뮬레이션 실행", use_container_width=True)

# 메인 화면 영역 구성
if run_btn:
    st.markdown(f"### 📊 [{dummy_apps[selected_app_key]}] 분석 결과")
    
    # 개발 중 상태를 알리는 세련된 경고 배너
    st.warning("🚧 **[시스템 개발 중] 현재 PPACT 시뮬레이터 백엔드 엔진 연동 작업이 진행되고 있습니다.**\n\n곧 하드웨어 아키텍처에 따른 **Performance, Power, Area, Cost, Thermal** 종합 분석 결과가 제공될 예정입니다.", icon="⚙️")
    
    # UI 플레이스홀더 (결과창이 비어있지 않도록 영역 선점)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.info("📉 **System Budgets (Absolute Constraints)**\n\n(차트 렌더링 준비 중...)")
    with col2:
        st.info("🕸️ **PPACT Efficiency (Normalized Score)**\n\n(차트 렌더링 준비 중...)")
        
else:
    # 초기 접속 화면 (안내 문구를 깔끔한 박스 형태로 구성)
    st.markdown("""
    <div style='background-color: #f8fafc; padding: 2rem; border-radius: 8px; border-left: 5px solid #3b82f6;'>
        <h4 style='color: #1e293b; margin-top: 0;'>🚀 시스템 점검 및 고도화 안내</h4>
        <p style='color: #475569; font-size: 1.1rem; line-height: 1.6;'>
            본 웹페이지는 AI 시스템 아키텍처 탐색을 위한 <strong>PPACT (Performance - Power - Area - Cost - Thermal) 시뮬레이터</strong>입니다.<br>
            현재 수강생 여러분께 최적의 실습 환경을 제공하기 위해 <strong>엔진 통합 및 UI 고도화 작업(개발 중)</strong>을 진행하고 있습니다.
        </p>
        <p style='color: #475569; font-size: 1.1rem; margin-bottom: 0; font-weight: 500;'>
            👉 왼쪽 메뉴에서 응용 분야를 둘러보시고, [시뮬레이션 실행] 버튼을 눌러 인터페이스를 확인해 보세요.
        </p>
    </div>
    """, unsafe_allow_html=True)
