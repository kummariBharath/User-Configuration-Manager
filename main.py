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

def main():
    # Initialize with some default settings
    user_settings = {
        "theme": "dark",
        "notifications": "enabled"
    }
    
    print("="*50)
    print("   USER CONFIGURATION MANAGER")
    print("="*50)

    while True:
        print("\n--- MENU ---")
        print("1. Add Setting")
        print("2. Update Setting")
        print("3. Delete Setting")
        print("4. View All Settings")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        print("-" * 30)

        if choice == '1':
            key = input("Enter setting name: ").strip()
            if not key:
                print("Setting name cannot be empty.")
                continue
            value = input(f"Enter value for '{key}': ").strip()
            print(add_setting(user_settings, (key, value)))
            
        elif choice == '2':
            key = input("Enter setting name to update: ").strip()
            value = input(f"Enter new value for '{key}': ").strip()
            print(update_setting(user_settings, (key, value)))
            
        elif choice == '3':
            key = input("Enter setting name to delete: ").strip()
            print(delete_setting(user_settings, key))
            
        elif choice == '4':
            print(view_settings(user_settings))
            
        elif choice == '5':
            print("Exiting Configuration Manager. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main() 
