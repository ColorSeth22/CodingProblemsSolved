function findNextSquare(sq) {
  if(!Math.sqrt(sq).toString().includes('.')){
    num = Math.sqrt(sq)
    num += 1
    return Math.pow(num, 2)
  }
  return -1;
}