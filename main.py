distance = 0

def on_button_pressed_a():
    doSomething(10)
input.on_button_pressed(Button.A, on_button_pressed_a)

def doSomething(num: number):
    global distance
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    led.plot_bar_graph(distance, 100)
    if distance > num:
        pins.digital_write_pin(DigitalPin.P2, 1)
    else:
        pins.digital_write_pin(DigitalPin.P2, 0)

def on_button_pressed_b():
    doSomething(100)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
