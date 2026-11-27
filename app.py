<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>玻璃箱裡的微型王國</title>
<style>
  :root {
    --bg-dark: #0f141c;
    --glass-border: #b89758;
    --card-bg: rgba(24, 32, 44, 0.92);
    --text-main: #eef2f6;
    --text-dim: #9aa7b8;
    --gold: #e5b869;
    --ice: #6ec6ff;
    --danger: #ff6b6b;
    --success: #51cf66;
  }
  * { box-sizing: border-box; font-family: "Noto Serif TC", "PingFang TC", "Microsoft JhengHei", serif; }
  body {
    margin: 0; padding: 14px; background: radial-gradient(circle at top, #1c2536 0%, var(--bg-dark) 80%);
    color: var(--text-main); min-height: 100vh; display: flex; flex-direction: column; align-items: center;
  }
  .container { width: 100%; max-width: 760px; display: flex; flex-direction: column; gap: 12px; }
  
  /* 玻璃箱主視窗 */
  .terrarium-box {
    border: 2px solid var(--glass-border); border-radius: 16px; padding: 16px;
    background: linear-gradient(180deg, rgba(255,255,255,0.06) 0%, rgba(15,20,28,0.95) 100%);
    box-shadow: 0 0 28px rgba(184, 151, 88, 0.18), inset 0 0 24px rgba(110, 198, 255, 0.12);
    position: relative;
  }
  .phase-badge {
    display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 13px;
    background: rgba(229, 184, 105, 0.15); border: 1px solid var(--gold); color: var(--gold);
    margin-bottom: 8px; font-weight: bold;
  }
  .scene-title { font-size: 20px; font-weight: bold; margin: 4px 0 8px; color: #fff; }
  .scene-desc { font-size: 15px; line-height: 1.65; color: #d5dfec; margin: 0; }

  /* 數值狀態列 */
  .stats-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-top: 14px;
  }
  .stat-card {
    background: rgba(10, 14, 20, 0.75); border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px; padding: 8px; text-align: center;
  }
  .stat-label { font-size: 12px; color: var(--text-dim); }
  .stat-val { font-size: 18px; font-weight: bold; margin-top: 2px; }

  /* 箱內祈禱與事件日誌 */
  .log-box {
    background: var(--card-bg); border: 1px solid rgba(184,151,88,0.35); border-radius: 12px;
    padding: 12px 14px; height: 170px; overflow-y: auto; font-size: 14px; line-height: 1.6;
  }
  .log-item { margin-bottom: 6px; padding-bottom: 6px; border-bottom: 1px dashed rgba(255,255,255,0.08); }
  .log-prayer { color: var(--ice); }
  .log-system { color: var(--gold); }
  .log-alert { color: var(--danger); font-weight: bold; }

  /* 神明操作區 */
  .action-panel {
    background: var(--card-bg); border: 1px solid rgba(255,255,255,0.12);
    border-radius: 14px; padding: 14px;
  }
  .panel-title { font-size: 14px; color: var(--gold); margin-bottom: 10px; font-weight: bold; }
  .btn-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; }
  button {
    background: linear-gradient(180deg, #273347 0%, #1b2433 100%);
    color: #fff; border: 1px solid var(--glass-border); border-radius: 10px;
    padding: 12px 10px; font-size: 15px; cursor: pointer; transition: 0.15s;
    text-align: center;
  }
  button:active { transform: scale(0.97); background: #33425c; }
  button.court-btn { border-color: #ff8787; background: linear-gradient(180deg, #3d2228 0%, #261418 100%); }

  /* 已創設法典石碑區 */
  .codex-bar {
    font-size: 13px; color: var(--text-dim); background: rgba(0,0,0,0.35);
    padding: 10px 12px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.08);
  }
  .law-tag {
    display: inline-block; background: rgba(229,184,105,0.2); color: var(--gold);
    border: 1px solid rgba(229,184,105,0.5); padding: 2px 8px; border-radius: 6px;
    margin: 4px 4px 0 0; font-size: 12px;
  }
</style>
</head>
<body>

<div class="container">
  <!-- 玻璃箱觀察視窗 -->
  <div class="terrarium-box">
    <div class="phase-badge" id="phaseBadge">序章第一幕：風雪中的微縮王國</div>
    <div class="scene-title" id="sceneTitle">深夜書房裡的玻璃箱奇蹟</div>
    <p class="scene-desc" id="sceneDesc">
      你穿著睡衣俯身擦去玻璃上的灰塵，望見裡面竟是一座暴風雪籠罩的迷你王國。拇指大的子民縮在破屋簷下瑟瑟發抖，糧倉空空如也。現在還不是立法的時候——他們必須先活下來。
    </p>

    <div class="stats-grid">
      <div class="stat-card"><div class="stat-label">溫度</div><div class="stat-val" id="statTemp" style="color:#6ec6ff;">10°</div></div>
      <div class="stat-card"><div class="stat-label">糧食</div><div class="stat-val" id="statFood" style="color:#ffd43b;">0</div></div>
      <div class="stat-card"><div class="stat-label">安全</div><div class="stat-val" id="statSafe" style="color:#ff8787;">20</div></div>
      <div class="stat-card"><div class="stat-label">法治</div><div class="stat-val" id="statLaw" style="color:#b197fc;">0</div></div>
    </div>
  </div>

  <!-- 箱內祈禱與事件日誌 -->
  <div class="log-box" id="logBox">
    <div class="log-item log-prayer">❄️ 箱內微弱祈禱：「好冷……已經三天沒有麵包了……誰來救救我們……」</div>
  </div>

  <!-- 神明操作面板 -->
  <div class="action-panel">
    <div class="panel-title" id="panelTitle">【神明介入】打開玻璃箱頂蓋，投放救命物資：</div>
    <div class="btn-grid" id="btnGrid"></div>
  </div>

  <!-- 創世法典進度 -->
  <div class="codex-bar">
    <div>📜 <strong>創世法典石碑與大法官神諭錄</strong>（司法官全考科：第 1 條 ➔ 最後一條）</div>
    <div id="codexList" style="margin-top:4px;">尚未刻下任何法條（目前處於自然狀態）</div>
  </div>
</div>

<script>
  const state = {
    phase: 'SURVIVAL', // SURVIVAL -> DEFENSE -> LAW_CIVIL_1 -> LAW_CRIM_1 -> COURT_111_2 -> DONE
    temp: 10,
    food: 0,
    safe: 20,
    law: 0,
    codex: []
  };

  function addLog(text, type = 'log-system') {
    const box = document.getElementById('logBox');
    const div = document.createElement('div');
    div.className = `log-item ${type}`;
    div.textContent = text;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
  }

  function updateUI() {
    document.getElementById('statTemp').textContent = state.temp + '°';
    document.getElementById('statFood').textContent = state.food;
    document.getElementById('statSafe').textContent = state.safe;
    document.getElementById('statLaw').textContent = state.law;

    const codexList = document.getElementById('codexList');
    if (state.codex.length > 0) {
      codexList.innerHTML = state.codex.map(c => `<span class="law-tag">${c}</span>`).join('');
    }

    const grid = document.getElementById('btnGrid');
    grid.innerHTML = '';

    // 階段 1：解決溫飽
    if (state.phase === 'SURVIVAL') {
      addBtn('💡 放入微型暖燈', () => {
        state.temp = Math.min(100, state.temp + 30);
        addLog('✨ 你將暖燈靠近玻璃箱，積雪開始融化，小人們驚喜地圍著光亮取暖！');
        checkPhase();
      });
      addBtn('🍞 投放一籃麵包', () => {
        state.food += 30;
        addLog('🍞 巨手伸入箱中放下熱麵包，飢餓的母子跪在雪地裡向你頂禮膜拜！');
        checkPhase();
      });
      addBtn('🌾 撒下抗寒麥種', () => {
        state.food += 25;
        state.temp += 10;
        addLog('🌱 農夫小人接過神賜麥種，在融雪的土地上播下希望的嫩芽。');
        checkPhase();
      });
    }

    // 階段 2：防禦外敵
    else if (state.phase === 'DEFENSE') {
      addBtn('🧱 放下防禦石塊', () => {
        state.safe += 30;
        addLog('🧱 你把桌上的小石塊放入箱緣，小人們齊心協力築起了堅固的石砌城牆！');
        checkPhase();
      });
      addBtn('🗡️ 賜予精鋼長矛', () => {
        state.safe += 30;
        addLog('⚔️ 民兵隊舉起神明賜予的長矛，成功將荒原掠奪者逼退到玻璃箱角落！');
        checkPhase();
      });
    }

    // 階段 3A：創設民法第 1 條
    else if (state.phase === 'LAW_CIVIL_1') {
      addBtn('📜 刻下【民法第 1 條】\n（法源：法律 ➔ 習慣 ➔ 法理）', () => {
        state.law += 25;
        state.codex.push('民法 第 1 條');
        addLog('⚖️ 發光的【民法第 1 條】石碑落入廣場！小人法官有了審判依據，平息了麥田歸屬爭執！');
        state.phase = 'LAW_CRIM_1';
        document.getElementById('phaseBadge').textContent = '第一章：成文法秩序建立（刑法創世）';
        document.getElementById('sceneTitle').textContent = '守衛隊濫權抓人！需要罪刑法定';
        document.getElementById('sceneDesc').textContent = '和平之後，當初負責防禦的守衛隊長卻隨意將看不順眼的平民關進地牢，聲稱「我說你有罪就是有罪」。平民拍打玻璃壁向你求救！';
        document.getElementById('panelTitle').textContent = '【創世法典】為王國刻下刑法第一條紅線：';
        updateUI();
      });
    }

    // 階段 3B：創設刑法第 1 條
    else if (state.phase === 'LAW_CRIM_1') {
      addBtn('⚖️ 刻下【刑法第 1 條】\n（罪刑法定主義）', () => {
        state.law += 25;
        state.codex.push('刑法 第 1 條');
        addLog('⚡ 雷鳴響起！【刑法第 1 條】石碑鎮壓了守衛隊的擅斷，無辜平民重獲自由！');
        state.phase = 'COURT_111_2';
        document.getElementById('phaseBadge').textContent = '憲政危機：神明＝大法官顯靈';
        document.getElementById('sceneTitle').textContent = '玻璃壁上的【裁判憲法審查聲請書】';
        document.getElementById('sceneDesc').textContent = '數月後，箱內已創設民法第 195 條。然而小人法官竟判決一名誹謗麵包店的平民「必須在王國廣場大聲朗讀道歉啟事」！該平民泣訴思想與不表意自由受辱，向玻璃外的你（大法官）遞出聲請書！';
        document.getElementById('panelTitle').textContent = '【憲法法庭審理】法院以判決命加害人公開道歉，是否合憲？';
        updateUI();
      });
    }

    // 階段 4：大法官顯靈（111年憲判字第2號）
    else if (state.phase === 'COURT_111_2') {
      addBtn('🌟 宣告違憲【111年憲判字第2號】\n侵害不表意自由，逾越比例原則', () => {
        state.law = 100;
        state.codex.push('111年憲判字第2號（違憲宣告）');
        addLog('🌟 金色神諭降臨！強制道歉布告欄化為光點消散，箱內法院從此學會「不表意自由」的界線（改以刊登判決書代替）！', 'log-system');
        state.phase = 'DONE';
        document.getElementById('phaseBadge').textContent = '雛形主線體驗完成！';
        document.getElementById('sceneTitle').textContent = '微縮王國迎來法治黎明';
        document.getElementById('sceneDesc').textContent = '從風雪求生、抵禦外敵，到親手刻下第 1 條法律與做出憲法法庭判決，王國已步入正軌。接下來可繼續擴充全法典（民、刑、公、商與 8 小科至最後一條）！';
        document.getElementById('panelTitle').textContent = '【系統就緒】可隨時擴充下一批法條與釋字／最高法院判決：';
        updateUI();
      }, true);

      addBtn('❌ 宣告合憲\n為回復被害人名譽之必要手段', () => {
        addLog('⚠️ 平行宇宙警告：箱子裡出現大量被迫違心道歉的偽君子，人民對言論自由產生寒蟬效應！請重新審酌憲法第11條不表意自由！', 'log-alert');
      }, true);
    }

    // 結束後可重新體驗
    else if (state.phase === 'DONE') {
      addBtn('🔄 重新體驗序章循環', () => {
        location.reload();
      });
    }
  }

  function addBtn(label, onClick, isCourt = false) {
    const btn = document.createElement('button');
    btn.innerText = label;
    if (isCourt) btn.className = 'court-btn';
    btn.onclick = onClick;
    document.getElementById('btnGrid').appendChild(btn);
  }

  function checkPhase() {
    if (state.phase === 'SURVIVAL' && state.temp >= 60 && state.food >= 50) {
      state.phase = 'DEFENSE';
      document.getElementById('phaseBadge').textContent = '序章第二幕：黑暗中的外敵';
      document.getElementById('sceneTitle').textContent = '荒原掠奪者逼近糧倉！';
      document.getElementById('sceneDesc').textContent = '王國剛迎來溫暖與第一批麥收，玻璃箱邊緣的陰影洞穴卻衝出一群荒原掠奪者！小人們拿著木棍節節敗退，抬頭向玻璃外的你呼救！';
      document.getElementById('panelTitle').textContent = '【神明庇護】投下防禦物資保護王國：';
      addLog('🚨 警報！荒原掠奪者襲擊王國邊界，安全度急劇下降！', 'log-alert');
    } else if (state.phase === 'DEFENSE' && state.safe >= 70) {
      state.phase = 'LAW_CIVIL_1';
      document.getElementById('phaseBadge').textContent = '序章第三幕：安逸後的矛盾（立法開始）';
      document.getElementById('sceneTitle').textContent = '溫飽與安全之後，內部爭執爆發';
      document.getElementById('sceneDesc').textContent = '外敵已退、糧倉滿滿，但民兵隊長與農夫卻為了「誰該擁有新開墾的麥田」大打出手！這時再丟麵包進去已經沒用了——他們需要第一條成文法規則！';
      document.getElementById('panelTitle').textContent = '【創世法典】在玻璃箱底座刻下王國的第一條法律：';
      addLog('🙏 小人們聚集在玻璃壁前祈禱：「神明啊，請賜予我們判斷是非的規矩！」', 'log-prayer');
    }
    updateUI();
  }

  updateUI();
</script>
</body>
</html>
