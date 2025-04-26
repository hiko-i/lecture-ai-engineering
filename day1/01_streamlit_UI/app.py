import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# ページ設定
# ============================================
st.set_page_config(
    page_title="🎨 Streamlit デモ 🎉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSSでスタイルを強調
st.markdown("""
<style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #ff6600;
        text-align: center;
        animation: pulse 1s infinite alternate;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.1); }
    }
    .highlight {
        font-size: 24px;
        font-weight: bold;
        color: #33ccff;
    }
    .bg {
        background-color: #ffe6cc;
        padding: 20px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 Streamlit 超派手デモ 🌟</div>', unsafe_allow_html=True)
st.markdown("<p class='highlight'>✨ コメントを解除しながらStreamlitの機能を学びましょう ✨</p>", unsafe_allow_html=True)

# ============================================
# サイドバー
# ============================================
st.sidebar.header("🎨 デモのガイド")
st.sidebar.info("コードのコメントを解除して、Streamlitのさまざまな機能を確認しましょう！")

# ============================================
# 基本的なUI要素
# ============================================
st.markdown('<div class="bg">', unsafe_allow_html=True)
st.header("🛠 基本的なUI要素")

# テキスト入力
st.subheader("🔤 テキスト入力")
name = st.text_input("あなたの名前", "ゲスト")
st.write(f"🌟 こんにちは、{name}さん！🌟")

# ボタン
st.subheader("🎯 ボタン")
if st.button("✨ クリックしてください ✨"):
    st.success("🎉 ボタンがクリックされました！ 🎊")

# チェックボックス
st.subheader("✅ チェックボックス")
if st.checkbox("🔍 追加コンテンツを見る"):
    st.info("🚀 これは隠れたコンテンツです！ 🎭")

# スライダー
st.subheader("🎚 スライダー")
age = st.slider("🎂 年齢", 0, 100, 25)
st.write(f"🕰 あなたの年齢: {age} 🎈")

# セレクトボックス
st.subheader("📌 セレクトボックス")
option = st.selectbox(
    "🌐 好きなプログラミング言語は?",
    ["🐍 Python", "🌐 JavaScript", "☕ Java", "🖥 C++", "🚀 Go", "🔥 Rust"]
)
st.write(f"💡 あなたは {option} を選びました")

st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# グラフ表示
# ============================================
st.header("📊 グラフの表示")

# ラインチャート
st.subheader("📈 ラインチャート")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['🔥 A', '💡 B', '🚀 C']
)
st.line_chart(chart_data)

# バーチャート
st.subheader("📊 バーチャート")
chart_data = pd.DataFrame({
    'カテゴリ': ['🎨 A', '🎯 B', '🚀 C', '🎶 D'],
    '値': [10, 25, 15, 30]
}).set_index('カテゴリ')
st.bar_chart(chart_data)

# ============================================
# インタラクティブ機能
# ============================================
st.header("🎮 インタラクティブ機能")

# プログレスバー
st.subheader("🔄 プログレスバー")
progress = st.progress(0)
if st.button("🎈 進捗をシミュレート"):
    for i in range(101):
        time.sleep(0.01)
        progress.progress(i / 100)
    st.balloons()

# ============================================
# デモの使用方法
# ============================================
st.divider()
st.subheader("📜 このデモの使い方")
st.markdown("""
🎨 **色とアイコンを追加して、視覚的に楽しくアレンジ！**
1️⃣ コメントアウトされたコードを解除（#を削除）
2️⃣ 変更を保存し、ブラウザで結果を確認
3️⃣ 様々な組み合わせを試して、UIの変化を楽しもう！
""")
