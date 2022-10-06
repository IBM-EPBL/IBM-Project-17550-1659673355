from gpiozero import Button, LED
led = LED(25)
button = Button(21)
while True:
button.wait_for_press()
led.on()
print("Pressed")

button.wait_for_release()
led.off()
print("Released")
