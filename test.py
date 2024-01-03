import time
from pythonray import *

def test_ray():
    screen_name = "Ray Python Test"
    screen_color = "blue"
    ray().show_app()
    ray().new_screen(screen_name)
    first_message = ray(f"You should see a new screen titled {screen_name} with a {screen_color} background")
    ray().screen_color(screen_color)
    delay_time = 3
    second_message = ray(f"In {delay_time} seconds, you should see this message blink red and then see both messages disappear.")
    time.sleep(delay_time)
    second_message.red()
    time.sleep(0.5)
    second_message.gray()
    time.sleep(0.5)
    second_message.red()
    time.sleep(0.5)
    second_message.gray()
    time.sleep(0.5)
    second_message.red()
    time.sleep(1)
    second_message.remove()
    first_message.remove()

    ray().screen_green()
    ray("Hoo-ray!").green()
    ray().ban().green()
    time.sleep(1)
    ray().confetti()

test_ray()