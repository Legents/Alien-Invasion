﻿class Settings():
    """所有设置"""
    def __init__(self):
        #初始化  屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color =(230, 230, 230)
        
        #飞船设置
        self.ship_limit = 3
        
        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        #外星人设
        self.fleet_drop_speed = 5
        
        
        #加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #动态变化设置
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #direction向右为正 向左为负
        self.fleet_direction = 1
        #计分
        self.alien_points = 50
        
    def increase_speed(self):
        #提高速度
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
