from pynput import keyboard

def on_press(key):
    vk = key.vk if hasattr(key, 'vk') else key.value.vk
    print('vk =', vk)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()