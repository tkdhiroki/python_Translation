# python_Translation
## 概要
pyocr（Tesseract-OCR）を用いて、指定したPC画面内の英文を翻訳するアプリケーション。

## 環境
- Windows
- Python 3.6
- Visual Studio Code
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
### pythonモジュール
- pyocr
- PIL
- pyautogui
- googletrans
- pynput

## 使い方
翻訳したい英文が表示している範囲をドラッグ&ドロップすると、和訳後のテキストが出力される。

[こちらのソース](https://github.com/tkdhiroki/python_Translation/blob/87d4a4e4913e65ea1cef1163fd238b857ed0cc13/Transister/src/translation/models/translate.py#L85C1-L90C17)のコメントアウトを解除した後、関数を呼び出すことで実行できる。
## 機能
- pynputでマウスの挙動を監視することで、ドラッグ&ドロップした範囲を座標として受け取る。
- 受け取った座標の範囲をpyautoguiを用いて画像として取得する。
- 取得した画像を翻訳しやすいよう、PILで二値化した後に、OCRを実行する。
- OCRで解析した英文を、googletransで和訳する。



## 未実装箇所
- MVCモデルを意識してかこうとしたが、実行を優先してしまい、modelに集約されている。
- tkinterを用いて、GUIで翻訳の実行・翻訳前後のテキスト表示を行おうとしているが、途中となっている。
