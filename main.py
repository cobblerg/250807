import streamlit as st

st.set_page_config(page_title="MBTI 추천 웹앱", page_icon="🧭")

st.title("🧠 MBTI 기반 직업 & 여행지 추천")
st.write("당신의 MBTI 유형을 선택하면, 성격에 어울리는 직업과 여행지를 추천해 드립니다!")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 추천 데이터
recommendations = {
    "INTJ": {
        "jobs": [("전략 컨설턴트", "분석적 사고와 기획력이 뛰어난 INTJ에게 적합"),
                 ("연구 과학자", "독립적으로 깊이 탐구하는 환경에 잘 맞음")],
        "travel": [("아이슬란드", "자연 속에서 고요한 사색 가능"),
                   ("교토", "고즈넉한 분위기에서 역사와 전통을 느낄 수 있음")]
    },
    "ENFP": {
        "jobs": [("광고 기획자", "창의적 아이디어로 세상을 바꾸는 역할에 적합"),
                 ("사회 운동가", "열정적으로 사람들과 소통하고 변화를 추구함")],
        "travel": [("스페인 바르셀로나", "예술과 열정이 넘치는 도시"),
                   ("태국 방콕", "다양한 문화와 사람을 만날 수 있는 곳")]
    },
    "ISTJ": {
        "jobs": [("회계사", "정확성과 책임감이 필요한 직업에 적합"),
                 ("공무원", "체계적인 업무 수행에 강점을 가짐")],
        "travel": [("독일 베를린", "질서정연한 도시와 역사 체험"),
                   ("일본 도쿄", "체계적이면서도 효율적인 도시 문화")]
    },
    "ISFP": {
        "jobs": [("디자이너", "감각과 미적 표현에 강점을 가진 ISFP에게 적합"),
                 ("플로리스트", "섬세하고 조용한 환경에서 창의력을 발휘할 수 있음")],
        "travel": [("프랑스 남부", "예술과 감성이 살아있는 지역"),
                   ("발리", "자연과 함께 조용히 휴식을 취할 수 있는 섬")]
    },
    # 기본값: 나머지 MBTI 유형 처리
    "default": {
        "jobs": [("콘텐츠 크리에이터", "자신만의 색깔을 표현하고 사람들과 소통"),
                 ("심리 상담사", "다른 사람을 이해하고 돕는 데 기쁨을 느낄 수 있음")],
        "travel": [("호주 시드니", "다양한 문화와 자유로운 분위기"),
                   ("캐나다 밴프", "자연 속에서 여유를 즐기며 자기 성찰 가능")]
    }
}

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_types)

st.markdown("---")

data = recommendations.get(selected_mbti, recommendations["default"])

st.subheader("🎯 추천 직업")
for job, desc in data["jobs"]:
    st.markdown(f"**🔹 {job}**  \n👉 {desc}")

st.subheader("✈️ 추천 여행지")
for place, desc in data["travel"]:
    st.markdown(f"**🌍 {place}**  \n📌 {desc}")
