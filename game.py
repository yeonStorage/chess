import pygame
import sys

pygame.init()

#set up a screen
display_width = 600
display_height = 630

chess_board = pygame.display.set_mode((display_width, display_height))

# images for setting up a board
box1 = pygame.image.load('resource/img/board/box1.png')
box2 = pygame.image.load('resource/img/board/box2.png')

# variable for turn
# turn % 2 == 0 means user, turn % 2 == 1 means opposite user
turn = 0

#variable for user's score
score_0 = 0
#variable for opposite user's score
score_1 = 0

#set up a board
board = []
index = 0
for i in range(8):
    for j in range(8):
        if j == 1:
            board.append([index, (i*75+10, j*75+10), "pawn"])
        elif j == 6:
            board.append([index, (i*75+10, j*75+10), "o_pawn"])
        elif (j == 0 and i == 0) or (j == 0 and i == 7):
            board.append([index, (i*75+10, j*75+10), "rook"])
        elif (j == 7 and i == 0) or (j == 7 and i == 7):
            board.append([index, (i*75+10, j*75+10), "o_rook"])
        elif (j == 0 and i == 1) or (j == 0 and i == 6):
            board.append([index, (i*75+10, j*75+10), "knight"])
        elif (j == 7 and i == 1) or (j == 7 and i == 6):
            board.append([index, (i*75+10, j*75+10), "o_knight"])
        elif (j == 0 and i == 2) or (j == 0 and i == 5):
            board.append([index, (i*75+10, j*75+10), "bishop"])
        elif (j == 7 and i == 2) or (j == 7 and i == 5):
            board.append([index, (i*75+10, j*75+10), "o_bishop"])
        elif j == 0 and i == 3:
            board.append([index, (i*75+10, j*75+10), "king"])
        elif j == 7 and i == 3:
            board.append([index, (i*75+10, j*75+10), "o_king"])
        elif j == 0 and i == 4:
            board.append([index, (i*75+10, j*75+10), "queen"])
        elif j == 7 and i == 4:
            board.append([index, (i*75+10, j*75+10), "o_queen"])
        else:
            board.append([index, (i*75+10, j*75+10), "none"])
        index = index + 1

        
#locate board
def board_locate(img, x, y):
    chess_board.blit(img, (x, y))

#varible for checking if the game finished or not
finished = False

#list for getting positions of clicked mouse
location_move_x = []
location_move_y = []

#number of clicked mouse
list_total = 0

def check_state(x, y):
    x = ((x // 75) * 75)+10
    y = ((y // 75) * 75)+10
    #보드내의 좌표 클릭하면 state 나오게
    for i in range(63):
        if board[i][1] == (x, y):
            return board[i][2]

def check_index(x, y):
    x = ((x // 75) * 75)+10
    y = ((y // 75) * 75)+10
    #보드내의 좌표 클릭하면 index 나오게
    for i in range(63):
        if board[i][1] == (x, y):
            return board[i][0]

def score(after_state):
    global score_0
    global score_1

    if "pawn" in after_state:
        if turn % 2 == 1:
            score_0 = score_0+1
        elif turn % 2 == 0:
            score_1 = score_1+1
    elif "rook" in after_state:
        if turn % 2 == 1:
            score_0 = score_0+5
        elif turn % 2 == 0:
            score_1 = score_1+5
    elif "knight" in after_state or "bishop" in after_state:
        if turn % 2 == 1:
            score_0 = score_0+3
        elif turn % 2 == 0:
            score_1 = score_1+3
    elif "queen" in after_state:
        if turn % 2 == 1:
            score_0 = score_0+9
        elif turn % 2 == 0:
            score_1 = score_1+9     
    elif "king" in after_state:
        if turn % 2 == 1:
            score_0 = finished
        elif turn % 2 == 0:
            score_1 = finished

#locate board
def img_locate(img, x, y):
    chess_board.blit(img, (x, y))

#chess rule
def move(before_state, before_x, before_y, after_state, after_x, after_y):
    width = abs(after_x-before_x)
    height = abs(after_y-before_y)
    icon = "none"
    global turn

    if "pawn" in before_state:
        # print("ok")
        # pawn_ex = pygame.image.load('resource/img/user/pawn.png')
        # chess_board.blit(pawn_ex, (after_x, after_y))
        # pawn_ex  = Pawn(1, after_x, after_y)
        # board[(after_x // 75)*(after_y // 75)] = "pawn"
        if 37.5 <= height <= 75+37.5:
            if before_state == "pawn":
                icon = "pawn"
                if turn % 2 == 0:
                    board[check_index(before_x, before_y)][2] = "none"
                    board[check_index(after_x, after_y)][2] = icon
            else:
                icon = "o_pawn"
                if turn % 2 == 1:
                    board[check_index(before_x, before_y)][2] = "none"
                    board[check_index(after_x, after_y)][2] = icon
        #width나 height가 <150이면 이동
    elif "rook" in before_state:
        if width // 37.5== 0:
            if before_state == "rook":
                icon = "rook"
                if turn % 2 == 0:
                    board[check_index(before_x, before_y)][2] = "none"
                    board[check_index(after_x, after_y)][2] = icon
            else:
                icon = "o_rook"
                if turn % 2 == 1:
                    board[check_index(before_x, before_y)][2] = "none"
                    board[check_index(after_x, after_y)][2] = icon
    elif before_state == "knight":
        if (37.5 < width < 75+37.5 and 75+37.5 < height < 150+37.5) or (37.5 < height < 75+37.5 and 75+37.5 < width < 150+37.5):
            if before_state == "knight":
                icon = "knight"
                if turn % 2 == 0:
                    board[check_index(before_x, before_y)][2] = "none"
                    board[check_index(after_x, after_y)][2] = icon
            else:
                icon = "o_knight"
                if turn % 2 == 1:
                    board[check_index(before_x, before_y)][2] = "none"
                    board[check_index(after_x, after_y)][2] = icon
    elif before_state == "bishop":
        if width // 75 == height // 75:
            if before_state == "bishop":
                icon = "bishop"
                if turn % 2 == 0:
                    board[check_index(before_x, before_y)][2] = "none"
                    board[check_index(after_x, after_y)][2] = icon
            else:
                icon = "o_bishop"
                if turn % 2 == 1:
                    board[check_index(before_x, before_y)][2] = "none"
                    board[check_index(after_x, after_y)][2] = icon
    elif before_state == "king":
        if 37.5 < width < 37.5+70 and 37.5 < height < 75+37.5:
            if before_state == "king":
                icon = "king"
                if turn % 2 == 0:
                    board[check_index(before_x, before_y)][2] = "none"
                    board[check_index(after_x, after_y)][2] = icon
            else:
                icon = "o_king"
                if turn % 2 == 1:
                    board[check_index(before_x, before_y)][2] = "none"
                    board[check_index(after_x, after_y)][2] = icon
    elif before_state == "queen":
        if before_state == "queen":
            icon = "queen"
            if turn % 2 == 0:
                board[check_index(before_x, before_y)][2] = "none"
                board[check_index(after_x, after_y)][2] = icon
        else:
            icon = "o_queen"
            if turn % 2 == 1:
                board[check_index(before_x, before_y)][2] = "none"
                board[check_index(after_x, after_y)][2] = icon
    else:
        pass
    #rook일 경우 x 좌표 값이 다르면
    #knight일 경우 가정문 4개 300, 150
    #bishop일 경우 x, y각각 <150으로 증가
    #queen일 경우 pass
    #King일 경우 알아서
    score(after_state)
    print(turn)
    turn = turn + 1

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # 마우스 두 번 클릭으로 말 움직임
        if event.type == pygame.MOUSEBUTTONDOWN:
            # list에 append 0, 1로 인덱싱 하고 초기화

            #get mouse clicked positions
            location_x = pygame.mouse.get_pos()[0]
            location_y = pygame.mouse.get_pos()[1]
                                                                                                                                                                                                                                                 
            location_move_x.append(location_x)
            location_move_y.append(location_y)

            before_state =check_state(location_move_x[0], location_move_y[0])

            list_total = list_total + 1

            if list_total >= 2:
                after_state =check_state(location_move_x[1], location_move_y[1])
                move(before_state, location_move_x[0], location_move_y[0], after_state, location_move_x[1], location_move_y[1])
                location_move_x.clear()
                location_move_y.clear()
                list_total = 0
            else:
                pass

    #set up board
    chess_board.fill((255, 255, 255))
    for i in range(8):
        for j in range(8):
            #if i is even
            if i % 2 == 1:
                if j % 2 == 0:
                    img_locate(box1, j*75, i*75)
                else:
                    img_locate(box2, j*75, i*75)
            else:
                if j % 2 == 0:
                    img_locate(box2, j*75, i*75)
                else:
                    img_locate(box1, j*75, i*75)

    for i in range(64):
        if board[i][2] == "pawn":
            pawn = pygame.image.load('resource/img/user/pawn.png')
            chess_board.blit(pawn, board[i][1])
        elif board[i][2] == "o_pawn":
            pawn = pygame.image.load('resource/img/opposite/pawn.png')
            chess_board.blit(pawn, board[i][1])
        elif board[i][2] == "rook":
            rook = pygame.image.load('resource/img/user/rook.png')
            chess_board.blit(rook, board[i][1])
        elif board[i][2] == "o_rook":
            rook = pygame.image.load('resource/img/opposite/rook.png')
            chess_board.blit(rook, board[i][1])
        elif board[i][2] == "knight":
            knight = pygame.image.load('resource/img/user/knight.png')
            chess_board.blit(knight, board[i][1])
        elif board[i][2] == "o_knight":
            knight = pygame.image.load('resource/img/opposite/knight.png')
            chess_board.blit(knight, board[i][1])
        elif board[i][2] == "bishop":
            bishop = pygame.image.load('resource/img/user/bishop.png')
            chess_board.blit(bishop, board[i][1])
        elif board[i][2] == "o_bishop":
            bishop = pygame.image.load('resource/img/opposite/bishop.png')
            chess_board.blit(bishop, board[i][1])
        elif board[i][2] == "king":
            king = pygame.image.load('resource/img/user/king.png')
            chess_board.blit(king, board[i][1])
        elif board[i][2] == "o_king":
            king = pygame.image.load('resource/img/opposite/king.png')
            chess_board.blit(king, board[i][1])
        elif board[i][2] == "queen":
            queen = pygame.image.load('resource/img/user/queen.png')
            chess_board.blit(queen, board[i][1])
        elif board[i][2] == "o_queen":
            queen = pygame.image.load('resource/img/opposite/queen.png')
            chess_board.blit(queen, board[i][1])

    font = pygame.font.SysFont(None, 30)
    text1 = font.render("user: "+str(score_0), True, (0, 0, 0))
    chess_board.blit(text1, (10, 605))
    text2 = font.render("opposite user: "+str(score_1), True, (0, 0, 0))
    chess_board.blit(text2, (425, 605))
    #update the whole screen
    pygame.display.flip()
            
pygame.quit()
quit()