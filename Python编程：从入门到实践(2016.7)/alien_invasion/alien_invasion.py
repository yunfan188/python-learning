
# 创建Pygame窗口以及响应用户输入
# import sys
import pygame
from pygame.sprite import Group
# 导入settings模块
from settings import Settings
# 导入ship模块
from ship import Ship
# 导入game_functions模块并指定别名为gf
import game_functions as gf


def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	# 创建Settings类对象实例
	ai_settings = Settings()
	# 创建显示窗口大小
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	# 设置窗口标题
	pygame.display.set_caption("Alien Invasion")
	# 创建一艘飞船
	ship = Ship(ai_settings, screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()

	# 开始游戏的主循环
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

