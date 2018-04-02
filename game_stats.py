class GameStats():
	#用于跟踪统计信息
	def __init__(self, ai_settings):
		#初始化
		self.ai_settings = ai_settings
		self.reset_stats()
		#点击按钮开始游戏
		self.game_active = False
		
	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
