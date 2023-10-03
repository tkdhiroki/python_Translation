# import translation.views.tkintergui
import translation.models.translate

# translation.views.tkintergui.start_tkinter()

texxxx = translation.models.translate.debug_test()
print(texxxx)
# 空文字時のエラーメッセージ
if not texxxx:
    print('null')