import random
import sys

import pygame


class Block(pygame.sprite.Sprite):

    def __init__(self, random):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15 - 3 * (score // 5)  # 方块坠落速度
        self.x = 4  # 方块抽象x坐标
        self.y = 1  # 方块抽象y坐标
        self.count = 0  # 方块坠落计数器
        self.block_type = -1  # 表示方块形态
        self.random = random  # 决定方块种类
        self.rect = self.block_box(self.x * cell, self.y * cell)
        for rect in self.rect:  # 检测游戏结束
            if scene[int(rect.y / cell)][int(rect.x / cell)] == 1:
                # print(int(rect.y / cell)," ",int(rect.x / cell))
                pygame.quit()
                sys.exit()

    def block_box(self, x, y):  # 储存所有方块的所有形态，提供变形
        T = ((pygame.Rect(x, y, cell, cell),
              pygame.Rect(x, y - cell, cell, cell),
              pygame.Rect(x - cell, y, cell, cell),
              pygame.Rect(x + cell, y, cell, cell)),  # (0形态)                              # T字形方块储存 0 <= random < 1

             (pygame.Rect(x, y, cell, cell),
              pygame.Rect(x, y - cell, cell, cell),
              pygame.Rect(x, y + cell, cell, cell),
              pygame.Rect(x + cell, y, cell, cell)),  # (1形态)

             (pygame.Rect(x, y, cell, cell),
              pygame.Rect(x, y - cell, cell, cell),
              pygame.Rect(x, y + cell, cell, cell),
              pygame.Rect(x - cell, y, cell, cell)),  # (2形态)

             (pygame.Rect(x, y, cell, cell),
              pygame.Rect(x, y + cell, cell, cell),
              pygame.Rect(x - cell, y, cell, cell),
              pygame.Rect(x + cell, y, cell, cell)))  # (3形态)

        I = ((pygame.Rect(x, y, cell, cell),
              pygame.Rect(x, y - cell, cell, cell),
              pygame.Rect(x, y + cell, cell, cell),
              pygame.Rect(x, y + 2 * cell, cell, cell)),  # (0形态)                    # I字形方块储存 1 <= random < 2

             (pygame.Rect(x, y, cell, cell),
              pygame.Rect(x - cell, y, cell, cell),
              pygame.Rect(x + cell, y, cell, cell),
              pygame.Rect(x + 2 * cell, y, cell, cell)))  # (1形态)

        Z_right = ((pygame.Rect(x, y, cell, cell),
                    pygame.Rect(x - cell, y, cell, cell),
                    pygame.Rect(x, y - cell, cell, cell),
                    pygame.Rect(x - cell, y + cell, cell, cell)),  # (0形态)          # Z字形方块储存 2 <= random < 3

                   (pygame.Rect(x, y, cell, cell),
                    pygame.Rect(x - cell, y, cell, cell),
                    pygame.Rect(x + cell, y + cell, cell, cell),
                    pygame.Rect(x, y + cell, cell, cell)))  # (1形态)

        L_left = ((pygame.Rect(x, y, cell, cell),
                   pygame.Rect(x, y + cell, cell, cell),
                   pygame.Rect(x - cell, y, cell, cell),
                   pygame.Rect(x, y + 2 * cell, cell, cell)),  # (0形态)     # L字形方块储存 3 <= random < 4

                  (pygame.Rect(x, y, cell, cell),
                   pygame.Rect(x, y - cell, cell, cell),
                   pygame.Rect(x - 2 * cell, y, cell, cell),
                   pygame.Rect(x - cell, y, cell, cell)),  # (1形态)

                  (pygame.Rect(x, y, cell, cell),
                   pygame.Rect(x, y - cell, cell, cell),
                   pygame.Rect(x, y - 2 * cell, cell, cell),
                   pygame.Rect(x + cell, y, cell, cell)),  # (2形态)

                  (pygame.Rect(x, y, cell, cell),
                   pygame.Rect(x, y + cell, cell, cell),
                   pygame.Rect(x + cell, y, cell, cell),
                   pygame.Rect(x + 2 * cell, y, cell, cell)))  # (3形态)

        L_right = ((pygame.Rect(x, y, cell, cell),
                    pygame.Rect(x, y + cell, cell, cell),
                    pygame.Rect(x + cell, y, cell, cell),
                    pygame.Rect(x, y + 2 * cell, cell, cell)),  # (0形态)         # L字形方块储存 4 <= random < 5

                   (pygame.Rect(x, y, cell, cell),
                    pygame.Rect(x, y - cell, cell, cell),
                    pygame.Rect(x + 2 * cell, y, cell, cell),
                    pygame.Rect(x + cell, y, cell, cell)),  # (1形态)

                   (pygame.Rect(x, y, cell, cell),
                    pygame.Rect(x, y - cell, cell, cell),
                    pygame.Rect(x, y - 2 * cell, cell, cell),
                    pygame.Rect(x - cell, y, cell, cell)),  # (2形态)

                   (pygame.Rect(x, y, cell, cell),
                    pygame.Rect(x, y + cell, cell, cell),
                    pygame.Rect(x - cell, y, cell, cell),
                    pygame.Rect(x - 2 * cell, y, cell, cell)))  # (3形态)

        Z_left = ((pygame.Rect(x, y, cell, cell),
                   pygame.Rect(x + cell, y, cell, cell),
                   pygame.Rect(x, y - cell, cell, cell),
                   pygame.Rect(x + cell, y + cell, cell, cell)),  # (0形态)         # Z字形方块储存 5 <= random < 6

                  (pygame.Rect(x, y, cell, cell),
                   pygame.Rect(x + cell, y, cell, cell),
                   pygame.Rect(x - cell, y + cell, cell, cell),
                   pygame.Rect(x, y + cell, cell, cell)))  # (1形态)

        D = (pygame.Rect(x, y, cell, cell),  # 田字形方块储存 6 <= random < 7

             pygame.Rect(x - cell, y, cell, cell),
             pygame.Rect(x - cell, y + cell, cell, cell),
             pygame.Rect(x, y + cell, cell, cell))

        if 0 <= self.random < 1:
            self.block_type += 1
            if self.block_type > 3:
                self.block_type = 0
            return T[self.block_type]
        elif 1 <= self.random < 2:
            self.block_type += 1
            if self.block_type > 1:
                self.block_type = 0
            return I[self.block_type]
        elif 2 <= self.random < 3:
            self.block_type += 1
            if self.block_type > 1:
                self.block_type = 0
            return Z_right[self.block_type]
        elif 3 <= self.random < 4:
            self.block_type += 1
            if self.block_type > 3:
                self.block_type = 0
            return L_left[self.block_type]
        elif 4 <= self.random < 5:
            self.block_type += 1
            if self.block_type > 3:
                self.block_type = 0
            return L_right[self.block_type]
        elif 5 <= self.random < 6:
            self.block_type += 1
            if self.block_type > 1:
                self.block_type = 0
            return Z_left[self.block_type]
        else:
            return D

    def draw(self):  # 画出方块
        for rect in self.rect:
            pygame.draw.rect(screen, white_color, rect)

    '''
    计数器的作用是为了让掉落动作在几个循环后才执行一次，由此提高
    左右移动的灵敏度
    '''

    def update(self):  # 方块持续掉落
        self.count += 1
        if self.count > self.speed:
            for rect in self.rect:
                if rect.y / cell == scene_y - 1 \
                        or scene[int(rect.y / cell + 1)][int(rect.x / cell)] == 1:
                    # for rt in self.rect:
                    for i in range(4):
                        rt = self.rect[i]
                        scene[int(rt.y / cell)][int(rt.x / cell)] = 1  # scene的索引是反的，即scene[y][x]
                    return True
            for rect in self.rect:
                rect.y += cell
            self.count = 0
        return False

    def change(self):  # 控制方块变形
        x = self.rect[0].x
        y = self.rect[0].y
        test_rect = self.block_box(x, y)
        for rect in test_rect:  # 检测方块变形后是否超出屏幕或与其他方块重叠
            if rect.y + cell > height or rect.x < 0 or rect.x + cell > width \
                    or scene[int(rect.y / cell)][int(rect.x / cell)] == 1:
                return False
        self.rect = test_rect

    def go_Left(self):  # 方块左移                           #实现“当全部方块都满足条件后才能移动，但凡有一个不满足都跳过下一句的移动代码（需要优化
        for rect in self.rect:  # 判断方块到左边界
            if rect.x - cell < 0 \
                    or scene[int(rect.y / cell)][int(rect.x / cell - 1)] == 1:
                return False
        for rect in self.rect:  # 移动方块
            rect.x -= cell

    def go_Right(self):  # 方块右移
        for rect in self.rect:  # 判断方块到右边界
            if rect.x + 2 * cell > width \
                    or scene[int(rect.y / cell)][int(rect.x / cell + 1)] == 1:
                return 1
        for rect in self.rect:  # 移动方块
            rect.x += cell

    def accelerate(self):
        self.speed = 1


def generate_Block():  # 方块生成器
    return Block(random.random() * 7)


def scene_flash(y):  # 将上层方块下移                        # 不是这里的问题
    for y in range(y, 0, -1):
        scene[y] = scene[y - 1].copy()  # 不能用scene[y] = scene[y - 1]赋值，否则scene[y]会引用scene[y - 1]


def check_score(score):  # 检查方块是否堆满一整条，记录得分
    for y in range(scene_y):
        s = 0  # 用于计数每一行存在的方块是否满足一整行
        for x in range(scene_x):
            if scene[y][x] == 1:
                s += 1
        if s == scene_x:
            score += 1
            scene_flash(y)
    return score


def draw_scene():  # 根据抽象坐标对场景进行重绘
    for x in range(scene_x):
        for y in range(scene_y):
            if scene[y][x] == 1:
                pygame.draw.rect(screen, white_color, pygame.Rect(x * cell, y * cell, cell, cell))
    pygame.display.update()


pygame.init()  # 初始化游戏窗口
scene_x = 10  # 抽象坐标x
scene_y = 20  # 抽象坐标y
size = width, height = 200, 400  # 窗口大小
cell = 20  # 格子大小
white_color = (255, 255, 255)  # RGB白色
black_color = (0, 0, 0)  # RGB黑色
score = 0  # 游戏分数
scene = [[0 for i in range(scene_x)] for j in range(scene_y)]
screen = pygame.display.set_mode(size)  # 设置窗口大小
pygame.display.set_caption("俄罗斯方块")

block_list = list()
clock = pygame.time.Clock()
block = generate_Block()

while True:  # 保持窗口显示

    clock.tick(30)
    screen.fill(black_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 检测是否关闭窗口
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # 检测键盘左方向键
                block.go_Left()
            if event.key == pygame.K_RIGHT:  # 检测键盘右方向键
                block.go_Right()
            if event.key == pygame.K_UP:
                block.change()
            if event.key == pygame.K_DOWN:
                block.accelerate()

    block.draw()
    draw_scene()

    if block.update():  # 判断方块触底或搭在其他方块上，把停止的方块的坐标记录在抽象坐标轴上
        score = check_score(score)  # 检测游戏得分，消除一整条的方块
        print("分数：", score)
        block = generate_Block()  # 生成新的方块
