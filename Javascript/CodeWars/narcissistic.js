function narcissistic(value) {
  sum = 0
  stringValue = value.toString()
  for (let i = 0; i < stringValue.length; i++) {
    sum += Math.pow(parseInt(stringValue[i]), stringValue.length)
  }
  return (sum === value)
}
