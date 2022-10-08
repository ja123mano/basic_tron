from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax, SSS
import random
temp_score = -1 * random.randint(0,1000)
class TronController (TwoPlayerGame):

    def __init__ (self, players, size=(10,10)):
        self.players = players
        self.current_player = 2
        
        if size[0] < 5 or size[1] < 5:
            self.board = [[0 for i in range(5)] for j in range(5)]
        else:
            self.board = [[0 for i in range(size[0])] for j in range(size[1])]
        
        self.board_size = (len(self.board), len(self.board[0]))
        self.board[1][self.board_size[1]//2] = 1
        self.board[self.board_size[0]-2][self.board_size[1]//2] = 2
        players[0].pos = (1, self.board_size[1]//2)
        players[1].pos = (self.board_size[0]-2, self.board_size[1]//2)

    def show (self):
        """ Imprimir el tablero """
        """ Tal vez imprimir espacio en blanco o guines para el área no visitada """
        """ y poner círculos para los jugadores y asteriscos para el recorrido """

        for row in range(len(self.board)):
            print(" ")

            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    print(". ", end="")
                elif self.board[row][col] == 1:
                    print("X ", end="")
                elif self.board[row][col] == 2:
                    print("O ", end="")
                elif self.board[row][col] == 3:
                    print("F ", end="")
                else:
                    print("* ", end="")
    
    def possible_moves (self):
        """ Movimientos posibles de acuerdo a la posición actual """
        """ Adelante, atrás o a los lados """

        pi, pj = self.player.pos
        blocked_path = self.opponent_index
        moves = []

        if pi > 0 and self.board[pi-1][pj] != blocked_path:
            moves.append("w")
        if pi < self.board_size[0]-1 and self.board[pi+1][pj] != blocked_path:
            moves.append("s")
        if pj > 0 and self.board[pi][pj-1] != blocked_path:
            moves.append("a")
        if pj < self.board_size[1]-1 and self.board[pi][pj+1] != blocked_path:
            moves.append("d")
        
        return moves

    def make_move (self, move):
        """ Ejecutar el movimiento seleccionado """

        pi, pj = self.player.pos
        self.board[pi][pj] = 4
        
        if move == "a":
            self.player.pos = (pi, pj-1)
        elif move == "d":
            self.player.pos = (pi, pj+1)
        elif move == "w":
            self.player.pos = (pi-1, pj)
        else:
            self.player.pos = (pi+1, pj)
        
        pi, pj = self.player.pos
        if self.board[pi][pj] == 4:
            self.board[pi][pj] = 3
        elif self.board[pi][pj] != 4:
            self.board[pi][pj] = self.current_player
    
    def loss_condition (self):
        """ Este método regresa si algún jugador ha chocado con el final del tablero """
        """ o recorrido suyo o del oponente """

        pi, pj = self.player.pos
        return True if self.possible_moves() == [] or self.board[pi][pj] == 3 else False

    def is_over (self):
        """ Decidir si el juego ha acabado """
        """ loss_condition """

        return self.loss_condition()
    
    def scoring (self):
        """ Funciones heurísticas """
        """ Podemos añadir más puntos de objetos adicionales """
        return  temp_score if self.loss_condition() else 0

def main():
    "You can adjust the difficulty of the AI by changing the number in the argument of the Negamax algorithm"
    #algo_neg1 = Negamax(5)
    "You can add an extra AI so 2 AI's can battle inside the game"
    #algo_neg2 = Negamax(15)
    human = Human_Player()
    ia1 = SSS(5)
    ia2 = Negamax(5)

    game = TronController([AI_Player(ia1), AI_Player(ia2)])
    #game = TronController([AI_Player(ia1), human])
    game.play()

    if game.loss_condition():
        print(f"\nEl jugador {game.opponent_index} gana")
    else:
        print("\nEmpate")
    print(f"Utilidad perdida: {temp_score}")

if __name__ == "__main__":
    main()

###########################################
#               Analisis
# Pese al cambio de utilidad en cada ejecución del 
# código la IA en ganar es la que comienza en cada  
# ocasión, considero que este en su factor que afecta
# al rendimiento del juego