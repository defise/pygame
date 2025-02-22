language = "ru"
sound_enabled = True

def get_language():
    return language

def switch_language():
    global language
    language = "en" if language == "ru" else "ru"

def toggle_volume():
    global sound_enabled
    sound_enabled = not sound_enabled
