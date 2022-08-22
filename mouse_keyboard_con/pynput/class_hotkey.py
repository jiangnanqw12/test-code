from pynput.keyboard import HotKey, Key, KeyCode, Listener,Controller


# The function called when a hotkey is pressed
def on_activate():

    print('Hotkey pressed')


# A helper function when delegating on_press/on_release events
def for_canonical(f):
    Con1 = Controller()
    Con1.press(Key.space)
    #Con1.release(Key.space)
    return lambda k: f(l.canonical(k))


# The hotkey itself
hotkey = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='r')],  # A list of the keys to look for
    on_activate  # The function to call when a hotkey is pressed
)

# The typical pynput listener that is calling functions on hotkey using `for_canonical`
with Listener(
    on_press=for_canonical(hotkey.press),
    on_release=for_canonical(hotkey.release)
) as l:
    l.join()