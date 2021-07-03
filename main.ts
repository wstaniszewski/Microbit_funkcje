input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("A")
    serial.writeLine("Test A")
})
function zapal_LED(num: number, num2: number) {
    led.plot(num, num2)
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("B")
    serial.writeLine("Test B")
})
let var_ = 4
zapal_LED(var_, 1)
input.onLogoDown(function on_logo_down() {
    basic.showString("Hello!")
})
