import sys 
import pygame
from settings import *
from ship import Ship

def run_game():
	#创建屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
                (ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#创建ship
	ship = Ship(screen)
	#开始游戏的循环
	while True:
                #监听器
		 for event in pygame.event.get():
			 if event.type == pygame.QUIT:
				 sys.exit()
                #重绘屏幕
		 screen.fill(ai_settings.bg_color)
		 ship.blitme()
		#显示最近绘制的屏幕
		 pygame.display.flip()
		
run_game()		 
		
