function validatePIN (pin) {
    const regex1 = '/[0-9]{4}/'
    const regex2 = '/[0-9]{6}/'
    return regex1.test(pin) || regex2.test(pin)
}