import streamlit as st
import random

st.set_page_config(page_title="司律備考闖關系統", page_icon="⚖️", layout="centered")

# 側邊欄模式切換
mode = st.sidebar.radio("📚 選擇練習模式", ["一試：法條選擇題闖關", "二試：爭點申論特訓"])

# ================= 模式一：一試選擇題 =================
if mode == "一試：法條選擇題闖關":
    QUIZ_DATA = [
        {
            "category": "民法總則",
            "question": "限制行為能力人未得法定代理人之允許，所訂立之契約，其效力為何？",
            "options": ["A. 無效", "B. 效力未定", "C. 得撤銷", "D. 有效"],
            "answer": "B. 效力未定",
            "explanation": "依民法第79條規定，限制行為能力人未得法定代理人之允許，所訂立之契約，須經法定代理人之承認，始生效力（即效力未定）。"
        },
        {
            "category": "刑法分則",
            "question": "甲意圖為自己不法之所有，趁乙不注意時取走乙桌上的手機，構成何罪？",
            "options": ["A. 搶奪罪", "B. 侵占罪", "C. 竊盜罪", "D. 詐欺罪"],
            "answer": "C. 竊盜罪",
            "explanation": "依刑法第320條第1項，意圖為自己或第三人不法之所有，而竊取他人之動產者，為竊盜罪。"
        },
        {
            "category": "憲法訴訟法",
            "question": "人民聲請法規範憲法審查，應於不利確定終局裁判送達後幾個月內為之？",
            "options": ["A. 2個月", "B. 3個月", "C. 6個月", "D. 1年"],
            "answer": "C. 6個月",
            "explanation": "依憲法訴訟法第59條第2項，聲請應自用盡審級救濟之最終裁判送達後翌日起之6個月不變期間內為之。"
        }
    ]

    if "q_list" not in st.session_state:
        st.session_state.q_list = random.sample(QUIZ_DATA, len(QUIZ_DATA))
        st.session_state.q_idx = 0
        st.session_state.hp = 3
        st.session_state.score = 0
        st.session_state.q_answered = False
        st.session_state.q_correct = None

    st.title("⚖️ 一試：法條選擇題闖關")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"生命值：{'❤️' * st.session_state.hp}{'🖤' * (3 - st.session_state.hp)}")
    with col2:
        st.subheader(f"得分：{st.session_state.score} 分")

    total_q = len(st.session_state.q_list)
    st.progress(st.session_state.q_idx / total_q)
    st.divider()

    if st.session_state.hp <= 0 or st.session_state.q_idx >= total_q:
        if st.session_state.hp > 0:
            st.balloons()
            st.success(f"🎉 恭喜通關！最終得分：{st.session_state.score} 分")
        else:
            st.error("💀 生命值歸零！再複習一下法條吧～")
        if st.button("🔄 再玩一次", use_container_width=True):
            for k in ["q_list", "q_idx", "hp", "score", "q_answered", "q_correct"]:
                del st.session_state[k]
            st.rerun()
    else:
        q = st.session_state.q_list[st.session_state.q_idx]
        st.caption(f"第 {st.session_state.q_idx + 1} / {total_q} 題 ｜ {q['category']}")
        st.markdown(f"### {q['question']}")

        for opt in q["options"]:
            if st.button(opt, key=opt, disabled=st.session_state.q_answered, use_container_width=True):
                st.session_state.q_answered = True
                if opt == q["answer"]:
                    st.session_state.score += 10
                    st.session_state.q_correct = True
                else:
                    st.session_state.hp -= 1
                    st.session_state.q_correct = False
                st.rerun()

        if st.session_state.q_answered:
            if st.session_state.q_correct:
                st.success("✅ 答對了！")
            else:
                st.error(f"❌ 答錯囉！正確答案：**{q['answer']}**")
            st.info(f"📖 **解析**：\n\n{q['explanation']}")
            if st.button("➡️ 下一題", type="primary", use_container_width=True):
                st.session_state.q_idx += 1
                st.session_state.q_answered = False
                st.rerun()

# ================= 模式二：二試申論題 =================
elif mode == "二試：爭點申論特訓":
    ESSAY_DATA = [
        {
            "category": "民法（債編與物權）",
            "title": "借名登記出名人擅自處分不動產之效力",
            "facts": "甲出資購買 A 地，與乙成立借名登記契約，將 A 地登記於乙名下。嗣後乙未經甲同意，擅自將 A 地出賣並移轉所有權登記予善意之丙。試問：乙、丙間之物權行為效力為何？",
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

    st.title("📜 二試：爭點申論特訓")
    st.progress(st.session_state.e_idx / len(ESSAY_DATA))
    st.divider()

    if st.session_state.e_idx >= len(ESSAY_DATA):
        st.balloons()
        st.success(f"🎉 今日申論特訓完成！累積爭點積分：{st.session_state.e_score} 分")
        if st.button("🔄 重新練習", use_container_width=True):
            for k in ["e_idx", "e_score", "e_sub"]:
                del st.session_state[k]
            st.rerun()
    else:
        item = ESSAY_DATA[st.session_state.e_idx]
        st.caption(f"第 {st.session_state.e_idx + 1} / {len(ESSAY_DATA)} 題 ｜ {item['category']}")
        st.subheader(f"📌 {item['title']}")
        st.info(f"**【案例事實】**\n\n{item['facts']}")

        user_ans = st.text_area("✍️ 請寫出【爭點】、【核心法條/實務見解】與【結論】：", height=140, disabled=st.session_state.e_sub)

        if not st.session_state.e_sub:
            if st.button("⚖️ 送出交卷", type="primary", use_container_width=True):
                if user_ans.strip():
                    st.session_state.e_sub = True
                    st.rerun()
                else:
                    st.warning("請先輸入答題關鍵字喔！")

        if st.session_state.e_sub:
            hit = [kw for kw in item["keywords"] if kw in user_ans]
            miss = [kw for kw in item["keywords"] if kw not in user_ans]
            rate = int((len(hit) / len(item["keywords"])) * 100)
            st.markdown(f"### 🎯 爭點命中率：**{rate}%**")
            c1, c2 = st.columns(2)
            c1.success(f"✅ **命中**：{', '.join(hit) if hit else '無'}")
            c2.error(f"⚠️ **漏掉**：{', '.join(miss) if miss else '全中！'}")

            with st.expander("📖 展開標準三段論法擬答", expanded=True):
                st.write(f"**1. 爭點意識**：{item['template']['爭點意識']}")
                st.write(f"**2. 大前提**：{item['template']['大前提']}")
                st.write(f"**3. 小前提與結論**：{item['template']['小前提與結論']}")

            if st.button("➡️ 下一題", type="primary", use_container_width=True):
                st.session_state.e_score += rate
                st.session_state.e_idx += 1
                st.session_state.e_sub = False
                st.rerun()
