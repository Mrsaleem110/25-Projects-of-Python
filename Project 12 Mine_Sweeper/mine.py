import random


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False
        self.revealed = False
        self.flagged = False
        self.adjacent_mines = 0

    def __str__(self):
        if self.flagged:
            return '🚩'
        elif not self.revealed:
            return '■'
        elif self.mine:
            return '💣'
        elif self.adjacent_mines > 0:
            return str(self.adjacent_mines)
        else:
            return ' '


class Board:
    def __init__(self, rows=8, cols=8, num_mines=10):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
        self.setup_board()

    def setup_board(self):
        # Place mines randomly
        mine_positions = random.sample(range(self.rows * self.cols), self.num_mines)
        for pos in mine_positions:
            r, c = divmod(pos, self.cols)
            self.board[r][c].mine = True

        # Calculate adjacent mine counts
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.board[r][c].mine:
                    self.board[r][c].adjacent_mines = self.count_adjacent_mines(r, c)

    def count_adjacent_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(row + 2, self.rows)):
            for c in range(max(0, col - 1), min(col + 2, self.cols)):
                if self.board[r][c].mine:
                    count += 1
        return count

    def reveal_cell(self, row, col):
        cell = self.board[row][col]
        if cell.revealed or cell.flagged:
            return
        cell.revealed = True

        if cell.mine:
            return "BOOM"
        elif cell.adjacent_mines == 0:
            # Recursively reveal neighbors
            for r in range(max(0, row - 1), min(row + 2, self.rows)):
                for c in range(max(0, col - 1), min(col + 2, self.cols)):
                    if not self.board[r][c].revealed:
                        self.reveal_cell(r, c)

    def toggle_flag(self, row, col):
        cell = self.board[row][col]
        if not cell.revealed:
            cell.flagged = not cell.flagged

    def print_board(self, reveal_all=False):
        print("   " + " ".join([str(c) for c in range(self.cols)]))
        print("  +" + "--" * self.cols + "+")
        for r in range(self.rows):
            row_str = f"{r} |"
            for c in range(self.cols):
                cell = self.board[r][c]
                if reveal_all:
                    if cell.mine:
                        row_str += '💣 '
                    else:
                        row_str += str(cell) + " "
                else:
                    row_str += str(cell) + " "
            print(row_str + "|")
        print("  +" + "--" * self.cols + "+")

    def check_win(self):
        for row in self.board:
            for cell in row:
                if not cell.revealed and not cell.mine:
                    return False
        return True


def main():
    print("🧨 Welcome to Minesweeper (CMD Edition) 🎮")
    board = Board()

    while True:
        board.print_board()
        move = input("Enter move (r c) or flag (f r c): ").split()

        if move[0] == 'f':
            _, r, c = move
            board.toggle_flag(int(r), int(c))
        else:
            r, c = map(int, move)
            result = board.reveal_cell(r, c)
            if result == "BOOM":
                board.print_board(reveal_all=True)
                print("💥 You hit a mine! Game Over.")
                break

        if board.check_win():
            board.print_board(reveal_all=True)
            print("🎉 Congratulations! You cleared the board!")
            break


if __name__ == "__main__":
    main()
