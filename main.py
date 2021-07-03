def on_button_pressed_a():
    basic.show_string("A")
    serial.write_line("Test A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def zapal_LED(num: number, num2: number):
    led.plot(num, num2)

def on_button_pressed_b():
    basic.show_string("B")
    serial.write_line("Test B")
input.on_button_pressed(Button.B, on_button_pressed_b)

var_ = 4
zapal_LED(var_, 1)

def on_logo_down():
    basic.show_string("Hello!")
input.on_logo_down(on_logo_down)
