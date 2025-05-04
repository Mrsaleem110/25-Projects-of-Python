def minimax(board, depth, is_maximizing):
    if game_over(board):
        return score  # 1, -1, or 0 depending on winner

    if is_maximizing:
        best_score = -inf
        for move in available_moves(board):
            board.make_move(move, AI)
            score = minimax(board, depth + 1, False)
            board.undo_move(move)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = +inf
        for move in available_moves(board):
            board.make_move(move, HUMAN)
            score = minimax(board, depth + 1, True)
            board.undo_move(move)
            best_score = min(score, best_score)
        return best_score
