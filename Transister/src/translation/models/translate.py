import os

from pathlib import Path
import pyautogui
from PIL import Image, ImageEnhance
import pyocr
import pyocr.builders
from googletrans import Translator

from translation.models.monitor import Monitor


class Recognition():
    """画像・翻訳前テキスト・翻訳語テキスト格納クラス"""
    def __init__(self):
        self.image = None
        self.ocr_txt = ''
        self.trans_txt = ''
    
    def get_image(self):
        return self.image
    def get_ocr_txt(self):
        return self.ocr_txt
    def get_trans_txt(self):
        return self.trans_txt



def ocrpath_set():
    """Tesseract-OCRフォルダのPathを取得し環境変数に追加"""
    path_tesseract = Path(__file__).parent
    path_tesseract = os.path.dirname(path_tesseract).split('\\')[0:-2]
    path_tesseract = '\\'.join(path_tesseract)
    path_tesseract = os.path.join(path_tesseract, 'res', 'Tesseract-OCR')
    
    if path_tesseract not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + path_tesseract

def start_ocr(recognition: Recognition, x, y, w, h):
        """与えられた範囲内の画像を取得し、画像内にある言語を解析したあと翻訳の実施"""

        # 入力値判定
        if w == 0 or h == 0:
            print("error")
            recognition.ocr_txt = "解析できません。"

        ocrpath_set()

        # 指定した範囲の画像取得
        img_org = pyautogui.screenshot(region = (x, y, w, h))
        recognition.image = img_org

        img_rgb = img_org.convert('RGB')
        img_w, img_h = img_rgb.size
        if img_w  < 600 or img_h < 600:
            img_rgb.resize((img_w * 2, img_h * 2), Image.NEAREST)
        
        enhancer = ImageEnhance.Sharpness(img_rgb)
        img_rgb = enhancer.enhance(4.0)
        pixels = img_rgb.load()

        # 原稿画像加工（二値化）
        c_max = 140
        for j in range(img_rgb.size[1]):
            for i in range(img_rgb.size[0]):
                if (pixels[i, j][0] > c_max or pixels[i, j][1] > c_max or
                        pixels[i, j][0] > c_max):
                    pixels[i, j] = (255, 255, 255)

        # OCRエンジンの取得
        tools = pyocr.get_available_tools()
        tool = tools[0]

        # OCR実行
        builder = pyocr.builders.TextBuilder()
        recognition.ocr_txt = tool.image_to_string(img_rgb, lang="eng", builder=builder)
        
        translator = Translator()
        recognition.trans_txt = translator.translate(recognition.ocr_txt ,src='en', dest='ja')
        # with open('./eng.txt', mode='w') as f:
        #     f.write(result)
        # with open('./jap.txt', mode='w', encoding='utf-8') as f:
        #     f.write(result_translator.text)

# def debug_test():
#     monitor = Monitor()
#     monitor.start()
#     x, y, w, h = monitor.draw_position()
#     aaa = start_ocr(x, y, w, h)
#     return aaa




    