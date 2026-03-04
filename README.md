# User Configuration Manager ⚙️

Welcome to the **User Configuration Manager**! This is a beginner-friendly Python project designed to help you understand how to manage data using **Dictionaries**, **Functions**, and **User Input**.

Think of this program as the "Settings" app on your phone. You can change your theme, turn notifications on or off, or add new preferences.

---

## 🚀 Features

1.  **View Settings**: See all current configurations.
2.  **Add Setting**: Create a new preference (e.g., "Brightness": "High").
3.  **Update Setting**: Change an existing preference.
4.  **Delete Setting**: Remove a preference you no longer need.

---

## 🧠 What You Will Learn

By exploring this code, you will learn about:

### 1. Python Dictionaries (`dict`)
The core of this program is a dictionary named `user_settings`. Dictionaries store data in **Key-Value** pairs.
*   **Key**: The setting name (e.g., "theme").
*   **Value**: The setting choice (e.g., "dark").

```python
user_settings = {
    "theme": "dark",
    "notifications": "enabled"
}
```

### 2. Functions
We use functions to organize code into reusable blocks.
*   `add_setting`: Checks if a key exists, then adds it.
*   `update_setting`: Modifies an existing key.
*   `delete_setting`: Removes a key using the `del` keyword.

### 3. String Manipulation
To make the program smart, we handle text carefully:
*   `.lower()`: We convert inputs to lowercase so "Dark", "DARK", and "dark" are treated the same.
*   `.strip()`: Removes accidental spaces at the start or end of your input.
*   `.capitalize()`: Makes the output look neat (e.g., "theme" becomes "Theme").

### 4. The Main Loop (`while True`)
The program runs inside a `while True` loop. This creates an interactive menu that keeps running until you choose to **Exit**.

---

## 📝 Code Walkthrough

### Adding a Setting
We pass the settings dictionary and a **Tuple** `(key, value)` to the function.
```python
def add_setting(settings, pair):
    key, value = pair  # Unpacking the tuple
    if key in settings:
        return "Error: Exists already"
    settings[key] = value
    return "Success!"
```

### The Menu System
We use `input()` to get commands from the user.
```python
choice = input("Enter your choice (1-5): ")
if choice == '1':
    # Logic to add setting
elif choice == '5':
    break # Exits the loop
```

---

## 💻 How to Run

1.  Ensure you have Python installed.
2.  Open your terminal or command prompt.
3.  Navigate to the folder containing the file.
4.  Run the command:
    ```bash
    python "User Configuration Manager.py"
    ```

## 🎮 Example Interaction

```text
--- MENU ---
1. Add Setting
2. Update Setting
3. Delete Setting
4. View All Settings
5. Exit
Enter your choice (1-5): 1
------------------------------
Enter setting name: Volume
Enter value for 'Volume': 100
Setting 'volume' added with value '100' successfully!   
```  
