
import streamlit as st
import random

# 1. 網頁基本設定
st.set_page_config(page_title="霍格華茲法學院｜司律魔法決鬥", page_icon="🪄", layout="centered")

# 2. 注入哈利波特魔法主題 CSS 美術設計（深邃夜空、燙金邊框、羊皮紙卷軸）
st.markdown("""
<style>
    /* 整體背景：霍格華茲深夜星空感 */
    .stApp {
        background: radial-gradient(circle at top, #1b1530 0%, #0d0a1a 100%);
        color: #f4e8c1;
    }
    /* 標題燙金效果 */
    h1, h2, h3 {
        color: #ffd700 !important;
        text-shadow: 0 0 12px rgba(255, 215, 0, 0.5);
        font-family: "Georgia", "Noto Serif TC", serif;
    }
    /* 羊皮紙魔法卷軸卡片 */
    .parchment-box {
        background: linear-gradient(135deg, #f5e6c8 0%, #e6cfa1 100%);
        color: #2c1e16;
        padding: 22px;
        border-radius: 12px;
        border: 3px solid #b8860b;
        box-shadow: 0 0 20px rgba(218, 165, 32, 0.4);
        margin-bottom: 20px;
        font-size: 1.15rem;
        line-height: 1.6;
        font-weight: 500;
    }
    /* 魔王遭遇戰橫幅 */
    .boss-card {
        background: rgba(60, 20, 40, 0.85);
        border: 2px solid #ff4b4b;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.4);
    }
    /* 魔法施法按鈕樣式 */
    div.stButton > button {
        background: linear-gradient(90deg, #2b1d42 0%, #3d2860 100%);
        color: #ffd700;
        border: 1.5px solid #d4af37;
        border-radius: 8px;
        padding: 12px 20px;
        font-size: 1.05rem;
        transition: all 0.25s ease;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #4b3275 0%, #63419c 100%);
        box-shadow: 0 0 15px #ffd700;
        transform: scale(1.01);
    }
    /* 側邊欄魔法學院風格 */
    section[data-testid="stSidebar"] {
        background-color: #130e24;
        border-right: 1px solid #d4af37;
    }
</style>
""", unsafe_allow_html=True)

# 計算巫師法學等級
def get_wizard_rank(score):
    if score >= 50:
        return "⚡ 魔法部最高法院大法官（正氣師領袖）"
    elif score >= 30:
        return "🦉 霍格華茲高年級優等生（N.E.W.T. 級）"
    elif score >= 10:
        return "🪄 葛萊分多／雷文克勞法學見習生"
    else:
        return "📜 剛收到貓頭鷹信件的麻瓜新生"

# 側邊欄：分類帽與課程選擇
with st.sidebar:
    st.markdown("## 🏰 霍格華茲法學院")
    st.caption("「法條是最強大的白魔法，唯有精準涵攝能擊退黑巫師。」")
    house = st.selectbox("🎩 選擇你的學院", ["🦁 葛萊分多（勇氣實戰）", "🦅 雷文克勞（睿智學說）", "🐍 史萊哲林（精準攻防）", "🦡 赫夫帕夫（穩健法條）"])
    mode = st.radio("📖 選擇今日修習課程", ["⚡ 一試決鬥：黑魔法防禦術（選擇題）", "🔮 二試特訓：高階變形學（申論爭點）"])
    st.divider()
    st.info("💡 提示：每答對一題可施展『疾疾，護法現身』重創魔王！")

# ================= 模式一：一試魔法決鬥（選擇題） =================
if mode == "⚡ 一試決鬥：黑魔法防禦術（選擇題）":
    QUIZ_DATA = [
        {
            "boss": "👻 催狂魔（專吸法律人記憶）",
            "spell_name": "民法總則・行為能力咒",
            "question": "限制行為能力人未得法定代理人之允許，所訂立之契約，其效力為何？",
            "options": ["A. 無效（去去，契約走）", "B. 效力未定（懸浮咒待承認）", "C. 得撤銷（時間轉換器）", "D. 有效（鐵甲護身）"],
            "answer": "B. 效力未定（懸浮咒待承認）",
            "explanation": "依【民法第79條】規定，限制行為能力人未得法定代理人之允許，所訂立之契約，須經法定代理人之承認，始生效力（即效力未定）。"
        },
        {
            "boss": "🐍 佛地魔的魂器（竊取魔杖者）",
            "spell_name": "刑法分則・財產犯罪防禦術",
            "question": "甲意圖為自己不法之所有，趁乙不注意時取走乙桌上的接骨木魔杖（手機），構成何罪？",
            "options": ["A. 搶奪罪", "B. 侵占罪", "C. 竊盜罪", "D. 詐欺罪"],
            "answer": "C. 竊盜罪",
            "explanation": "依【刑法第320條第1項】，意圖為自己或第三人不法之所有，而竊取他人之動產者，為竊盜罪。"
        },
        {
            "boss": "⚖️ 恩不里居（魔法部教育官）",
            "spell_name": "憲法訴訟法・基本權救濟咒",
            "question": "人民聲請法規範憲法審查，應於不利確定終局裁判送達後幾個月內為之？",
            "options": ["A. 2個月", "B. 3個月", "C. 6個月", "D. 1年"],
            "answer": "C. 6個月",
            "explanation": "依【憲法訴訟法第59條第2項】，聲請應自用盡審級救濟之最終裁判送達後翌日起之6個月不變期間內為之。"
        }
    ]

    if "q_list" not in st.session_state:
        st.session_state.q_list = random.sample(QUIZ_DATA, len(QUIZ_DATA))
        st.session_state.q_idx = 0
        st.session_state.hp = 3
        st.session_state.score = 0
        st.session_state.combo = 0
        st.session_state.q_answered = False
        st.session_state.q_correct = None

    st.title("🪄 黑魔法防禦術：法條決鬥場")
    st.caption(f"所屬學院：{house} ｜ 當前稱號：**{get_wizard_rank(st.session_state.score)}**")

    # 狀態欄
    c1, c2, c3 = st.columns(3)
    c1.metric("巫師生命值", f"{'❤️' * st.session_state.hp}{'🖤' * (3 - st.session_state.hp)}")
    c2.metric("魔力積分", f"{st.session_state.score} pts")
    c3.metric("連擊 Combo", f"🔥 {st.session_state.combo} 連勝")

    total_q = len(st.session_state.q_list)
    st.progress(st.session_state.q_idx / total_q)

    # 結算畫面
    if st.session_state.hp <= 0 or st.session_state.q_idx >= total_q:
        if st.session_state.hp > 0:
            st.balloons()
            st.markdown(f"""
            <div class="parchment-box">
                <h3>🏆 霍格華茲決鬥勝利！</h3>
                <p>你成功擊退了所有黑巫師與考題魔王！</p>
                <p><b>最終魔力積分：</b> {st.session_state.score} 分<br>
                <b>獲得最高頭銜：</b> {get_wizard_rank(st.session_state.score)}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("💀 魔力耗盡！你被催狂魔擊倒了，快去圖書館重溫法條卷軸吧！")
            
        if st.button("🔄 揮動魔杖，開啟新一輪決鬥", use_container_width=True):
            for k in ["q_list", "q_idx", "hp", "score", "combo", "q_answered", "q_correct"]:
                del st.session_state[k]
            st.rerun()

    # 戰鬥題目畫面
    else:
        q = st.session_state.q_list[st.session_state.q_idx]
        
        # 魔王登場橫幅
        st.markdown(f"""
        <div class="boss-card">
            <span style="color:#ff8080; font-size:0.9rem;">第 {st.session_state.q_idx + 1} / {total_q} 關 遭遇強敵</span><br>
            <strong style="font-size:1.3rem; color:#ffffff;">{q['boss']}</strong><br>
            <span style="color:#ffd700; font-size:0.95rem;">考驗領域：{q['spell_name']}</span>
        </div>
        """, unsafe_allow_html=True)

        # 羊皮紙題目卷軸
        st.markdown(f"""
        <div class="parchment-box">
            📜 <b>【魔法卷軸題目】</b><br><br>
            {q['question']}
        </div>
        """, unsafe_allow_html=True)

        st.write("✨ **請選擇你要詠唱的反擊咒語：**")
        for opt in q["options"]:
            if st.button(f"🪄 {opt}", key=opt, disabled=st.session_state.q_answered, use_container_width=True):
                st.session_state.q_answered = True
                if opt == q["answer"]:
                    st.session_state.combo += 1
                    bonus = 10 + (st.session_state.combo - 1) * 5
                    st.session_state.score += bonus
                    st.session_state.q_correct = True
                else:
                    st.session_state.hp -= 1
                    st.session_state.combo = 0
                    st.session_state.q_correct = False
                st.rerun()

        if st.session_state.q_answered:
            if st.session_state.q_correct:
                st.success(f"⚡ **『疾疾，護法現身！』** 施法成功！對魔王造成暴擊傷害！")
            else:
                st.error(f"💥 **『咒語反彈！』** 施法失敗！正確咒語是：**{q['answer']}**")
            
            st.markdown(f"""
            <div class="parchment-box" style="border-color:#4b0082;">
                📖 <b>【圖書館禁書區・法條奧義解析】</b><br><br>
                {q['explanation']}
            </div>
            """, unsafe_allow_html=True)

            if st.button("➡️ 邁向下一間魔法密室", use_container_width=True):
                st.session_state.q_idx += 1
                st.session_state.q_answered = False
                st.rerun()

# ================= 模式二：二試高階變形學（申論爭點） =================
elif mode == "🔮 二試特訓：高階變形學（申論爭點）":
    ESSAY_DATA = [
        {
            "category": "民法變形學（物權與債編）",
            "title": "借名登記出名人擅自處分不動產之效力",
            "facts": "巫師甲出資購買『古靈閣金庫（A地）』，與乙成立借名登記契約，將 A 地登記於乙名下。嗣後乙未經甲同意，擅自將 A 地出賣並移轉所有權登記予善意之巫師丙。試問：乙、丙間之物權行為效力為何？",
            "keywords": ["借名登記", "無權處分", "有權處分", "106年第3次民事庭決議", "善意取得"],
            "template": {
                "爭點意識": "借名登記契約之出名人擅自處分借名登記之不動產予第三人，該處分行為究屬有權處分或無權處分？",
                "大前提": "依最高法院 106 年度第 3 次民事庭會議決議，借名登記契約僅為借名人與出名人間之內部債權契約，不動產登記名義人既為出名人，出名人處分該不動產即屬「有權處分」，不因第三人為善意或惡意而受影響。",
                "小前提與結論": "本題中，乙為 A 地之登記名義人，其將 A 地所有權移轉登記予丙之物權行為，性質上為「有權處分」，丙已合法取得 A 地所有權，無須再論民法第 759 條之 1 善意取得之問題。"
            }
        }
    ]

    if "e_idx" not in st.session_state:
        st.session_state.e_idx = 0
        st.session_state.e_score = 0
        st.session_state.e_sub = False

    st.title("🔮 高階變形學：三段論法煉金術")
    st.caption("寫出核心爭點與實務見解關鍵字，煉成無懈可擊的法學結界！")
    st.progress(st.session_state.e_idx / len(ESSAY_DATA))

    if st.session_state.e_idx >= len(ESSAY_DATA):
        st.balloons()
        st.markdown(f"""
        <div class="parchment-box">
            <h3>🏆 變形學大師認證達成！</h3>
            <p>今日三段論法煉成圓滿結束！累積爭點魔力：<b>{st.session_state.e_score} 分</b></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 重新煉製卷軸", use_container_width=True):
            for k in ["e_idx", "e_score", "e_sub"]:
                del st.session_state[k]
            st.rerun()
    else:
        item = ESSAY_DATA[st.session_state.e_idx]
        st.subheader(f"📌 煉金課題：{item['title']}")
        
        st.markdown(f"""
        <div class="parchment-box">
            📜 <b>【魔法部案件卷宗】</b><br><br>
            {item['facts']}
        </div>
        """, unsafe_allow_html=True)

        user_ans = st.text_area("🪶 請用羽毛筆寫下【爭點】、【核心實務見解】與【結論】：", height=140, disabled=st.session_state.e_sub)

        if not st.session_state.e_sub:
            if st.button("✨ 注入魔力，封印卷軸（送出批改）", use_container_width=True):
                if user_ans.strip():
                    st.session_state.e_sub = True
                    st.rerun()
                else:
                    st.warning("羽毛筆還沒沾墨水呢！請先輸入關鍵字喔！")

        if st.session_state.e_sub:
            hit = [kw for kw in item["keywords"] if kw in user_ans]
            miss = [kw for kw in item["keywords"] if kw not in user_ans]
            rate = int((len(hit) / len(item["keywords"])) * 100)
            
            st.markdown(f"### 🎯 魔法陣共鳴度（爭點命中率）：**{rate}%**")
            c1, c2 = st.columns(2)
