/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  for (i = 0; i < board.length; i++) {
    let nums = [];
    for (x = 0; x < board[i].length; x++) {
      if (!nums.includes(board[i][x])) {
        nums.push(board[i][x]);
      } else if (board[i][x] != ".") {
        return false;
      }
    }
  }
  let ThreeByThree = [];
  let OtherThree = [];
  let LastThree = [];
  for (z = 0; z < board.length; z++) {
    for (c = 0; c < 3; c++) {
      if (!ThreeByThree.includes(board[z][c])) {
        ThreeByThree.push(board[z][c]);
      } else if (board[z][c] != ".") {
        return false;
      }
    }
    for (c = 3; c < 6; c++) {
      console.log(OtherThree, board[z][c]);
      if (!OtherThree.includes(board[z][c])) {
        OtherThree.push(board[z][c]);
      } else if (board[z][c] != ".") {
        return false;
      }
    }
    for (c = 6; c < board.length; c++) {
      if (!LastThree.includes(board[z][c])) {
        LastThree.push(board[z][c]);
      } else if (board[z][c] != ".") {
        return false;
      }
    }
    if (z === 2 || z === 5 || z === 8) {
      ThreeByThree = [];
      LastThree = [];
      OtherThree = [];
    }
  }
  for (i = 0; i < board.length; i++) {
    let column = [];
    for (x = 0; x < board.length; x++) {
      if (!column.includes(board[x][i])) {
        column.push(board[x][i]);
      } else if (board[x][i] != ".") {
        return false;
      }
    }
  }
  return true;
};