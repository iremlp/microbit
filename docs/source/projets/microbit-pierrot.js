let note = 0
let index = 0
let test = false
let musique: number[] = []
input.onButtonPressed(Button.A, () => {
    basic.showLeds(`
        . . # . .
        . . # # #
        . . # . .
        . # # . .
        . # # . .
        `)
    for (let valeur of musique) {
        radio.sendNumber(valeur)
        basic.pause(520)
    }
})
input.onButtonPressed(Button.B, () => {
    basic.clearScreen()
    test = false
    index = 0
    note = 262
    test = true
    while (test) {
        if (input.pinIsPressed(TouchPin.P0)) {
            note = 262
            testNote()
        } else if (input.pinIsPressed(TouchPin.P1)) {
            note = 294
            testNote()
        } else if (input.pinIsPressed(TouchPin.P2)) {
            note = 330
            testNote()
        }
    }
})
function testNote() {
    basic.clearScreen()
    radio.sendNumber(note)
    if (musique[index] == note) {
        basic.showIcon(IconNames.Happy)
        basic.pause(100)
        basic.clearScreen()
        index += 1
    } else {
        basic.showIcon(IconNames.Sad)
        test = false
    }
    if (index == 11) {
        succes()
    }
}
function succes() {
    for (let i = 0; i < 4; i++) {
        basic.showIcon(IconNames.Heart)
        basic.pause(100)
        basic.showIcon(IconNames.SmallHeart)
        basic.pause(100)
    }
    basic.showString("temp")
}
radio.onDataPacketReceived(({ receivedNumber }) => {
    music.playTone(receivedNumber, music.beat(BeatFraction.Half))
})
radio.setGroup(2)
musique = [262, 262, 262, 294, 330, 294, 262, 330, 294, 294, 262]
