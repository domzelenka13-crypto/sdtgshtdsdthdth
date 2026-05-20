import time
import keyboard

if __name__ == '__main__':
    # Number of new tabs to open
    tabs_to_open = 10000
    keyboard.press_and_release('windows')
    keyboard.write('google')
    time.sleep(1)  # Wait for the search results to load
    keyboard.press_and_release('enter')
    time.sleep(1)  # Wait for the browser to open
    for _ in range(tabs_to_open):
        keyboard.press_and_release('ctrl+t')
        print ('good luck :D')
input('Press Enter to exit...')
