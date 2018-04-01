import pygame
from settings import *
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
                (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建ship
    ship = Ship(ai_settings, screen)
    #创建一组bullet
    bullets = Group()
    #一组外星人
    aliens = Group()
    #外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #开始游戏的循环
    while True:
                gf.check_events(ai_settings, screen, ship, bullets)
                ship.update()
                gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
                gf.update_aliens(ai_settings, ship, aliens)
                gf.update_screen(ai_settings, screen, ship, aliens, bullets)              
run_game()
