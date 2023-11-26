import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置显示窗口
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Card RPG Game')

# 加载图像
hero_image = pygame.image.load('image/hero.png')  # 替换为主角图像的路径
goblin_image = pygame.image.load('image/goblin.png')  # 替换为哥布林图像的路径
fist_icon = pygame.image.load('image/basic_attack.png')  # 替换为拳头图标的路径

# 缩放图像
hero_image = pygame.transform.scale(hero_image, (150, 150))  # 调整为合适的大小
goblin_image = pygame.transform.scale(goblin_image, (100, 100))  # 调整为合适的大小
fist_icon = pygame.transform.scale(fist_icon, (50, 50))  # 调整为合适的大小

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 检测鼠标点击
        if event.type == pygame.MOUSEBUTTONDOWN:
            if fist_icon.get_rect().collidepoint(event.pos):
                print("技能被激活")  # 这里添加攻击逻辑

    # 清除屏幕
    screen.fill((255, 255, 255))

    # 绘制角色和敌人
    screen.blit(hero_image, (50, screen_height // 2 - 75))
    for i in range(3):
        screen.blit(goblin_image, (screen_width - 150, 150 * i))

    # 绘制技能按钮
    screen.blit(fist_icon, (screen_width - 60, screen_height - 60))

    # 更新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
sys.exit()