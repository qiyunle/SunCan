
import time
import pyautogui

from pynput import keyboard, mouse
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController

# 创建键盘和鼠标控制器
keyboard_controller = KeyboardController()
mouse_controller = MouseController()

class MousekeyController:
    def __init__(self):
        self.Place_times = 26
        self.Pick_times = 60
        self.Bungee_coord = None
        self.Sunflower_coord = None

    def on_press(self, key):
        """按键监听回调函数：
        鼠标放到蹦极僵尸上按B键（每次打开程序只需按一次），鼠标放到向日葵上按S键。按G键开始操作，按ESC键退出"""
        try:
            if key == keyboard.Key.esc:
                print(f"\n程序已退出")
                # 返回False终止按键监听
                return False
            if key == keyboard.KeyCode(char='b') or key == keyboard.KeyCode(char='B'):
                self.Bungee_coord = pyautogui.position()
            if key == keyboard.KeyCode(char='s') or key == keyboard.KeyCode(char='S'):
                self.Sunflower_coord = pyautogui.position()

            # 监听大小写G键，触发操作
            if key == keyboard.KeyCode(char='g') or key == keyboard.KeyCode(char='G'):
                # 检查有无获取坐标，防止报错
                if self.Bungee_coord is None or self.Sunflower_coord is None:
                    print("未获取蹦极僵尸或向日葵的坐标")

                else:
                # 开始对向日葵进行开罐操作
                    for i in range(self.Place_times):
                        # 选择蹦极僵尸
                        mouse_controller.position = self.Bungee_coord
                        mouse_controller.press(mouse.Button.left)
                        mouse_controller.release(mouse.Button.left)
                        time.sleep(0.01)

                        mouse_controller.position = self.Sunflower_coord
                        mouse_controller.press(mouse.Button.left)
                        mouse_controller.release(mouse.Button.left)
                        time.sleep(0.01)


            # 开罐后捡阳光操作
            if key == keyboard.KeyCode(char='j') or key == keyboard.KeyCode(char='J'):

                for i in range(self.Pick_times):

                    mouse_controller.press(mouse.Button.left)
                    mouse_controller.release(mouse.Button.left)

                    time.sleep(0.01)


        except AttributeError:
            # 监听特殊按键（ESC），触发程序退出
            if key == keyboard.Key.esc:
                print(f"\n程序已退出")
                # 返回False终止按键监听
                return False


# 打印操作提示
print("=== 阳光罐头（solar can）操作工具 ===")
print("操作说明：")
print("1. 鼠标放到蹦极僵尸上，按B键（大小写均可）-（每次打开程序只需按一次）")
print("2. 鼠标放到向日葵上，按S键（大小写均可）")
print("3. 按G键（大小写均可），打开阳光罐头（solar can）=======>>这就是tmd太阳能！")
print("4. 按J键（大小写均可），鼠标放在阳光堆上，暴风吸入阳光！")
print("5. 按下 ESC 键，终止程序")
print("========================\n")

# 创建控制器实例
controller = MousekeyController()

# 创建并启动键盘监听器
with keyboard.Listener(on_press=controller.on_press) as listener:
    listener.join()