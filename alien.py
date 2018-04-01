import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	#外星人类
	def __init__(self, ai_settings, screen):
		#位置
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#加载图片
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#设置默认位置
		self.rect.x = self.screen.width
		self.rect.y = self.screen.height
		
		#存储正确位置
		self.x = float(self.rect.x)
		
def blitme(self):
	#指定位置绘制
	self.screen.blit(self.image, self.rect)
	
