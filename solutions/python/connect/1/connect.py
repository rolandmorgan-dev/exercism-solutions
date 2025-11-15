class ConnectGame:
    def __init__(self, board):
        self.board = board.replace(" ", "").split("\n")

    def get_winner(self):
        board = self.board
        x_possible = o_possible = False
        x_left = o_top = []
        
        height = len(board)
        width = len(board[0])
        
        # check if X is a possible winner, save X positions on the left
        if any(board[x][0]=="X" for x in range(height)):
            if any(board[x][-1]=="X" for x in range(height)):
                x_possible = True
                x_left = [x for x in range(height) if board[x][0]=="X"]
        
        # check if O is a possible winner, save O positions on the top
        if any(board[0][o]=="O" for o in range(width)):
            if any(board[height-1][o]=="O" for o in range(width)):
                o_possible = True
                o_top = [o for o in range(width) if board[0][o]=="O"]
        
        for x in x_left:
            #p = position on x line
            p = 0
            x_been = set()
            while x_possible:
                # check if X has won (did we arrive from start to end)
                if p == width-1:
                    return "X"
                
                x_been.add((x,p))
                
                current_x = x
                current_p = p
                
                p_top_end = p+2 if p+2 < width else width
                p_bot_start = p-1 if p-1 >= 0 else 0
                
                # X topside check
                if x-1 >= 0:
                    next_loop = False
                    for top in range(p, p_top_end):
                        if board[x-1][top] == "X" and (x-1, top) not in x_been:
                            x -= 1
                            p = top
                            next_loop = True
                            break
                    if next_loop: continue
                
                # X in line, before/after current position
                if p-1 >= 0:
                    if board[x][p-1] == "X"and (x, p-1) not in x_been:
                        p = p-1
                        continue
                
                if p+1 < width:
                    if board[x][p+1] == "X" and (x, p+1) not in x_been:
                        p = p+1
                        continue
                
                # X bottom side check
                if x+1 < height:
                    next_loop = False
                    for bot in range(p_bot_start, p+1):
                        if board[x+1][bot] == "X" and (x+1, bot) not in x_been:
                            x += 1
                            p = bot
                            break
                    if next_loop: continue
                
                # check x & p change, break if no change
                if current_x == x and current_p == p:
                    x_possible = False
        
        
        for p in o_top:
            #p = position on o line
            o = 0
            o_been = []
            while o_possible:
                # check if O has won (did we arrive from top to bottom)
                if o == height-1:
                    return "O"
                
                o_been.append((o,p))
                
                current_o = o
                current_p = p
                
                p_top_end = p+2 if p+2 < width else width
                p_bot_start = p-1 if p-1 >= 0 else 0
                # O topside check
                if o-1 >= 0:
                    next_loop = False
                    for top in range(p, p_top_end):
                        if board[o-1][top] == "O" and (o-1, top) not in o_been:
                            o -= 1
                            p = top
                            next_loop = True
                            break
                    if next_loop: continue
                
                # O in line, before/after current position
                if p-1 >= 0:
                    if board[o][p-1] == "O"and (o, p-1) not in o_been:
                        p = p-1
                        continue
                
                if p+1 < width:
                    if board[o][p+1] == "O" and (o, p+1) not in o_been:
                        p = p+1
                        continue
                
                # O bottom side check
                if o+1 < height:
                    next_loop = False
                    for bot in range(p_bot_start, p+1):
                        if board[o+1][bot] == "O" and (o+1, bot) not in o_been:
                            o += 1
                            p = bot
                            break
                    if next_loop: continue
                
                # check o & p change, break if no change
                if current_o == o and current_p == p:
                    o_possible = False
            
        return ""