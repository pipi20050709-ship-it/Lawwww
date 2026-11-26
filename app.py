import streamlit as st

st.set_page_config(page_title="神魔法典｜司律魔法RPG", page_icon="⚔️", layout="centered")

# 注入魔法 RPG 視覺樣式
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at center, #1f1635 0%, #0b0814 100%);
        color: #f4e8c1;
    }
    h1, h2, h3 {
        color: #ffd700 !important;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.6);
    }
    .battle-arena {
        background: linear-gradient(180deg, #2b1329 0%, #161129 60%, #1d263b 100%);
        border: 3px solid #d4af37;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.35);
        margin-bottom: 18px;
    }
    .enemy-zone {
        background: rgba(80, 15, 30, 0.75);
        border: 2px solid #ff4b4b;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
    }
    .player-zone {
        background: rgba(20, 50, 80, 0.75);
        border: 2px solid #4da6ff;
        border-radius: 12px;
        padding: 12px;
        display: flex;
        align-items: center;
    }
    .scroll-box {
        background: linear-gradient(135deg, #f7ebd2 0%, #e4cca0 100%);
        color: #2b1d12;
        padding: 18px;
        border-radius: 10px;
        border: 2px solid #b8860b;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 15px;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #2c1e4a 0%, #432c70 100%);
        color: #ffd700;
        border: 1.5px solid #ffd700;
        border-radius: 10px;
        padding: 12px;
        font-size: 1.05rem;
        font-weight: bold;
    }
    section[data-testid="stSidebar"] {
        background-color: #120d21;
        border-right: 1px solid #d4af37;
    }
</style>
""", unsafe_allow_html=True)

# 側邊欄：自創巫師角色
with st.sidebar:
    st.markdown("## 🧙‍♂️ 角色創建與裝備")
    player_name = st.text_input("✍️ 輸入你的巫師／律師大名", value="見習正氣師")
    avatar_choice = st.selectbox("🎭 選擇角色外觀", [
        "🧙‍♂️ 黑袍男巫師（手持接骨木魔杖）",
        "🧙‍♀️ 學院女巫師（配戴雷文克勞冠冕）",
        "🧝‍♂️ 精靈法學劍士（雙持六法全書）",
        "🦉 神秘貓頭鷹使者（夜行審判者）"
    ])
    wand_attr = st.selectbox("🔮 主修屬性", [
        "🔥 火屬性・民法烈焰",
        "💧 水屬性・刑法寒冰",
        "⚡ 光屬性・憲法雷霆"
    ])
    st.divider()
    mode = st.radio("⚔️ 選擇副本關卡", ["🔥 主線關卡：一試選擇題討伐戰", "📜 魔王深淵：二試申論爭點戰"])

# 修正：正確取出頭像符號與屬性名稱文字
avatar_icon = avatar_choice.split(" ")[0]
attr_label = wand_attr.split("・")[0]

# 初始化 RPG 數值
if "rpg_init" not in st.session_state:
    st.session_state.rpg_init = True
    st.session_state.player_hp = 100
    st.session_state.player_max_hp = 100
    st.session_state.level = 1
    st.session_state.exp = 0
    st.session_state.enemy_hp = 100
    st.session_state.enemy_max_hp = 100
    st.session_state.enemy_cd = 2
    st.session_state.combo = 0
    st.session_state.battle_log = "⚔️ 遭遇法典魔物！答對題目即可發動屬性連擊！"
    st.session_state.q_idx = 0
    st.session_state.answered = False

# ================= 主線關卡：一試選擇題討伐戰 =================
if mode == "🔥 主線關卡：一試選擇題討伐戰":
    QUIZ_DATA = [
        {
            "enemy_name": "暗黑催狂魔・民法吞噬者",
            "enemy_icon": "👻",
            "attr": "🔥 民法總則",
            "question": "限制行為能力人未得法定代理人之允許，所訂立之契約，其效力為何？",
            "options": ["A. 無效（去去，契約走）", "B. 效力未定（懸浮咒待承認）", "C. 得撤銷（時間轉換器）", "D. 有效（鐵甲護身）"],
            "answer": "B. 效力未定（懸浮咒待承認）",
            "explanation": "依【民法第79條】，限制行為能力人未得法定代理人之允許，所訂立之契約，須經法定代理人之承認，始生效力（效力未定）。"
        },
        {
            "enemy_name": "食死人掠奪者・刑法夢魘",
            "enemy_icon": "💀",
            "attr": "💧 刑法分則",
            "question": "甲意圖為自己不法之所有，趁乙不注意時取走乙桌上的魔杖，構成何罪？",
            "options": ["A. 搶奪罪", "B. 侵占罪", "C. 竊盜罪", "D. 詐欺罪"],
            "answer": "C. 竊盜罪",
            "explanation": "依【刑法第320條第1項】，意圖為自己或第三人不法之所有，而竊取他人之動產者，為竊盜罪。"
        },
        {
            "enemy_name": "魔法部審判官・違憲巨獸",
            "enemy_icon": "🐉",
            "attr": "⚡ 憲法訴訟",
            "question": "人民聲請法規範憲法審查，應於不利確定終局裁判送達後幾個月內為之？",
            "options": ["A. 2個月", "B. 3個月", "C. 6個月", "D. 1年"],
            "answer": "C. 6個月",
            "explanation": "依【憲法訴訟法第59條第2項】，聲請應自用盡審級救濟之最終裁判送達後翌日起之6個月不變期間內為之。"
        }
    ]

    q = QUIZ_DATA[st.session_state.q_idx % len(QUIZ_DATA)]

    st.title("⚔️ 神魔法典：司律魔法RPG")
    c1, c2, c3 = st.columns(3)
    c1.metric("🧙 角色等級", f"Lv.{st.session_state.level} ({st.session_state.exp}/100)")
    c2.metric("🔥 攻擊連擊", f"{st.session_state.combo} Combo")
    c3.metric("🔮 裝備屬性", attr_label)

    enemy_hp_pct = max(0, int((st.session_state.enemy_hp / st.session_state.enemy_max_hp) * 100))
    player_hp_pct = max(0, int((st.session_state.player_hp / st.session_state.player_max_hp) * 100))

    st.markdown(f"""
    <div class="battle-arena">
        <div class="enemy-zone">
            <div style="font-size: 3.5rem;">{q['enemy_icon']}</div>
            <div style="font-size: 1.2rem; font-weight: bold; color: #ff8080;">{q['enemy_name']}</div>
            <div style="color: #ffd700; font-size: 0.95rem; margin: 4px 0;">
                ⏳ 攻擊倒數：<b>CD {st.session_state.enemy_cd}</b> ｜ 關卡屬性：{q['attr']}
            </div>
            <div style="background:#333; border-radius:8px; height:14px; width:80%; margin:8px auto; overflow:hidden;">
                <div style="background:linear-gradient(90deg, #ff1e1e, #ff7b00); width:{enemy_hp_pct}%; height:100%;"></div>
            </div>
            <div style="font-size:0.85rem; color:#ffcccc;">BOSS HP: {st.session_state.enemy_hp} / {st.session_state.enemy_max_hp}</div>
        </div>
        <div style="text-align:center; color:#ffd700; font-weight:bold; margin: 10px 0;">
            {st.session_state.battle_log}
        </div>
        <div class="player-zone">
            <div style="font-size: 2.8rem;">{avatar_icon}</div>
            <div style="flex-grow:1; padding-left: 15px;">
                <div style="font-size: 1.1rem; font-weight: bold; color: #80c1ff;">{player_name} (Lv.{st.session_state.level})</div>
                <div style="background:#333; border-radius:8px; height:14px; width:100%; margin:6px 0; overflow:hidden;">
                    <div style="background:linear-gradient(90deg, #00c853, #69f0ae); width:{player_hp_pct}%; height:100%;"></div>
                </div>
                <div style="font-size:0.85rem; color:#cce6ff;">MY HP: {st.session_state.player_hp} / {st.session_state.player_max_hp}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.player_hp <= 0:
        st.error("💀 你的生命值歸零，在法典迷宮中力竭倒下了！")
        if st.button("✨ 使用復活石重新挑戰", use_container_width=True):
            st.session_state.player_hp = 100
            st.session_state.enemy_hp = 100
            st.session_state.enemy_cd = 2
            st.session_state.combo = 0
            st.session_state.answered = False
            st.session_state.battle_log = "⚔️ 復活成功！再次迎戰法典魔物！"
            st.rerun()

    elif st.session_state.enemy_hp <= 0:
        st.balloons()
        st.success(f"🏆 **STAGE CLEAR！** 你成功擊殺了【{q['enemy_name']}】，獲得 +50 經驗值與回復 30 HP！")
        if st.button("➡️ 進入下一層迷宮（挑戰新魔王）", use_container_width=True):
            st.session_state.exp += 50
            if st.session_state.exp >= 100:
                st.session_state.level += 1
                st.session_state.exp -= 100
                st.session_state.player_max_hp += 20
            st.session_state.player_hp = min(st.session_state.player_max_hp, st.session_state.player_hp + 30)
            st.session_state.enemy_max_hp += 20
            st.session_state.enemy_hp = st.session_state.enemy_max_hp
            st.session_state.enemy_cd = 2
            st.session_state.q_idx += 1
            st.session_state.answered = False
            st.session_state.battle_log = "⚔️ 新的法典魔王出現了！"
            st.rerun()

    else:
        st.markdown(f"""
        <div class="scroll-box">
            📜 <b>【魔法題目卷軸】</b><br>{q['question']}
        </div>
        """, unsafe_allow_html=True)

        for opt in q["options"]:
            if st.button(f"⚡ 施放技能：{opt}", key=opt, disabled=st.session_state.answered, use_container_width=True):
                st.session_state.answered = True
                if opt == q["answer"]:
                    st.session_state.combo += 1
                    dmg = 40 + (st.session_state.combo * 10) + (st.session_state.level * 5)
                    st.session_state.enemy_hp = max(0, st.session_state.enemy_hp - dmg)
                    st.session_state.battle_log = f"💥 {player_name} 發動 {st.session_state.combo} Combo 屬性暴擊！對魔王造成 {dmg} 點傷害！"
                else:
                    st.session_state.combo = 0
                    st.session_state.enemy_cd -= 1
                    if st.session_state.enemy_cd <= 0:
                        enemy_dmg = 35
                        st.session_state.player_hp = max(0, st.session_state.player_hp - enemy_dmg)
                        st.session_state.enemy_cd = 2
                        st.session_state.battle_log = f"🔥 答錯且敵人 CD 歸零！{q['enemy_name']} 發動猛攻，你受到 {enemy_dmg} 點傷害！"
                    else:
                        st.session_state.battle_log = f"⚠️ 咒語施放失敗！敵人攻擊倒數剩下 CD {st.session_state.enemy_cd}！"
                st.rerun()

        if st.session_state.answered:
            st.info(f"📖 **【法典解析卷軸】**\n\n{q['explanation']}")
            if st.button("⚔️ 繼續下一回合攻防", use_container_width=True):
                st.session_state.q_idx += 1
                st.session_state.answered = False
                st.rerun()

# ================= 魔王深淵：二試申論爭點戰 =================
else:
    st.title("📜 魔王深淵：二試申論大決戰")
    st.caption(f"出戰勇者：{avatar_icon} {player_name} (Lv.{st.session_state.level})")
    
    st.markdown("""
    <div class="scroll-box">
        <b>【深淵案例】</b><br>
        甲出資購買 A 地，與乙成立借名登記契約，將 A 地登記於乙名下。嗣後乙未經甲同意，擅自將 A 地出賣並移轉所有權登記予善意之丙。試問：乙、丙間之物權行為效力為何？
    </div>
    """, unsafe_allow_html=True)

    user_ans = st.text_area("✍️ 詠唱你的三段論法咒語（寫出爭點與實務見解關鍵字）：", height=130)
    if st.button("🔥 釋放奧義・三段論法斬擊！", use_container_width=True):
