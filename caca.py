import pyautogui
import time
import keyboard
import win32api
import win32con

def click():
    """Simulate right mouse click"""
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

print("Minecraft Fishing Bot")
print("Press 'q' to quit the program")
print("Starting in 5 seconds...")
time.sleep(5)  # Give time to switch to Minecraft window

try:
    while not keyboard.is_pressed('q'):  # Press 'q' to quit
        # Cast the fishing rod
        click()
        print("Cast fishing rod")
        
        # Wait for initial splash
        time.sleep(1)
        
        # Wait for fish to bite (you may need to adjust these values)
        caught = False
        while not caught and not keyboard.is_pressed('q'):
            # Look for red pixel color that indicates fishing bob went under
            pixel = pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)
            if pixel[0] > 140:  # Red component threshold
                click()
                print("Fish caught!")
                caught = True
                time.sleep(2)  # Wait before casting again
            time.sleep(0.1)  # Small delay between checks

except KeyboardInterrupt:
    print("\nBot stopped by user")
except Exception as e:
    print(f"\nAn error occurred: {e}")

print("Bot terminated")