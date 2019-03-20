from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Controller as KeyController


class TwistScroll:
    def __init__(self):
        self.pressing = False
        self.key_controller = KeyController()
        self.last_pressed = 0

    def start(self):
        with MouseListener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) \
         as listener:
                listener.join()

    def on_move(self, x, y):
        pass
    
    def on_click(self, x, y, button, pressed):
        if pressed:
            print("Pressing")
            self.pressing = True
        else:
            print("Releasing")
            self.pressing = False
    
    def on_scroll(self, x, y, dx, dy):
        if not self.pressing:
            # print(f"scrolling {x} {y} {dx} {dy}")
            if dy >= 3:
                self.key_controller.press("6")
                self.key_controller.release("6")

            if dy <= -3:
                self.key_controller.press("7")
                self.key_controller.release("7")

        # print(self.pressing)


ts = TwistScroll()
ts.start()

