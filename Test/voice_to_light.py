# voice_to_light.py
from command import execute

def get_command():
    return input("🧠 Command: ").strip()

if __name__ == "__main__":
    print("💬 Voice to light controller started")
    while True:
        cmd = get_command()
        if not execute(cmd):
            break
