import pygame


class Button:
    def __init__(self, color, x, y, width, height, game, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.__game = game

    def draw(self, thickness, outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(self.__game.screen, outline, (self.x - thickness, self.y - thickness, self.width + 2*thickness, self.height + 2*thickness), 0)
            
        pygame.draw.rect(self.__game.screen, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.Font(None, 20)
            text = font.render(self.text, 1, (255, 255, 255))
            self.__game.screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


class Scene:

    def __init__(self, game):
        self.__game = game
        self.__texts = []
        self.__buttons = dict()

    def render(self):
        for text in self.__texts:
            self.__game.screen.blit(text[0], text[1])

        for button in self.__buttons.values():
            button.draw(2, (255, 255, 255))

    def getGame(self):
        return self.__game

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT :
                exit()

    def clearText(self):
        self.__texts = []

    def addText(self, string, x, y, color = [255, 255, 255], background = [0, 0, 0], size = 20):
        font = pygame.font.Font(None, size)
        if [font.render(string, True, color, background), (x,y)] not in self.__texts :
            self.__texts.append([font.render(string, True, color, background), (x,y)])

    def addButton(self, title, color, x, y, width, height, text):
        self.__buttons[title] = Button(color, x, y, width, height, self.__game, text)

    def getButton(self, title):
        return self.__buttons[title]

    def isButtonin(self, title):
        return title in self.__buttons.keys()

    def clearButtons(self):
        self.__buttons = dict()