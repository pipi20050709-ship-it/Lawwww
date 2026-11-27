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
  }
  * { box-sizing: border-box; font-family: "Noto Serif TC", "PingFang TC", "Microsoft JhengHei", serif; }
  body {
    margin: 0; padding: 14px; background: radial-gradient(circle at top, #1c2536 0%, var(--bg-dark) 80%);
    color: var(--text-main); min-height: 100vh; display: flex; flex-direction: column; align-items: center;
  }
  .container { width: 100%; max-width: 760px; display: flex; flex-direction: column; gap: 12px; }
  
  .terrarium-box {
    border: 2px solid var(--glass-border); border-radius: 16px; padding: 16px;
    background: linear-gradient(180deg, rgba(255,255,255,0.06) 0%, rgba(15,20,28,0.95) 100%);
    box-shadow: 0 0 28px rgba(184, 151, 88, 0.18), inset 0 0 24px rgba(110, 198, 255, 0.12);
  }
  .phase-badge {
    display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 13px;
    background: rgba(229, 184, 105, 0.15); border: 1px solid var(--gold); color: var(--gold);
    margin-bottom: 8px; font-weight: bold;
  }
  .scene-title { font-size: 20px; font-weight: bold; margin: 4px 0 8px; color: #fff; }
  .scene-desc { font-size: 15px; line-height: 1.65; color: #d5dfec; margin: 0; }
  .reason-box {
    margin-top: 10px; padding: 10px 12px; border-radius: 8px;
    background: rgba(229, 184, 105, 0.08); border-left: 3px solid var(--gold);
    font-size: 13.5px; color: #f3dfb6; line-height: 1.55;
  }

  .stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-top: 14px; }
  .stat-card {
    background: rgba(10, 14, 20, 0.75); border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px; padding: 8px; text-align: center;
  }
  .stat-label { font-size: 12px; color: var(--text-dim); }
  .stat-val { font-size: 18px; font-weight: bold; margin-top: 2px; }

  .log-box {
    background: var(--card-bg); border: 1px solid rgba(184,151,88,0.35); border-radius: 12px;
    padding: 12px 14px; height: 155px; overflow-y: auto; font-size: 14px; line-height: 1.6;
  }
  .log-item { margin-bottom: 6px; padding-bottom: 6px; border-bottom: 1px dashed rgba(255,255,255,0.08); }
  .log-prayer { color: var(--ice); }
  .log-system { color: var(--gold); }
  .log-alert { color: var(--danger); font-weight: bold; }

  .action-panel {
    background: var(--card-bg); border: 1px solid rgba(255,255,255,0.12);
    border-radius: 14px; padding: 14px;
  }
  .panel-title { font-size: 14px; color: var(--gold); margin-bottom: 10px; font-weight: bold; }
  .btn-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 10px; }
  button {
    background: linear-gradient(180deg, #273347 0%, #1b2433 100%);
    color: #fff; border: 1px solid var(--glass-border); border-radius: 10px;
    padding: 12px 10px; font-size: 14px; cursor: pointer; transition: 0.15s;
    text-align: center; line-height: 1.45;
  }
  button:active { transform: scale(0.97); background: #33425c; }

  .codex-bar {
    font-size: 13px; color: var(--text-dim); background: rgba(0,0,0,0.35);
    padding: 10px 12px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.08);
  }
  .law-tag {
    display: inline-block; background: rgba(229,184,105,0.2); color: var(--gold);
    border: 1px solid rgba(229,184,105,0.5); padding: 2px 8px; border-radius: 6px;
    margin: 4px 4px 0 0; font-size: 12px;
  }
  .law-tag.const { border-color: #ff8787; color: #ffc9c9; background: rgba(255, 107, 107, 0.18); }
</style>
</head>
<body>

<div class="container">
  <div class="terrarium-box">
    <div class="phase-badge" id="phaseBadge">序章第一幕：風雪中的微縮王國</div>
    <div class="scene-title" id="sceneTitle">深夜書房裡的玻璃箱奇蹟</div>
    <p class="scene-desc" id="sceneDesc">
      你穿著睡衣俯身擦去玻璃上的灰塵，望見裡面竟是一座暴風雪籠罩的迷你王國。拇指大的子民縮在破屋簷下瑟瑟發抖，糧倉空空如也。現在還不是立法的時候——他們必須先活下來。
    </p>
    <div class="reason-box" id="reasonBox" style="display:none;"></div>

    <div class="stats-grid">
      <div class="stat-card"><div class="stat-label">溫度</div><div class="stat-val" id="statTemp" style="color:#6ec6ff;">10°</div></div>
      <div class="stat-card"><div class="stat-label">糧食</div><div class="stat-val" id="statFood" style="color:#ffd43b;">0</div></div>
      <div class="stat-card"><div class="stat-label">安全</div><div class="stat-val" id="statSafe" style="color:#ff8787;">20</div></div>
      <div class="stat-card"><div class="stat-label">法治</div><div class="stat-val" id="statLaw" style="color:#b197fc;">0</div></div>
    </div>
  </div>

  <div class="log-box" id="logBox">
    <div class="log-item log-prayer">❄️ 箱內微弱祈禱：「好冷……已經三天沒有麵包了……誰來救救我們……」</div>
  </div>

  <div class="action-panel">
    <div class="panel-title" id="panelTitle">【神明介入】打開玻璃箱頂蓋，投放救命物資：</div>
    <div class="btn-grid" id="btnGrid"></div>
  </div>

  <div class="codex-bar">
    <div>📜 <strong>創世法典石碑</strong>（各法典皆從第 1 條出發，依衝突而生）</div>
    <div id="codexList" style="margin-top:4px;">尚未刻下任何法條（自然狀態）</div>
  </div>
</div>

<script>
  const state = {
    phase: 'SURVIVAL', // SURVIVAL -> DEFENSE -> CONST_1 -> CIVIL_1 -> CRIM_1 -> DONE
    temp: 10,
    food: 0,
    safe: 20,
    law: 0,
    enactedLaws: new Set(),
    codexDisplay: []
  };

  function enactLaw(id, label, isConst = false) {
    state.enactedLaws.add(id);
    state.codexDisplay.push({ label, isConst });
  }

  function addLog(text, type = 'log-system') {
    const box = document.getElementById('logBox');
    const div = document.createElement('div');
    div.className = `log-item ${type}`;
    div.textContent = text;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
  }

  function setScene(badge, title, desc, panelTitle, reasonText = '') {
    document.getElementById('phaseBadge').textContent = badge;
    document.getElementById('sceneTitle').textContent = title;
    document.getElementById('sceneDesc').textContent = desc;
    document.getElementById('panelTitle').textContent = panelTitle;
    const rb = document.getElementById('reasonBox');
    if (reasonText) {
      rb.style.display = 'block';
      rb.innerHTML = reasonText;
    } else {
      rb.style.display = 'none';
    }
  }

  function updateUI() {
    document.getElementById('statTemp').textContent = state.temp + '°';
    document.getElementById('statFood').textContent = state.food;
    document.getElementById('statSafe').textContent = state.safe;
    document.getElementById('statLaw').textContent = state.law;

    const codexList = document.getElementById('codexList');
    if (state.codexDisplay.length > 0) {
      codexList.innerHTML = state.codexDisplay.map(c =>
        `<span class="law-tag ${c.isConst ? 'const' : ''}">${c.label}</span>`
      ).join('');
    }

    const grid = document.getElementById('btnGrid');
    grid.innerHTML = '';

    // 1. 溫飽階段
    if (state.phase === 'SURVIVAL') {
      addBtn('💡 放入微型暖燈', () => {
        state.temp = Math.min(100, state.temp + 30);
        addLog('✨ 暖燈照亮玻璃箱，積雪消融，小人們圍著暖光歡呼！');
        checkSurvivalAndDefense();
      });
      addBtn('🍞 投放一籃麵包', () => {
        state.food += 30;
        addLog('🍞 麵包從天而降，飢餓的居民跪在地上感謝創世神明！');
        checkSurvivalAndDefense();
      });
      addBtn('🌾 撒下抗寒麥種', () => {
        state.food += 25; state.temp += 10;
        addLog('🌱 農夫接過麥種，在融雪後的田地裡播下第一批作物。');
        checkSurvivalAndDefense();
      });
    }

    // 2. 防禦階段
    else if (state.phase === 'DEFENSE') {
      addBtn('🧱 放下防禦石塊', () => {
        state.safe += 30;
        addLog('🧱 小人們用神賜石塊在邊界築起了堅固的石砌城牆！');
        checkSurvivalAndDefense();
      });
      addBtn('🗡️ 賜予精鋼長矛', () => {
        state.safe += 30;
        addLog('⚔️ 民兵隊舉起長矛擊退荒原掠奪者，保住了糧倉！');
        checkSurvivalAndDefense();
      });
    }

    // 3. 憲法第 1 條：為什麼創？因為有人自稱「世襲大公」要把王國變私產
    else if (state.phase === 'CONST_1') {
      addBtn('🏛️ 刻下【憲法第 1 條】\n中華民國基於三民主義，為民有民治民享之民主共和國', () => {
        enactLaw('CONST_1', '憲法 第 1 條', true);
        state.law += 20;
        addLog('🏛️ 【憲法第 1 條】金光降臨！世襲大公的「私產王國宣言」失效，王國確立主權在民與民主共和國根基！');

        state.phase = 'CIVIL_1';
        setScene(
          '立法起點：民法第 1 條（法源）',
          '借糧與分田吵翻天，卻沒有成文法可判！',
          '民主共和的框架立下了，居民開始日常互助與借貸。但農夫甲冬天向農夫乙借了 10 斤麥種，春天收成時卻吵著「只要還 10 斤就好」，乙主張「要連同冬日借貸利息與風險一起算」。小人長老攤手說：「現在還沒有民法典，我該怎麼判？」',
          '【創世法典】刻下民法第一條，建立沒有明文規定時的裁判依據：',
          '<strong>💡 為什麼要創《民法》第 1 條？</strong><br>在成文法條文尚未寫全之前，民間交易與財產糾紛已經發生。第 1 條規定「法律所未規定者，依習慣；無習慣者，依法理」，讓審判者能先依在地習慣與法理定分止爭，不會陷入「無法可判」的僵局。'
        );
        updateUI();
      });
    }

    // 4. 民法第 1 條：為什麼創？因為民間借貸與分田糾紛無明文可依，需習慣與法理
    else if (state.phase === 'CIVIL_1') {
      addBtn('📜 刻下【民法第 1 條】\n民事，法律所未規定者，依習慣；無習慣者，依法理', () => {
        enactLaw('CIVIL_1', '民法 第 1 條');
        state.law += 20;
        addLog('📜 【民法第 1 條】落入廣場！長老依村落借糧習慣與公平法理做出裁決，兩名農夫握手言和！');

        state.phase = 'CRIM_1';
        setScene(
          '立法起點：刑法第 1 條（罪刑法定）',
          '治安官隨意抓人：「我覺得你以後會偷東西！」',
          '民事糾紛平息後，王國治安官卻開始濫權——他把一名剛耕完田的年輕人關進地牢，理由是「我看你眼神飄忽，將來可能會偷竊」。居民驚恐萬分，拍打玻璃壁向你求救！',
          '【創世法典】刻下刑法第一條，用罪刑法定擋住恣意抓捕：',
          '<strong>💡 為什麼要創《刑法》第 1 條？</strong><br>刑罰是最嚴厲的國家手段，會剝奪自由甚至生命。若沒有「行為之處罰，以行為時之法律有明文規定者為限」，統治者或治安官就能拿莫須有的罪名隨意關人。創下第 1 條，就是把「法無明文規定不為罪、不處罰」刻成鐵律。'
        );
        updateUI();
      });
    }

    // 5. 刑法第 1 條：為什麼創？因為沒有明文法律就抓人定罪，必須確立罪刑法定
    else if (state.phase === 'CRIM_1') {
      addBtn('⚖️ 刻下【刑法第 1 條】\n行為之處罰，以行為時之法律有明文規定者為限', () => {
        enactLaw('CRIM_1', '刑法 第 1 條');
        state.law += 20;
        state.law = Math.min(100, state.law + 40);
        addLog('⚖️ 【刑法第 1 條】鎮壓全場！治安官因無明文刑法規定而必須立刻釋放年輕人，王國迎來第一道法治曙光！');

        state.phase = 'DONE';
        setScene(
          '三部法典「第 1 條」起點完成',
          '憲法 1 ➔ 民法 1 ➔ 刑法 1 的完整動機',
          '你完成了王國最核心的三個「第一條」：用《憲法》第 1 條確立民主共和國、用《民法》第 1 條解決無明文時的民間糾紛、用《刑法》第 1 條擋住無法律依據的抓人。接下來可一路往第 2 條、第 3 條……直到最後一條推進！',
          '【下一步擴充】要往哪一條繼續寫下去？'
        );
        updateUI();
      });
    }

    else if (state.phase === 'DONE') {
      addBtn('🔄 重新體驗起點流程', () => location.reload());
    }
  }

  function addBtn(label, onClick) {
    const btn = document.createElement('button');
    btn.innerText = label;
    btn.onclick = onClick;
    document.getElementById('btnGrid').appendChild(btn);
  }

  function checkSurvivalAndDefense() {
    if (state.phase === 'SURVIVAL' && state.temp >= 60 && state.food >= 50) {
      state.phase = 'DEFENSE';
      setScene(
        '序章第二幕：黑暗中的外敵',
        '荒原掠奪者逼近糧倉！',
        '王國剛迎來溫暖與第一批麥收，玻璃箱邊緣的陰影洞穴卻衝出一群荒原掠奪者！小人們拿著木棍節節敗退，抬頭向玻璃外的你呼救！',
        '【神明庇護】投下防禦物資保護王國：'
      );
      addLog('🚨 警報！荒原掠奪者襲擊王國邊界！', 'log-alert');
    } else if (state.phase === 'DEFENSE' && state.safe >= 70) {
      state.phase = 'CONST_1';
      setScene(
        '立法起點：憲法第 1 條（民主共和國）',
        '自稱「世襲大公」的強人想把王國變私產！',
        '外敵退去、糧倉充盈後，箱內一名強壯的頭目卻站上高台宣稱：「這座王國是我打下來的，從今天起你們都是我的家奴，財產全歸我！」小人們跪在玻璃壁前向你求救！',
        '【創世法典】刻下憲法第一條，宣示王國的根本體制：',
        '<strong>💡 為什麼要創《憲法》第 1 條？</strong><br>當王國從求生走向秩序時，第一個致命危機就是「權力被少數人據為己有」。立下《憲法》第 1 條，確立民主共和國與主權歸屬，才能擋住專制獨裁的源頭。'
      );
      addLog('🙏 小人們跪在玻璃壁前祈禱：「神明啊，王國到底屬於誰？請賜予根本大法！」', 'log-prayer');
    }
    updateUI();
  }

  updateUI();
</script>
</body>
</html>
