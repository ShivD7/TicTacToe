import pygame
pygame.init()

line_colour = (255, 255, 255)
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
game_drawn = True
run = True

game_played = [
    ["1"], ["4"], ["7"],
    ["2"], ["5"], ["8"],
    ["3"], ["6"], ["9"]

]
                            

count = 0

def checking(): 
 global run
 while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
               pygame.QUIT
               break

def new_game():
        global WIN
        global game_played
        global game_drawn
        game_drawn = False
        pygame.time.wait(1000)
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        game_played = [
    ["1"], ["4"], ["7"],
    ["2"], ["5"], ["8"],
    ["3"], ["6"], ["9"]
]
        board()
        main()
        checking()


def check_for_win():
        if count % 2 != 0:
                if game_played[0] == game_played[1] == game_played[2]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("X WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update()
                        new_game()

                elif game_played[3] == game_played[4] == game_played[5]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("X WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update()
                        new_game()
                
                elif game_played[6] == game_played[7] == game_played[8]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("X WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update() 
                        new_game()

                elif game_played[0] == game_played[3] == game_played[6]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("X WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update() 
                        new_game()

                elif game_played[1] == game_played[4] == game_played[7]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("X WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update()
                        new_game()

                elif game_played[2] == game_played[5] == game_played[8]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("X WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update()
                        new_game()

                elif game_played[0] == game_played[4] == game_played[8]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("X WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update() 
                        new_game()
 
                elif game_played[2] == game_played[4] == game_played[6]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("X WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update()
                        new_game()  

        elif count % 2 == 0:
                if game_played[0] == game_played[1] == game_played[2]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("O WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update() 
                        new_game()

                elif game_played[3] == game_played[4] == game_played[5]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("O WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update()   
                        new_game()
         
                elif game_played[6] == game_played[7] == game_played[8]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("O WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update() 
                        new_game()

                elif game_played[0] == game_played[3] == game_played[6]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("O WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update()
                        new_game()

                elif game_played[1] == game_played[4] == game_played[7]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("O WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update()
                        new_game()

                elif game_played[2] == game_played[5] == game_played[8]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("O WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update()
                        new_game()

                elif game_played[0] == game_played[4] == game_played[8]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("O WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update()   
                        new_game()

                elif game_played[2] == game_played[4] == game_played[6]:
                        font = pygame.font.SysFont(None, 100)
                        img = font.render("O WINS!", True, RED)
                        WIN.blit(img, (250 - 130, 250 - 40))
                        pygame.display.update() 
                        new_game()
               

def board():
    pygame.draw.line(WIN, line_colour, (WIDTH//3, 500), (WIDTH//3, -500), 5)
    pygame.draw.line(WIN, line_colour, ((WIDTH//3) * 2, 500), ((WIDTH//3) * 2, -500), 5)
    pygame.draw.line(WIN, line_colour, (0, (WIDTH//3)), (500, (WIDTH//3)), 5)
    pygame.draw.line(WIN, line_colour, (0, (WIDTH//3) * 2), (500, (WIDTH//3) * 2), 5)
    pygame.display.update()

board() 

def main():
   global player1 
   global count
   global run
   player1 = True
   count = 0
   while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
               pygame.QUIT
               break 
   
            elif event.type == pygame.MOUSEBUTTONDOWN and player1 == False:
                    coordinates = (0, 0)
                    coordinates = pygame.mouse.get_pos()
                    count += 1
                    
                    if coordinates[0] >= 0 and coordinates[0] <= WIDTH/3:
                        if coordinates[1] >= 0 and coordinates[1] <= HEIGHT/3:
                                if game_played[0] == "X":
                                       count -= 1
                                       player1 = False
                                elif game_played[0] == "O":
                                        count -= 1
                                        player1 = False
                                else:
                                        pygame.draw.circle(WIN, line_colour, (250/3, 250/3), 30, 5)
                                        pygame.display.update()
                                        game_played[0] = "O"
                                        check_for_win()
                                        player1 = True

                                       
                        elif coordinates[1] >= HEIGHT / 3 and coordinates[1] <= HEIGHT * (2/3):
                                if game_played[1] == "X":
                                      count -= 1
                                      player1 = False
                                elif game_played[1] == "O":
                                        count -= 1
                                        player1 = False
                                else:
                                        pygame.draw.circle(WIN, line_colour, (250/3, 250), 30, 5)
                                        pygame.display.update()
                                        game_played[1] = "O"
                                        check_for_win()
                                        player1 = True
  

                        elif coordinates[1] >= HEIGHT * (2 / 3) and coordinates[1] <= HEIGHT:
                                if game_played[2] == "X":
                                      count -= 1
                                      player1 = False
                                elif game_played[2] == "O":
                                        count -= 1
                                        player1 = False
                                else:
                                        pygame.draw.circle(WIN, line_colour, (250/3, 1250/3), 30, 5)
                                        pygame.display.update()
                                        game_played[2] = "O"
                                        check_for_win()
                                        player1 = True


                    elif coordinates[0] >= WIDTH/3 and coordinates[0] <= WIDTH * (2/3):
                        if coordinates[1] >= 0 and coordinates[1] <= HEIGHT/3:
                                if game_played[3] == "X":
                                       count -= 1
                                       player1 = False
                                elif game_played[3] == "O":
                                        count -= 1
                                        player1 = False
                                else:
                                        pygame.draw.circle(WIN, line_colour, (250, 250/3), 30, 5)
                                        pygame.display.update()
                                        game_played[3] = "O"
                                        check_for_win() 
                                        player1 = True      


                        elif coordinates[1] >= HEIGHT / 3 and coordinates[1] <= HEIGHT * (2/3):
                                if game_played[4] == "X":
                                       count -= 1
                                       player1 = False
                                elif game_played[4] == "O":
                                        count -= 1
                                        player1 = False
                                else:
                                        pygame.draw.circle(WIN, line_colour, (250, 250), 30, 5)
                                        pygame.display.update()
                                        game_played[4] = "O"
                                        check_for_win()
                                        player1 = True


                        elif coordinates[1] >= HEIGHT * (2/3) and coordinates[1] <= HEIGHT:
                                if game_played[5] == "X":
                                       count -= 1
                                       player1 = False
                                elif game_played[5] == "O":
                                        count -= 1
                                        player1 = False
                                else:
                                        pygame.draw.circle(WIN, line_colour, (250, 1250/3), 30, 5)
                                        pygame.display.update()
                                        game_played[5] = "O"
                                        check_for_win()
                                        player1 = True


                    else:
                        if coordinates[1] >= 0 and coordinates[1] <= HEIGHT/3:
                                if game_played[6] == "X":
                                       count -= 1
                                       player1 = False
                                elif game_played[6] == "O":
                                        count -= 1
                                        player1 = False
                                else:
                                        pygame.draw.circle(WIN, line_colour, (1250/3, 250/3), 30, 5)
                                        pygame.display.update()
                                        game_played[6] = "O"
                                        check_for_win()
                                        player1 = True

                        elif coordinates[1] >= HEIGHT / 3 and coordinates[1] <= HEIGHT * (2/3):
                                if game_played[7] == "X":
                                       count -= 1
                                       player1 = False
                                elif game_played[7] == "O":
                                         count -= 1
                                         player1 = False
                                else:
                                        pygame.draw.circle(WIN, line_colour, (1250/3, 250), 30, 5)
                                        pygame.display.update()
                                        game_played[7] = "O"
                                        check_for_win()
                                        player1 = True


                        elif coordinates[1] >= HEIGHT * (2/ 3) and coordinates[1] <= HEIGHT:
                                if game_played[8] == "X":
                                       count -= 1
                                       player1 = False
                                elif game_played[8] == "O":
                                         count -= 1
                                         player1 = False
                                else:
                                        pygame.draw.circle(WIN, line_colour, (1250/3, 1250/3), 30, 5)
                                        pygame.display.update()
                                        game_played[8] = "O"
                                        check_for_win()
                                        player1 = True


            elif event.type == pygame.MOUSEBUTTONDOWN and player1 == True:
                coordinates = pygame.mouse.get_pos()
                count += 1
                
                if coordinates[0] >= 0 and coordinates[0] <= WIDTH/3:
                        if coordinates[1] >= 0 and coordinates[1] <= HEIGHT/3:
                                if game_played[0] == "O":
                                       count -= 1
                                       player1 = True
                                elif game_played[0] == "X":
                                        count -= 1
                                        player1 = True
                                else:
                                        font = pygame.font.SysFont(None, 100)
                                        img = font.render("X", True, WHITE)
                                        WIN.blit(img, (250/3 - 25, 250/3 - 25))
                                        pygame.display.update()
                                        game_played[0] = "X"
                                        check_for_win()
                                        player1 = False

                        elif coordinates[1] >= HEIGHT / 3 and coordinates[1] <= HEIGHT * (2/3):
                                if game_played[1] == "O":
                                       count -= 1
                                       player1 = True
                                elif game_played[1] == "X":
                                        count -= 1
                                        player1 = True
                                else:
                                        font = pygame.font.SysFont(None, 100)
                                        img = font.render("X", True, WHITE)
                                        WIN.blit(img, (250/3 - 25, 250 - 25))
                                        pygame.display.update()
                                        game_played[1] = "X"
                                        check_for_win() 
                                        player1 = False


                        elif coordinates[1] >= HEIGHT * (2/ 3) and coordinates[1] <= HEIGHT:
                                if game_played[2] == "O":
                                       count -= 1 
                                       player1 = True
                                elif game_played[2] == "X":
                                        count -= 1
                                        player1 = True
                                else:
                                        font = pygame.font.SysFont(None, 100)
                                        img = font.render("X", True, WHITE)
                                        WIN.blit(img, (250/3 - 25, 1250/3 - 25))
                                        pygame.display.update()
                                        game_played[2] = "X"
                                        check_for_win()
                                        player1 = False


                elif coordinates[0] >= WIDTH/3 and coordinates[0] <= WIDTH * (2/3):
                        if coordinates[1] >= 0 and coordinates[1] <= HEIGHT/3:
                                if game_played[3] == "O":
                                       count -= 1
                                       player1 = True
                                elif game_played[3] == "X":
                                        count -= 1
                                        player1 = True
                                else:
                                        font = pygame.font.SysFont(None, 100)
                                        img = font.render("X", True, WHITE)
                                        WIN.blit(img, (250 - 25, 250/3 - 25))
                                        pygame.display.update()
                                        game_played[3] = "X"
                                        check_for_win()
                                        player1 = False


                        elif coordinates[1] >= HEIGHT / 3 and coordinates[1] <= HEIGHT * (2/3):
                                if game_played[4] == "O":
                                       count -= 1
                                       player1 = True
                                elif game_played[4] == "X":
                                        count -= 1
                                        player1 = True
                                else:
                                        font = pygame.font.SysFont(None, 100)
                                        img = font.render("X", True, WHITE)
                                        WIN.blit(img, (250 - 25, 250 - 25))
                                        pygame.display.update()
                                        game_played[4] = "X"
                                        check_for_win()  
                                        player1 = False


                        elif coordinates[1] >= HEIGHT * (2/ 3) and coordinates[1] <= HEIGHT:
                                if game_played[5] == "O":
                                       count -= 1
                                       player1 = True
                                elif game_played[5] == "X":
                                        count -= 1
                                        player1 = True
                                else:
                                        font = pygame.font.SysFont(None, 100)
                                        img = font.render("X", True, WHITE)
                                        WIN.blit(img, (250 - 25, 1250/3 - 25))
                                        pygame.display.update()
                                        game_played[5] = "X"
                                        check_for_win() 
                                        player1 = False

                else:
                        if coordinates[1] >= 0 and coordinates[1] <= HEIGHT/3:
                                if game_played[6] == "O":
                                       count -= 1
                                       player1 = True
                                elif game_played[6] == "X":
                                        count -= 1
                                        player1 = True
                                else:
                                        font = pygame.font.SysFont(None, 100)
                                        img = font.render("X", True, WHITE)
                                        WIN.blit(img, (1250/3 - 25, 250/3 - 25))
                                        pygame.display.update()
                                        game_played[6] = "X"
                                        check_for_win()
                                        player1 = False

                        elif coordinates[1] >= HEIGHT / 3 and coordinates[1] <= HEIGHT * (2/3):
                                if game_played[7] == "O":
                                       count -= 1
                                       player1 = True
                                elif game_played[7] == "X":
                                        count -= 1
                                        player1 = True
                                else:
                                        font = pygame.font.SysFont(None, 100)
                                        img = font.render("X", True, WHITE)
                                        WIN.blit(img, (1250/3 - 25, 250 - 25))
                                        pygame.display.update()
                                        game_played[7] = "X"
                                        check_for_win()
                                        player1 = False

                        elif coordinates[1] >= HEIGHT * (2/ 3) and coordinates[1] <= HEIGHT:
                                if game_played[8] == "O":
                                       count -= 1
                                       player1 = True
                                elif game_played[8] == "X":
                                        count -= 1
                                        player1 = True
                                else:
                                        font = pygame.font.SysFont(None, 100)
                                        img = font.render("X", True, WHITE)
                                        WIN.blit(img, (1250/3 - 25, 1250/3 - 25))
                                        pygame.display.update()
                                        game_played[8] = "X"
                                        check_for_win()
                                        player1 = False

               
                if count >= 9:
                                img = font.render("TIE GAME!", True, RED)
                                WIN.blit(img, (250 - 175, 250 - 40))
                                pygame.display.update() 
                                new_game()


                


main()




