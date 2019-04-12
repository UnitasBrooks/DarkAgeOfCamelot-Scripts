"""
Twists DAoC spells when you scroll, so you don't get carpel tunnel syndrome.
"""

from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Controller as KeyController, Key
import argparse


class TwistScroll:
    """
    Main class
    """

    def __init__(self, keys, modifier=None):
        self._pressing = False
        self._key_controller = KeyController()
        self._last_pressed = 0
        self._keys = keys
        self._modifier = modifier
        self._index = 0
        self._key_length = len(keys)
        self._modifier = self._get_modifier(modifier)

    def start(self):
        """
        Start the input listener.

        :return: None
        """
        with MouseListener(on_click=self._on_click, on_scroll=self._on_scroll) as listener:
                listener.join()

    def _on_click(self, x, y, button, pressed):
        """
        In DAoC when you are clicking and scrolling you zoom in and out, I don't want to cast while I'm zooming so check
        if we are clicking and set the member variable.

        :param x: Unused
        :param y: Unused
        :param button: Unused
        :param pressed: Whether we are pressing the click button
        :return: None
        """
        if pressed:
            print("Pressing")
            self._pressing = True
        else:
            print("Releasing")
            self._pressing = False
    
    def _on_scroll(self, x, y, dx, dy):
        """
        Main scroll handler, presses the key and tracks the index.

        :param x: Unused
        :param y: Unused
        :param dx: Unused
        :param dy: Direction we are scrolling.
        :return: None
        """
        if not self._pressing:
            if self._index >= self._key_length:
                self._index = 0

            if dy >= 1:
                if self._modifier is not None:
                    self._key_controller.press(self._modifier)

                self._key_controller.press(self._keys[self._index])
                self._key_controller.release(self._keys[self._index])
                self._index += 1

                if self._modifier is not None:
                    self._key_controller.release(self._modifier)

    @staticmethod
    def _get_modifier(modifier):
        """
        Returns the modifier Key that pynput uses.

        :param modifier: modifier string or None
        :return:
        """
        if modifier is None:
            return None
        elif modifier.lower() == "ctrl":
            return Key.ctrl
        elif modifier.lower() == "alt":
            return Key.alt


def parse_args():
    """
    Build the arg object from the CLI using argparse

    :return: the parsed args object
    """
    parser = argparse.ArgumentParser(description='Turns your scroll wheel into a skill presser allowing you to '
                                                 'twist spells by scrolling.')
    parser.add_argument("--keys", type=str, nargs='+', help="Space separated list of keys you want to press and "
                                                            "the order you want to press them.")
    parser.add_argument("--modifier", type=str, help="ctrl, alt, or blank for none", default=None)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    ts = TwistScroll(args.keys, modifier=args.modifier)
    ts.start()

