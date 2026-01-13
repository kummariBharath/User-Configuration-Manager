def add_setting(settings: dict, pair: tuple):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: dict, pair: tuple):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings: dict, key: str):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"


def view_settings(settings: dict):
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result

test_settings = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled"
}

print(add_setting(test_settings, ("Volume", "High")))
print(update_setting(test_settings, ("Theme", "Light")))
print(delete_setting(test_settings, "language"))
print(view_settings(test_settings))
