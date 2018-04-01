class Settings():
    """所有设置"""
    def __init__(self):
        #初始化  屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color =(230, 230, 230)
        
        #飞船设置
        self.ship_speed_factor = 1.5
        
        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        #direction向右为正 向左为负
        self.fleet_direction = 1
