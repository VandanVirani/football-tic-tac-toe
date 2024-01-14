from position_cal import position_cal
class Tic_tac_toe:
    import random
    import pygame
    import cv2
    def __init__(self):
            self.e=1500
            self.b=1050
            self.a= self.b
            self.winner = self.pygame.image.load("C:\\Users\\Ravi\\Desktop\\nn tic\\winner.jpg")
            self.winner = self.pygame.transform.scale(self.winner,(self.e,self.b))

            self.image_x = self.pygame.image.load("C:\\Users\\Ravi\\Desktop\\nn tic\\x2 logo.png")
            self.image_x = self.pygame.transform.scale(self.image_x,(self.b//3-50,self.b//3-50))
            
            self.image_o = self.pygame.image.load("C:\\Users\\Ravi\\Desktop\\nn tic\\o2 logo.png")
            self.image_o = self.pygame.transform.scale(self.image_o,(self.b//3-50,self.b//3-50))

            self.image_xF = self.pygame.image.load("C:\\Users\\Ravi\\Desktop\\nn tic\\xf logo.png")
            self.image_xF = self.pygame.transform.scale(self.image_xF,(self.b//3-50,self.b//3-50))
            
            self.image_oF = self.pygame.image.load("C:\\Users\\Ravi\\Desktop\\nn tic\\of logo.png")
            self.image_oF = self.pygame.transform.scale(self.image_oF,(self.b//3-50,self.b//3-50))


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
   

            self.board_loc = ['-','-','-','-','-','-','-','-','-']
            self.board =   [[self.board_loc[0],self.board_loc[1],self.board_loc[2]],
                                    [self.board_loc[3],self.board_loc[4],self.board_loc[5]],
                                    [self.board_loc[6],self.board_loc[7],self.board_loc[8]]] 
            self.turn = 0

    def print_text(self,text,pos,font_size,color):
        font = self.pygame.font.SysFont("freesansbold.ttf",font_size,True,False)
        surf = font.render(text,True,color)
        #print((self.e-self.b)/2, self.b/3)
        self.surface.blit(surf,pos)

    def updating_board(self,value,pos):
          self.board_loc[pos] = value


    def display_updating(self):
            
            self.dict1 = {0:(self.e-self.a,0),1:(self.e-2*self.a/3,0),2:(self.e-self.a/3,0),
                3:(self.e-self.a,self.b/3),4:(self.e-2*self.a/3,self.b/3),5:(self.e-self.a/3,self.b/3),
                6:(self.e-self.a,2*self.b/3),7:(self.e-2*self.a/3,2*self.b/3),8:(self.e-self.a/3,2*self.b/3)}
            tt = [[0,1,2],
                    [3,4,5],
                    [6,7,8],
                    [0,3,6],
                    [1,4,7],
                    [2,5,8],
                    [0,4,8],
                    [2,4,6]]
            self.surface.fill((148, 180, 115))

            for i in range(len(self.grid)):
                        self.pygame.draw.line(self.surface,(59, 63, 100),self.grid[i][0],self.grid[i][1],8)     
            
            self.pygame.draw.line(self.surface,(59, 63, 100),((self.e-self.b-250)/4, self.b/6 -150 + 70),(((self.e-self.b-250)/4)+360, self.b/6-150 +70),5)
            #self.pygame.draw.line(self.surface,(59, 63, 100),((self.e-self.b-250)/4, self.b/6+ 50),(((self.e-self.b-250)/4)+360, self.b/6+50))     
            self.print_text("TIC TAC TOE",((self.e-self.b-250)/4+50, self.b/6-150),60,(0, 7, 232))    
            self.print_text("TURN :- ",((self.e-self.b-250)/4+50, self.b/6+ 100),60,(0,0,0))
            self.print_text("{}".format(self.dict[1-self.turn]),((self.e-self.b-250)/4+250, self.b/6+ 100),60,(17, 100, 59))
            
            # print(self.board_loc,self.turn)
            for o in range(9):
                if self.board_loc[o]=="X":
                        self.surface.blit(self.image_x,(self.dict1[o][0]+25,self.dict1[o][1]+25))
                elif self.board_loc[o]=="O":
                        self.surface.blit(self.image_o,(self.dict1[o][0]+25,self.dict1[o][1]+25))

            fff = []
            for ii in range(len(self.board_loc)):
                if self.board_loc[ii] == self.dict[self.turn]:
                   fff.append(ii)
            
            for yy in  tt:
                if yy[0]in fff and yy[1]in fff and yy[2]in fff:
                    if self.turn==0:
                        self.surface.blit(self.winner,(0,0))
                        self.surface.blit(self.image_xF,(self.e//2-140,self.b//2-220))
                        self.pygame.display.update()
                        self.cv2.waitKey(5000)
                        self.main()

                    elif self.turn==1:
                        self.surface.blit(self.winner,(0,0))
                        self.surface.blit(self.image_oF,(self.e//2-140,self.b//2-220))
                        self.pygame.display.update()
                        self.cv2.waitKey(5000)
                        self.main()

                    else:
                        pass    
            if '-' not in self.board_loc:
                        self.main()
            self.pygame.display.update()
                    
            
            self.pygame.display.flip()
            self.pygame.display.update()
    def main(self):

            self.pygame.init()
            self.__init__()
            self.dict = {0:'X',1:'O'}
            self.turn = self.random.randint(0,1)
            print(self.turn)
            T=1
            
            model  = position_cal()
            print(model)
            self.display_updating()
            self.turn=1-self.turn
            while T:
                inp = model.calculate()
                self.cv2.waitKey(1000)
                
                if inp==None:
                    inp=10
                if 0<=inp<=8:

                    if self.board_loc[inp]=='-':
                        self.board_loc[inp]=self.dict[self.turn]
                        
                        g=[]
                        for k in range(len(self.board_loc)):
                            if self.board_loc[k]==self.dict[self.turn]:
                                 g.append(k)
                        if (0 in g and 1 in g and 2 in g) or (3 in g and 4 in g and 5 in g) or (6 in g and 7 in g and 8 in g) or (0 in g and 3 in g and 6 in g) or (1 in g and 4 in g and 7 in g) or (2 in g and 5 in g and 8 in g) or (0 in g and 4 in g and 8 in g) or (2 in g and 4 in g and 6 in g):
                                    print("print {} win".format(self.dict[self.turn]))
                                    T=0
                                    break
                        for event in self.pygame.event.get():
                            if event.type == self.pygame.QUIT:
                                self.pygame.quit()

                        #displaying
                        self.display_updating()
                        self.turn = 1 - self.turn
                    else:
                        pass
                
                elif inp==10:
                    pass

            while True:
                self.display_updating()
                        

                    
                    


      
game = Tic_tac_toe()
game.main()


