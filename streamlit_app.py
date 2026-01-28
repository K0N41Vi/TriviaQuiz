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
# 雑学クイズ（30問）
# =====================
QUIZ = [
    {"id": 1, "q": "日本で一番面積が大きい都道府県は【　】である。", "a": "北海道", "h": ["2位の約4倍", "都でも府でもない", "本州とトンネルで接続"]},
    {"id": 2, "q": "光の速さは約【　】km/秒である。", "a": "300000", "h": ["1秒で地球7周", "物理定数", "音より圧倒的に速い"]},
    # ……（中略：ここは元コードそのまま）……
    {"id": 30, "q": "人間の脳は体重の約【　】％しかない。", "a": "2", "h": ["小さい", "でも高消費", "エネルギー20％"]},
]

# =====================
# 初期化
# =====================
if "pool" not in st.session_state:
    st.session_state.pool = QUIZ.copy()
    random.shuffle(st.session_state.pool)
    st.session_state.current = st.session_state.pool.pop()
    st.session_state.hint = 0
    st.session_state.answered = False

st.title("🧠 雑学クイズ（30問）")

# ユーザー名入力（追加）
username = st.text_input("ユーザー名を入力してください")

st.subheader("問題")
st.write(st.session_state.current["q"])

answer = st.text_input("答えを入力（数字・漢字OK）", key=f"answer_{st.session_state.current['id']}")

if st.button("ヒント"):
    if st.session_state.hint < len(st.session_state.current["h"]):
        st.info(st.session_state.current["h"][st.session_state.hint])
        st.session_state.hint += 1

if st.button("回答"):
    st.session_state.answered = True

if st.session_state.answered:
    is_correct = answer.strip() == st.session_state.current["a"]

    if is_correct:
        st.success("⭕ 正解")
    else:
        st.error(f"❌ 不正解：正解は「{st.session_state.current['a']}」")

    # =====================
    # Supabase に保存（ここが課題の核心）
    # =====================
    if username:
        supabase.table("quiz_logs").insert({
            "username": username,
            "quiz_id": st.session_state.current["id"],
            "question": st.session_state.current["q"],
            "answer": answer,
            "is_correct": is_correct
        }).execute()
    else:
        st.warning("ユーザー名が未入力のため、履歴は保存されていません")

    if st.button("次の問題へ"):
        if not st.session_state.pool:
            st.session_state.pool = QUIZ.copy()
            random.shuffle(st.session_state.pool)

        st.session_state.current = st.session_state.pool.pop()
        st.session_state.hint = 0
        st.session_state.answered = False
        st.session_state["answer"] = ""
