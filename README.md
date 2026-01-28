# 🧠 雑学クイズアプリ（Trivia Quiz）

Streamlit を用いて開発した、ブラウザ上で遊べる雑学クイズアプリです。  
ユーザーが回答した履歴は Supabase のデータベースに保存され、アプリを再起動してもデータが消えない仕組みになっています。

---

## 🔗 アプリURL

以下のURLから、誰でもアプリを試すことができます。

👉 https://blank-app-hg1fh3ngspp.streamlit.app/ 
※ Streamlit Community Cloud 上で公開しています

---

## 📌 アプリの主な機能

- 雑学クイズ（全30問）
- 問題はランダム順で出題
- ヒント機能（1問につき最大3回）
- 回答の正誤判定表示
- ユーザー名を入力して回答履歴を保存
- 回答内容・正誤結果を Supabase に永続保存
- 次の問題へ進むと回答入力欄が自動でリセットされる

---

## 🛠 使用技術

- Python
- Streamlit
- Supabase（PostgreSQL）
- GitHub
- Streamlit Community Cloud

---

## 🧠 工夫した点・改良点

- **sqlite3 ではなく Supabase を利用**  
  Streamlit Cloud ではアプリが停止するとローカルDBの内容が消えてしまうため、外部データベースとして Supabase を使用しました。

- **回答入力欄が前の入力を保持してしまう問題の解決**  
  Streamlit の `session_state` の仕様により、入力欄の値を直接リセットできなかったため、  
  問題IDごとに `key` を変更することで、毎回新しい入力欄として扱われるようにしました。

- **認証情報の安全な管理**  
  Supabase の URL と API Key は、`secrets.toml` を用いて管理し、GitHub には公開しないようにしています。

---

## 🤖 生成AIの活用について

- Streamlit と Supabase を連携する方法
- Supabase のテーブル設計
- Streamlit の `session_state` に関するエラーの原因調査と解決
- README（本ファイル）の構成と Markdown 記法

これらについて、生成AIを活用して調査・実装を行いました。

---

## ⚠️ 大変だった点

- Supabase の RLS（Row Level Security）が有効なままだと insert に失敗する点に気づくまで時間がかかりました。
- Streamlit の入力欄をリセットしようとして API エラーが発生し、`key` の仕組みを理解する必要がありました。
- GitHub の Public repository と、アプリの公開URLは別物である点を理解するのに苦労しました。

---

## 📁 リポジトリ構成（一部）

