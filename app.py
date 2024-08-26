# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello, Azure Web Apps!"

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=8000)

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return '''
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport
#         content="width=device-width, initial-scale=1.0">
#         <title>Hello, Azure Web Apps!</title>
#         <style>
#             body {
#                 margin: 0;
#                 padding: 0;
#                 height: 100vh;
#                 display: flex;
#                 justify-content: center;
#                 align-items: center;
#                 background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
#                 font-family: 'Arial', sans-serif;
#                 overflow: hidden;
#             }
#             h1 {
#                 font-size: 4rem;
#                 color: white;
#                 animation: fadeIn 2s ease-in-out;
#             }
#             @keyframes fadeIn {
#                 0% {
#                     opacity: 0;
#                     transform: scale(0.8);
#                 }
#                 100% {
#                     opacity: 1;
#                     transform: scale(1);
#                 }
#             }
#             .floating-stars {
#                 position: absolute;
#                 width: 100%;
#                 height: 100%;
#                 top: 0;
#                 left: 0;
#                 pointer-events: none;
#             }
#             .floating-stars div {
#                 position: absolute;
#                 width: 5px;
#                 height: 5px;
#                 background: white;
#                 border-radius: 50%;
#                 opacity: 0.7;
#                 animation: float 5s infinite ease-in-out;
#             }
#             @keyframes float {
#                 0% {
#                     transform: translateY(0) rotate(0deg);
#                     opacity: 0;
#                 }
#                 50% {
#                     opacity: 1;
#                 }
#                 100% {
#                     transform: translateY(-200px) rotate(360deg);
#                     opacity: 0;
#                 }
#             }
#         </style>
#     </head>
#     <body>
#         <h1>Hello, Azure Web Apps!</h1>
#         <div class="floating-stars">
#             <div style="left: 20%; animation-duration: 4s;"></div>
#             <div style="left: 50%; animation-duration: 6s;"></div>
#             <div style="left: 80%; animation-duration: 8s;"></div>
#         </div>
#     </body>
#     </html>
#     '''

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=8000)


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the game board
def initialize_board():
    return [['' for _ in range(3)] for _ in range(3)]

# Check for a winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        board = request.form.getlist("board")
        board = [board[i:i+3] for i in range(0, len(board), 3)]
    else:
        board = initialize_board()
    
    winner = check_winner(board)
    if winner:
        return render_template("index.html", board=board, winner=winner)
    
    return render_template("index.html", board=board, winner=None)

@app.route("/move/<int:row>/<int:col>")
def move(row, col):
    board = request.args.getlist("board")
    board = [board[i:i+3] for i in range(0, len(board), 3)]
    
    player = 'X' if board[row][col] == '' else ''
    board[row][col] = player
    
    return redirect(url_for('index', board=sum(board, [])))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)




