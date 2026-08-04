import streamlit as st
import sys
import io
import os
from ppact.application import APPLICATION_LIBRARY
from ppact.workflow import run_application

# 페이지 기본 설정
st.set_page_config(
    page_title="PPACT Simulator",
    layout="wide"
)

# 메인 타이틀 (공식 타이틀 적용)
st.title("숭실대학교 차세대반도체학과 - AI 반도체 PPACT 시뮬레이터")
st.markdown("---")

# 사이드바 UI 구성
st.sidebar.header("⚙️ 시뮬레이션 설정")

# Application 선택 드롭다운 구성 (이름과 Key 매핑)
app_keys = list(APPLICATION_LIBRARY.keys())
selected_app = st.sidebar.selectbox(
    "Application (응용 분야) 선택", 
    app_keys,
    format_func=lambda x: f"{x} ({APPLICATION_LIBRARY[x].name})"
)

# 실행 버튼
if st.sidebar.button("▶️ 시뮬레이션 실행"):
    st.subheader(f"📊 [{APPLICATION_LIBRARY[selected_app].name}] 분석 결과")
    
    # 1. 기존 파이썬의 print() 출력을 웹 화면용으로 캡처
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    
    try:
        with st.spinner("PPACT 엔진 분석 중..."):
            # 기존 workflow.py의 함수를 그대로 호출
            run_application(selected_app, show_analysis=True)
    except Exception as e:
        print(f"실행 중 오류가 발생했습니다: {e}")
    finally:
        # 표준 출력 원상 복구
        sys.stdout = old_stdout
        
    # 2. 캡처된 텍스트 분석 리포트 출력
    st.text(captured_output.getvalue())
    
    # 3. 그래프 결과 출력 (화면을 2분할하여 나란히 배치)
    st.markdown("### 📈 PPACT 차트 분석")
    col1, col2 = st.columns(2)
    
    if os.path.exists("system_bars.png"):
        col1.image("system_bars.png", caption="System Budgets (Absolute Constraints)", use_container_width=True)
    else:
        col1.info("막대 그래프(system_bars.png)가 생성되지 않았습니다. (제약 조건 통과 실패 등)")
        
    if os.path.exists("system_spider.png"):
        col2.image("system_spider.png", caption="PPACT Efficiency (Normalized Score)", use_container_width=True)
    else:
        col2.info("방사형 차트(system_spider.png)가 생성되지 않았습니다.")
