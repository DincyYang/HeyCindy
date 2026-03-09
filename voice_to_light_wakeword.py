# voice_to_light_wakeword.py
from wake_word import WakeWordDetector
from command import execute
from command_listener import listen_for_command
import sys
import time
import numpy as np
import simpleaudio as sa
import logging
import threading
from normalizer import normalize_command
from cloud_client import send_command
import os

# ========= Configuration =========
ACCESS_KEY = "b9uFY0Z2mfDVvhNNa9p3DxHzEWL5T/yHaS+NqIO7/KQBoBmKWJJugA=="
KEYWORD_PATH = "Hey-Cindy_en_mac_v4_0_0/Hey-Cindy_en_mac_v4_0_0.ppn"
DEVICE_INDEX = None  # system default mic
# ==================================

# ========= Logging =========
logging.basicConfig(
    filename="test_run.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
# ============================

# ========= Beep =========
def play_beep():
    frequency = 800  # Hz
    duration = 0.12  # seconds (slightly shorter)
    sample_rate = 44100

    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t)

    audio = (tone * 32767).astype(np.int16)
    sa.play_buffer(audio, 1, 2, sample_rate).wait_done()
# ==========================


def handle_wake(detector: WakeWordDetector):
    detector.pause_event.set()

    print("🟢 Wake word detected!")
    logging.info("Wake word detected")

    play_beep()
    time.sleep(0.2)
    print("🔔 Speak now: on/off/quit")

    raw_text = listen_for_command(timeout=3)
    logging.info(f"Raw text heard: {raw_text!r}")

    if not raw_text:
        print("😶 No speech recognized")
        logging.info("No speech recognized")
        detector.pause_event.clear()
        return

    # 1) 系统命令优先处理
    if raw_text.strip().lower() in ("quit", "exit", "stop"):
        print("👋 Quitting...")
        logging.info("Quit command received")
        sys.exit(0)

    # 2) 归一化
    result = normalize_command(raw_text)

    print(f"🎧 raw_text: {raw_text}")
    print(f"🧠 normalized: {result.normalized} | conf={result.confidence} | reason={result.reason}")
    print(f"🧹 cleaned: {result.cleaned_text}")

    logging.info(
        f"Normalized: {result.normalized} conf={result.confidence} "
        f"reason={result.reason} cleaned={result.cleaned_text!r}"
    )

    # 3) on/off 执行
    if result.normalized in ("on", "off"):
        print(f"👉 Executing: {result.normalized}")

        # 本地执行
        should_continue = execute(result.normalized)

        # 云端记录（如果 cloud_client 还不支持这些参数，先只发 result.normalized）
        try:
            resp = send_command(
                result.normalized,
                raw_text=raw_text,
                confidence=result.confidence,
                reason=result.reason,
                source="voice"
            )
            print("☁️ Cloud recorded:", resp)
        except TypeError:
            # 兼容旧版 send_command(cmd)
            resp = send_command(result.normalized)
            print("☁️ Cloud recorded (legacy):", resp)
        except Exception as e:
            print("☁️ Cloud send failed:", e)

        if should_continue is False:
            sys.exit(0)

    # 4) unknown 不执行，只记录
    else:
        print("⚠️ No action taken (unknown).")
        logging.warning(
            f"Unknown command: raw={raw_text!r} cleaned={result.cleaned_text!r} reason={result.reason}"
        )

    # 5) 恢复 wake word 监听
    detector.pause_event.clear()


def main():
    print("Voice to light with wake word started")
    logging.info("Program started")

    detector = WakeWordDetector(
        access_key=ACCESS_KEY,
        keyword_path=KEYWORD_PATH,
        device_index=DEVICE_INDEX
    )

    threading.Thread(target=detector.listen, daemon=True).start()

    while True:
        detector.wake_event.wait()
        detector.wake_event.clear()
        handle_wake(detector)


if __name__ == "__main__":
    import platform, sys
    logging.info(f"Python: {sys.version}")
    logging.info(f"Platform: {platform.platform()}")
    main()