import pygame
class Ship():

    def __init__(self,screen):
        #ship初始化设置位置
        self.screen = screen
        
        #加载ship获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将飞船放在屏幕底部的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #绘制
        self.screen.blit(self.image,self.rect)
