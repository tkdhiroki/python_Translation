"""マウスのクリック監視クラスの定義"""
from pynput import mouse


class Monitor:
    """マウスのクリック監視クラスのベース"""

    def __init__(self):
        self.counter = 0
        self.over_count = 2
        self.start_x_pos = 0
        self.end_x_pos = 0
        self.start_y_pos = 0
        self.end_y_pos = 0
        #self.timer = 5    # マウスをどのくらい入力待ちをするか

    def count(self):
        self.counter += 1
        print(f'Count:{self.counter}')

    def is_over(self):
        return True if self.counter >= self.over_count else False

    def call(self):
        self.count()
        if self.is_over():
            print('Done')
            self.listener.stop() # 規定回数過ぎたら終了

    def on_click(self, x, y, button, pressed):
        """マウスクリック時のイベント関数
           クリック時の座標を記録する

        Args:
            x (int): x座標
            y (int): y座標
        """
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x,y)))
        if pressed:
            self.start_x_pos = x
            self.start_y_pos = y
        else:
            self.end_x_pos = x
            self.end_y_pos = y
        self.call()
    
    def start(self):
        """マウスのクリック待機イベント開始"""
        with mouse.Listener(
            on_click=self.on_click,) as self.listener:
            self.listener.join()
            ## 指定時間操作がない場合停止させる。
            # time.sleep(self.timer)
            # if self.listener.is_alive():
            #    self.listener.stop()
    
    def draw_position(self):
        """描画範囲の決定

        Returns:
            tupple: 始点の座標、幅、高さを返す
        """
        x = self.start_x_pos if self.start_x_pos <= self.end_x_pos else self.end_x_pos
        y = self.start_y_pos if self.start_y_pos <= self.end_y_pos else self.end_y_pos
        width = abs(self.start_x_pos - self.end_x_pos)
        height = abs(self.start_y_pos - self.end_y_pos)
        return x, y, width, height     

    def debug(self):
        print(f'Start:{self.start_x_pos} at {self.start_y_pos}')
        print(f'Start:{self.end_x_pos} at {self.end_y_pos}')


# def start_monitor():
#     monitor = Monitor()
#     monitor.start()