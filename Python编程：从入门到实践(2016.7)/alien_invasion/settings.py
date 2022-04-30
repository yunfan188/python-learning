
# 编写settings模块，用来存储和添加设置

# 创建设置类
class Settings():
	def __init__(self):
		"""初始化游戏的设置"""
		# 设置屏幕参数
		self.screen_width = 800
		self.screen_height = 480
		self.bg_color = (230, 230, 230)
		# 飞船的设置
		self.ship_speed_factor = 1.5
		# 子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
