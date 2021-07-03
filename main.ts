let distance = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    doSomething(10)
})
function doSomething(num: number) {
    
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.Centimeters)
    led.plotBarGraph(distance, 100)
    if (distance > num) {
        pins.digitalWritePin(DigitalPin.P2, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
    
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    doSomething(100)
})
basic.forever(function on_forever() {
    
})
