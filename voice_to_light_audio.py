import sounddevice as sd
import numpy as np
import time

from command import execute

# ========= 配置区 =========
SAMPLE_RATE = 16000
CHANNELS = 1
DEVICE_INDEX = 3   # MacBook Air Microphone
VOLUME_THRESHOLD = 0.02
COOLDOWN_SECONDS = 1.5
# ==========================

last_trigger_time = 0
state_on = False


def audio_callback(indata, frames, time_info, status):
    global last_trigger_time, state_on

    if status:
        print(status)

    # 计算音量
    volume = np.linalg.norm(indata)

    now = time.time()
    if volume > VOLUME_THRESHOLD and now - last_trigger_time > COOLDOWN_SECONDS:
        last_trigger_time = now

        if state_on:
            print("🧠 Command: OFF")
            execute("off")
        else:
            print("🧠 Command: ON")
            execute("on")

        state_on = not state_on


def main():
    print("💬 Voice to light controller started")

    with sd.InputStream(
        device=DEVICE_INDEX,
        channels=CHANNELS,
        samplerate=SAMPLE_RATE,
        callback=audio_callback,
    ):
        while True:
            time.sleep(0.1)


if __name__ == "__main__":
    main()