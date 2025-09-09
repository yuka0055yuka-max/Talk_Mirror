import os
from PIL import Image

# --- 設定 ---
image_filename = "IMG_2352.jpg"  # 画像ファイル名（Pyto内に保存されていること）
keywords = ["パチンコ", "乾燥機"]  # 検出対象のキーワード

# --- 入力 ---
text = input("今日どこ行った？（例：パチンコ店で乾燥機がある場所）\n")

# --- キーワード検出 ---
found = [word for word in keywords if word in text]

# --- 結果処理 ---
if found:
    print(f"🔍 検出されたキーワード：{found}")
    print("🖼️ この発言から連想される風景を表示します：")

    # --- 画像表示 ---
    if os.path.exists(image_filename):
        img = Image.open(image_filename)
        img.show()
    else:
        print(f"⚠️ 画像ファイル '{image_filename}' が見つかりません。Pyto内に保存されているか確認してください。")
else:
    print("✅ 特定可能なキーワードは見つかりませんでした。")
