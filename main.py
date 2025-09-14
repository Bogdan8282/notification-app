import time
from plyer import notification

def remind_to_rest():
    while True:
        time.sleep(20 * 60)
        notification.notify(
            title="Перерва 🧘‍♂️",
            message="Час відпочити від комп'ютера!",
            timeout=10
        )

remind_to_rest()
