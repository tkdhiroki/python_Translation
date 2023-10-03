# python_Translation
## 概要
pyocr（Tesseract-OCR）を用いて、指定したPC画面内の英文を翻訳するアプリケーション。

## 仕組み
pyinputでマウスの挙動を監視して、ドラッグ&ドロップした範囲をpyautoguiで撮像する。

撮像した画像を翻訳しやすい用に二値化を行った後、OCRを実行し、抽出したテキストを翻訳にかけている。

## 主要モジュール
PIL
pyautogui
googletrans
pyinput

## 未実装箇所
MVCモデルを意識してかこうとしたが、実行を優先してしまい、modelに集約されている。

tkinterを用いて、GUIで翻訳の実行・翻訳前後のテキスト表示を行おうとしているが、途中となっている。
