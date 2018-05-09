let test = false
let t = 0
input.onButtonPressed(Button.A, () => {
    basic.clearScreen()
    test = false
    verif()
})
input.onButtonPressed(Button.B, () => {
    if (test) {
        radio.sendNumber(90)
    } else {
        radio.sendNumber(10)
    }
})
radio.onDataPacketReceived( ({ receivedNumber }) =>  {
    pins.servoWritePin(AnalogPin.P0, receivedNumber)
    if (receivedNumber == 90) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
function verif()  {
    t = 0
    while (t < 5 && input.lightLevel() > 200) {
        led.plot(t, 0)
        basic.pause(1000)
        t += 1
    }
    if (t > 4) {
        test = true
    }
}
radio.setGroup(1)
test = false
