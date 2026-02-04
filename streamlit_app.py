import streamlit as st
import random
from supabase import create_client

# =====================
# Supabase 接続
# =====================
supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

# =====================
# クイズデータ（30問）
# =====================
QUIZ = [
    {
        "id": 1,
        "q": "日本で一番面積が大きい県はどれ？",
        "choices": ["岩手県", "北海道", "長野県", "熊本県"],
        "a": "岩手県",
        "h": ["問題文に注目", "東日本", "わんこそば"]
    },
    {
        "id": 2,
        "q": "富士山の標高として最も近いものはどれ？",
        "choices": ["3150m", "3667m", "3776m", "8848m"],
        "a": "3776m",
        "h": [ "語呂合わせで有名", "3500m超", "8848mはエベレストですよ"]
    },
    {
        "id": 3,
        "q": "人の舌で感じられる基本味はいくつ？",
        "choices": ["4", "5", "6", "7"],
        "a": "5",
        "h": ["甘・酸・塩・苦は含まれる", "最近追加された味がある", "うま味"]
    },
    {
        "id": 4,
        "q": "日本の通貨単位はどれ？",
        "choices": ["ウォン", "ドル", "円", "元"],
        "a": "円",
        "h": ["漢字一文字", "硬貨がある", "￥マーク"]
    },
    {
        "id": 5,
        "q": "雷が光ってから音が遅れて聞こえる理由は？",
        "choices": ["光が遅い", "音が遅い", "目が遅い", "耳が遅い"],
        "a": "音が遅い",
        "h": ["空気を伝わる", "真空では聞こえない", "光より遅い"]
    },
    {
        "id": 6,
        "q": "人間の体で一番硬い部分は？",
        "choices": ["骨", "歯", "爪", "頭蓋骨"],
        "a": "歯",
        "h": ["エナメル質", "骨ではない", "鉱物に近い"]
    },
    {
        "id": 7,
        "q": "ペンギンができないことは？",
        "choices": ["泳ぐ", "歩く", "飛ぶ", "潜る"],
        "a": "飛ぶ",
        "h": ["鳥類", "翼はある", "空は飛べない"]
    },
    {
        "id": 8,
        "q": "世界で最も話者数が多い言語は？",
        "choices": ["英語", "スペイン語", "中国語", "ヒンディー語"],
        "a": "中国語",
        "h": ["人口が多い国", "漢字文化", "英語ではない"]
    },
    {
        "id": 9,
        "q": "血液型を発見した国は？",
        "choices": ["ドイツ", "イギリス", "オーストリア", "フランス"],
        "a": "オーストリア",
        "h": ["ヨーロッパ", "医学者", "20世紀初頭"]
    },
    {
        "id": 10,
        "q": "1円玉の素材は？",
        "choices": ["鉄", "銅", "アルミニウム", "銀"],
        "a": "アルミニウム",
        "h": ["軽い", "水に浮く", "銀色"]
    },
    {
        "id": 11,
        "q": "サメにない器官は？",
        "choices": ["心臓", "肺", "浮き袋", "ひれ"],
        "a": "浮き袋",
        "h": ["魚類", "泳ぎ続ける", "肝臓が大きい"]
    },
    {
        "id": 12,
        "q": "エッフェル塔は夏にどうなる？",
        "choices": ["低くなる", "曲がる", "高くなる", "色が変わる"],
        "a": "高くなる",
        "h": ["金属", "熱膨張", "数cm伸びる"]
    },
    {
        "id": 13,
        "q": "大人の人間の骨の数は？",
        "choices": ["180", "196", "206", "220"],
        "a": "206",
        "h": ["200本以上", "赤ちゃんは多い", "成長で減る"]
    },
    {
        "id": 14,
        "q": "日本の紙幣で最も高額なのは？",
        "choices": ["1000円", "5000円", "10000円", "50000円"],
        "a": "10000円",
        "h": ["紫色", "福沢諭吉", "最高額"]
    },
    {
        "id": 15,
        "q": "カメが呼吸できる体の部位は？",
        "choices": ["皮膚", "えら", "お尻", "甲羅"],
        "a": "お尻",
        "h": ["総排泄孔", "冬眠", "皮膚呼吸"]
    },
    {
        "id": 16,
        "q": "月が地球を一周するのにかかる日数は？",
        "choices": ["7日", "14日", "27日", "30日"],
        "a": "27日",
        "h": ["約4週間", "満ち欠けとは別", "公転周期"]
    },
    {
        "id": 17,
        "q": "世界で一番深い海溝は？",
        "choices": ["日本海溝", "マリアナ海溝", "トンガ海溝", "千島海溝"],
        "a": "マリアナ海溝",
        "h": ["太平洋", "1万m級", "日本近海"]
    },
    {
        "id": 18,
        "q": "人の体の約60％を占めるものは？",
        "choices": ["脂肪", "筋肉", "水", "骨"],
        "a": "水",
        "h": ["体液", "重量比", "タプタプ"]
    },
    {
        "id": 19,
        "q": "氷は水よりどうなる？",
        "choices": ["重い", "軽い", "同じ", "不明"],
        "a": "軽い",
        "h": ["浮く", "密度", "体積"]
    },
    {
        "id": 20,
        "q": "ミツバチの巣の形は？",
        "choices": ["三角形", "四角形", "六角形", "円形"],
        "a": "六角形",
        "h": ["イメージを信じろ", "これの正多角形を敷き詰めて完璧な球状にするのは不可能", "内角は120°"]
    },
    {
        "id": 21,
        "q": "イルカは何類？",
        "choices": ["魚類", "両生類", "爬虫類", "哺乳類"],
        "a": "哺乳類",
        "h": ["肺呼吸", "子を産む", "魚ではない"]
    },
    {
        "id": 22,
        "q": "人が1日にまばたきする回数に最も近いのは？",
        "choices": ["1000回", "5000回", "10000回", "30000回"],
        "a": "10000回",
        "h": ["無意識", "目を守る", "1分に数十回"]
    },
    {
        "id": 23,
        "q": "この中で人が寝ている間にしていないことはどれ？",
        "choices": ["眼球運動", "呼吸", "消化活動", "株取引"],
        "a": "株取引",
        "h": ["情勢が大事", "一喜一憂するな", "春本晃汰作問"]
    },
    {
        "id": 24,
        "q": "世界で一番高い山は？",
        "choices": ["K2", "富士山", "エベレスト", "マッターホルン"],
        "a": "エベレスト",
        "h": ["ヒマラヤ", "8000m超", "チョモランマ"]
    },
    {
        "id": 25,
        "q": "血液が体を一周する時間は約？",
        "choices": ["10秒", "30秒", "60秒", "5分"],
        "a": "60秒",
        "h": ["約1分", "心臓", "循環"]
    },
    {
        "id": 26,
        "q": "地球が1回自転する時間は？",
        "choices": ["12時間", "18時間", "24時間", "48時間"],
        "a": "24時間",
        "h": ["1日", "昼夜", "太陽"]
    },
    {
        "id": 27,
        "q": "次のうち肩を鍛えるトレーニング種目はなんでしょう？",
        "choices": ["アーノルドプレス", "ハンマーカール", "ブルガリアンスクワット", "インクラインプレス"],
        "a": "アーノルドプレス",
        "h": ["三角筋前部を集中的に刺激", "さらに三角筋中部にも負荷がかかる", "長拓人作問"]
    },
    {
        "id": 28,
        "q": "金が錆びにくい理由は？",
        "choices": ["柔らかい", "軽い", "酸化しにくい", "高価"],
        "a": "酸化しにくい",
        "h": ["貴金属", "化学的に安定", "変色しない"]
    },
    {
        "id": 29,
        "q": "人の心臓は1日に何回拍動する？",
        "choices": ["1万回", "5万回", "10万回", "50万回"],
        "a": "10万回",
        "h": ["1分約70回", "24時間", "無意識"]
    },
    {
        "id": 30,
        "q": "泉侑吾が唯一覚えている地学用語は何？",
        "choices": ["モホロビチッチ不連続面", "マントル", "アセノスフェア", "白色矮星"],
        "a": "モホロビチッチ不連続面",
        "h": ["ご本人作問", "響きが面白い", "地震波速度の境界であり、地球の地殻とマントルとの境界のこと"]
    }
]

# =====================
# セッション初期化
# =====================
if "initialized" not in st.session_state:
    st.session_state.pool = QUIZ.copy()
    random.shuffle(st.session_state.pool)
    st.session_state.current = st.session_state.pool.pop()
    st.session_state.hint = 0
    st.session_state.correct = 0
    st.session_state.total = 0
    st.session_state.used_hints = 0
    st.session_state.finished = False
    st.session_state.show_result = False
    st.session_state.result = None
    st.session_state.initialized = True

# =====================
# 画面表示
# =====================
st.title("🧠 常識・雑学クイズ")

username = st.text_input("ユーザー名を入力してください")

# 何問目か（/◯ は出さない）
if not st.session_state.finished:
    current_no = min(st.session_state.total + 1, len(QUIZ))
    st.caption(f"第 {current_no} 問")

st.divider()

# =====================
# クイズ画面
# =====================
if not st.session_state.finished:

    st.subheader("問題")
    st.write(st.session_state.current["q"])

    choice = st.radio(
        "選択してください",
        st.session_state.current["choices"],
        key=f"choice_{st.session_state.current['id']}"
    )

    # ---------- ヒント ----------
    if st.button("ヒントを見る"):
        if st.session_state.hint < len(st.session_state.current["h"]):
            st.warning(
                f"ヒント {st.session_state.hint + 1}："
                f"{st.session_state.current['h'][st.session_state.hint]}"
            )
            st.session_state.hint += 1
            st.session_state.used_hints += 1
        else:
            st.info("これ以上ヒントはありません")

    # ---------- 回答 ----------
    if not st.session_state.show_result:
        if st.button("回答する"):
            st.session_state.total += 1

            is_correct = choice == st.session_state.current["a"]

            if is_correct:
                st.session_state.correct += 1
                st.session_state.result = "correct"
            else:
                st.session_state.result = "wrong"

            # Supabase 保存
            supabase.table("quiz_logs").insert({
                "username": username if username else "anonymous",
                "quiz_id": st.session_state.current["id"],
                "question": st.session_state.current["q"],
                "selected_answer": choice,
                "correct_answer": st.session_state.current["a"],
                "is_correct": is_correct
            }).execute()

            st.session_state.show_result = True
            st.rerun()

    # ---------- 正誤表示 ----------
    if st.session_state.show_result:
        if st.session_state.result == "correct":
            st.success("⭕ 正解！")
        else:
            st.error(f"❌ 不正解：正解は「{st.session_state.current['a']}」")

        if st.button("次の問題へ"):
            if st.session_state.pool:
                st.session_state.current = st.session_state.pool.pop()
                st.session_state.hint = 0
                st.session_state.show_result = False
                st.session_state.result = None
            else:
                st.session_state.finished = True

            st.rerun()

# =====================
# 結果表示
# =====================
else:
    st.subheader("📊 結果発表")

    rate = (
        st.session_state.correct / st.session_state.total * 100
        if st.session_state.total > 0 else 0
    )

    st.write(f"ユーザー名：{username if username else '未入力'}")
    st.write(f"正解数：{st.session_state.correct} / {st.session_state.total}")
    st.write(f"正答率：{rate:.1f}%")
    st.write(f"使用ヒント数：{st.session_state.used_hints}")

    if rate == 100 and st.session_state.used_hints == 0:
        st.success("🏆カンニングしてない??")
    elif rate >= 80:
        st.info("🥈雑学マスター")
    elif rate >= 60:
        st.info("🥉ちょっと微妙ですね")
    else:
        st.info("📘常識もなければ話の引き出しも少ない人")
