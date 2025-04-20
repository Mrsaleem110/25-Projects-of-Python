import streamlit as st
import math

# Initialize session state
if 'board' not in st.session_state:
    st.session_state.board = [' '] * 9
    st.session_state.game_over = False
    st.session_state.winner = None

# Utility functions
def print_board():
    for i in range(3):
        st.write(st.session_state.board[i*3:(i+1)*3])

def check_winner(player):
    b = st.session_state.board
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(b[i] == player for i in combo) for combo in wins)

def available_moves():
    return [i for i, spot in enumerate(st.session_state.board) if spot == ' ']

def minimax(board, is_maximizing):
    if check_static_winner(board, 'O'):
        return {'score': 1}
    elif check_static_winner(board, 'X'):
        return {'score': -1}
    elif ' ' not in board:
        return {'score': 0}

    if is_maximizing:
        best = {'score': -math.inf}
        for move in available_moves_static(board):
            board[move] = 'O'
            sim_score = minimax(board, False)
            board[move] = ' '
            sim_score['position'] = move
            if sim_score['score'] > best['score']:
                best = sim_score
        return best
    else:
        best = {'score': math.inf}
        for move in available_moves_static(board):
            board[move] = 'X'
            sim_score = minimax(board, True)
            board[move] = ' '
            sim_score['position'] = move
            if sim_score['score'] < best['score']:
                best = sim_score
        return best

def check_static_winner(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def available_moves_static(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def ai_move():
    result = minimax(st.session_state.board.copy(), True)
    if result.get('position') is not None:
        st.session_state.board[result['position']] = 'O'

def reset_game():
    st.session_state.board = [' '] * 9
    st.session_state.game_over = False
    st.session_state.winner = None

# --- Streamlit UI ---

st.title("🧠 Tic Tac Toe with AI")
st.markdown("Play as **X**. The AI plays as **O**.")

if st.button("🔄 Restart Game"):
    reset_game()

# Draw the board as buttons
cols = st.columns(3)
for i in range(9):
    col = cols[i % 3]
    if st.session_state.board[i] == ' ' and not st.session_state.game_over:
        if col.button(" ", key=i):
            st.session_state.board[i] = 'X'
            if check_winner('X'):
                st.session_state.game_over = True
                st.session_state.winner = 'You (X)'
            elif ' ' not in st.session_state.board:
                st.session_state.game_over = True
                st.session_state.winner = 'Draw'
            else:
                ai_move()
                if check_winner('O'):
                    st.session_state.game_over = True
                    st.session_state.winner = 'AI (O)'
                elif ' ' not in st.session_state.board:
                    st.session_state.game_over = True
                    st.session_state.winner = 'Draw'
    else:
        col.markdown(f"### {st.session_state.board[i]}")

# Game result
if st.session_state.game_over:
    if st.session_state.winner == 'Draw':
        st.success("It's a draw! 😐")
    else:
        st.success(f"{st.session_state.winner} wins! 🎉")

