class Grid:
    import pygame
    def __init__(self):
        self.e=1500
        self.b=1050
        self.a= self.b
        self.image = self.pygame.image.load("C:\\Users\\Ravi\\Desktop\\nn tic\\blue_back.jpg")

        self.image_x = self.pygame.image.load("C:\\Users\\Ravi\\Desktop\\nn tic\\x logo.png")
        self.image_x = self.pygame.transform.scale(self.image_x,(self.b//3,self.b//3))
        
        self.image_o = self.pygame.image.load("C:\\Users\\Ravi\\Desktop\\nn tic\\o logo.png")
        self.image_o = self.pygame.transform.scale(self.image_o,(self.b//3,self.b//3))

        self.image = self.pygame.transform.scale(self.image,(self.e,self.b))
        self.image.fill((12,12,12), special_flags=self.pygame.BLEND_RGB_ADD) 
        self.black = (0,0,0)
        self.surface = self.pygame.display.set_mode((self.e,self.b))
        self.pygame.display.set_caption("tic")
        self.grid = [((self.e-self.b,3),(self.e,3)),
                     ((self.e-self.b,self.b-3),(self.e,self.b-3)),
                     ((self.e-self.b,self.b/3),(self.e,self.b/3)),
                     ((self.e-self.b,2*self.b/3),(self.e,2*self.b/3)),
                     ((self.e-self.b + self.a/3,0),(self.e-self.b +self.a/3,self.b)),
                     ((self.e-3,3),(self.e-3,self.b-3)),
                     ((self.e-self.b + 2*self.a/3,0),(self.e-self.b + 2*self.a/3,self.b)),
                     ((self.e-self.b,0),(self.e-self.b,self.b))]

    def print_text(self,text,pos,font_size,color):
        font = self.pygame.font.SysFont("freesansbold.ttf",font_size,True,False)
        surf = font.render(text,True,color)
        #print((self.e-self.b)/2, self.b/3)
        self.surface.blit(surf,pos)
    def main(self):  
        self.pygame.init()  
        dict = {1:(self.e-self.a,0),2:(self.e-2*self.a/3,0),3:(self.e-self.a/3,0),
                4:(self.e-self.a,self.b/3),5:(self.e-2*self.a/3,self.b/3),6:(self.e-self.a/3,self.b/3),
                6:(self.e-self.a,2*self.b/3),7:(self.e-2*self.a/3,2*self.b/3),9:(self.e-self.a/3,2*self.b/3)}
        t=True
        #name1 = input("name 1")
        #name2 = input("name 2")
        name1  = "Vandan"
        # set the center of the rectangular object.
        while t:
            self.surface.blit(self.image,(0,0))
            self.surface.blit(self.image_start,((self.e-self.b-250)/4+70, self.b/6-100))
            self.surface.blit(self.image_o,dict[9])
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    t=False

            #self.surface.fill((255,255,255)) 
            for i in range(len(self.grid)):
                #print(self.grid[i])
                self.pygame.draw.line(self.surface,(255,255,255),self.grid[i][0],self.grid[i][1])     
            self.print_text("Tic Tac Toe",((self.e-self.b-250)/4, self.b/6-150),80,(255,255,255))
            self.pygame.draw.line(self.surface,(255,255,255),((self.e-self.b-250)/4, self.b/6 -150 + 70),(((self.e-self.b-250)/4)+360, self.b/6-150 +70))

            self.pygame.draw.line(self.surface,(255,255,255),((self.e-self.b-250)/4, self.b/6+ 50),(((self.e-self.b-250)/4)+360, self.b/6+50))     
           
            self.print_text("Turn : {}".format(name1),((self.e-self.b-250)/4, self.b/6+ 100),60,(20,255,20))
            #self.print_text(,((self.e-self.b-250)/4, self.b/6+200),40)
            self.pygame.display.update()  

d = Grid()
d.main()