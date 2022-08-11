from pynput.keyboard import Key, Controller

Con1 = Controller()

# Press and release space
Con1.press(Key.space)
Con1.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
Con1.press('a')
Con1.release('a')

# Type two upper case As
Con1.press('A')
Con1.release('A')
with Con1.pressed(Key.shift):
    Con1.press('a')
    Con1.release('a')

# Type 'Hello World' using the shortcut type method
Con1.type('Hello World')