from pynput.keyboard import Key, Controller
import time
import PySimpleGUI as sg
import sys, os

BASE_PATH = sys.argv[0]
icon_path = os.path.abspath(os.path.join(os.path.dirname(BASE_PATH), 'icon'))


class MessageAttack():
    #使用回车发送消息
    def __init__(self):
        self.keyboard = Controller()

    def main(self, message, times):
        time.sleep(2)

        for i in range(5):
            print(f'再过{5 - i}秒钟后发送消息')
        for i in range(int(times)):
            self.keyboard.type(message)
            self.keyboard.tap(Key.enter)
            # self.keyboard.press(Key.enter)
            # self.keyboard.release(Key.enter)
            time.sleep(0.1)







sg.theme('DefaultNoMoreNagging')
quit_ico = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAVhJREFUOE+dUzFOw0AQnD3JlltKCluHQML+BCQFBY9Ackp6KpokDd9IJGiR+EHMK2JEweHwiGDILbqLzzLGlixc+W53Z+dmZwmtby0DmaitWkkEh9p/AnDiabo8/vh8dbFmCTUP68ifETBlIcZC6zMG5lX8IS7Kqzzy2dwlRTlzdTVAHnorEI1MwAKwvmDGbZX4yELckNZv1VnFRXlk/i2A6+xQBwCYwuVpUU4sgKHWfMoQAMeU2t0HPsH2MyzoJfIXDKT/YQBAUR75Rhj5C4B5QkTfAO6rTlPNXBDRojV1RU316yBzFm++xnnoXTPoINmUd11MLXhfwHpAiMzQhNap8UfbdFaDLhHbiX3nPYAMZMMgQ2ttnhn33kihl3YIZMekgfcu+s7StZX7/JCobdY2GiqRays73h0g6s+I+5apBpGBxG43EkTnDNjlArNiomcIsTSr3hTqB9JxwRTiGrqvAAAAAElFTkSuQmCC'
reset_ico = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAU1JREFUOE+VU0FuwjAQnAG+AFJPuC9peAnpE6rCGTgD6hOAlzS8BHOqlHyBZKu1cWJSIKpPibWe3ZmdodnmKSpaOx9mAGC+fgwug1SINwAJIBagFYjt9cuV/XixWhcOx5v8ROHBzodLsy6WQiz0kd65op5YVDRCmepvqP0D4DuKaReEQjdZ1U9EuAOQnWfDiQPUCQAaj45JoBKPGX8rkJSDEwUrnToGyJSnm/oO1xuQbZ6KYMF+OeGVtwrWCOPRnaj3znWKHQVHPirqug+N3QQYXPbt9XQCBBpujcTKfo72XY/aYqpfON4U38pFFf0PQO0Dz0Wm59no9RmAWReJUNQDkdg8sN4r5f0ZjWBxfd3YHJnbguYh7LVLzNAwZMQD1AGS6SMrN428lVU3neTGB3GYBMh6xNERrsNEEyxc+6At3G2cxWVEj0tn5JcQrl9M/90doFzS3gAAAABJRU5ErkJggg=='
send_ico = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAARdJREFUOE+dk0FSwkAQRf8PHEBzAlgkVZ5CuAlZJh4icgjDMtxEbmEVWTgH0OABkLZ6dMJEGKJkkaqp6v/m959u4srvZvUyoYxr/lfvCWegrP8MUGGEUQnhAhADcBIR80FAXwjord8QoC0SBgFWeBgvQJRdm4Jld6as2zzNTgBnhUrwxdaIZO8P6TGDoBBiKFgKWfuBq309Myy015qIzD4FJYFZB/ixbwHxU/PY6/PYsGmLdHpbNc89sWffAvT324UAm12RzM+Jtf7A/fQjvzMdwF3qnkzTjVfb2j1Xb9g8+ycAv9C5EuLeb8Gl72qDcxBX21cN8C1PNj5MuM+c/YsO4qoRnTpt59K+BB1ogBrk0LIN7sIQ4AvjqIY6fkzemAAAAABJRU5ErkJggg=='
layout = [
    [sg.T('提示：点击发送按钮后，将鼠标移至聊天发送窗口，\n等待5秒，消息会自动发送', text_color='red')],
    [sg.T('发送的消息')],
    [sg.Multiline('', tooltip='请输入要发送的消息', key='-mes-', no_scrollbar=True, size=(45, 3), )],
    [sg.T('发送的次数')],
    [sg.Input('', tooltip='请输入要发送消息的次数', key='-times-')],
    [sg.T()],
    [sg.B('', key='-send-', tooltip='发送', image_data=send_ico, image_size=(30, 25), button_color='white',
          auto_size_button=True, expand_x=True),
     sg.B('', key='-reset-', tooltip='重置', image_data=reset_ico, image_size=(30, 25), button_color='white',
          auto_size_button=True, expand_x=True),
     sg.B('', key='-quit-', tooltip='关闭', image_data=quit_ico, image_size=(30, 25), button_color='white',
          auto_size_button=True, expand_x=True)
     ],

]
window = sg.Window('消息发送助手', layout, icon=icon_path + r'\海豚_dolphin.ico',
                   force_toplevel=False, no_titlebar=True,
                   grab_anywhere=True
                   )

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-quit-':
        break
    if event == '-send-':
        if not values['-mes-']:
            sg.Popup('', '发送消息不能为空', no_titlebar=True)
            continue
        if not values['-times-']:
            sg.Popup('', '发送次数不能为空', no_titlebar=True)
            continue
    if event == '-reset-':
        if values['-mes-'] or values['-times-']:
            window['-mes-'].Update('')
            window['-times-'].Update('')
        continue
    m = MessageAttack()
    m.main(values['-mes-'], values['-times-'])
    window['-send-'].Update('发送中...')
    time.sleep(2)
    window['-send-'].Update('已发送')
    window['-send-'].Update('发送')
    sg.Popup('', '消息发送成功', no_titlebar=True)
window.close()
