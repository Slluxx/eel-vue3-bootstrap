import eel
eel.init('web')

@eel.expose
def print_string(text):
    print(text)
    return True

eel.fromPy_alert("Eel started")
eel.start('index.html', size=(640, 320))