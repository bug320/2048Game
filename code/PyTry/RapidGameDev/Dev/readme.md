# Rapid Game Deveopment In Python（在Python中快速开发游戏）
作者: Richard Jones
## 如何制作游戏？
游戏 主要由 用户输入（user input）, 游戏输出（game output） 和 世界模拟（sort of word simulatio） 组成。最有趣的游戏是有
不同之处或者有新的世界模拟。Python 是游戏模拟中的很好的语言。幸运的是，一些其他人做了很多关于用户输入和游戏输出的工作贡
献到 Python 库。

## Python has

Python
    可能是最后的游戏世界模拟语言。Python很容易被阅读和编写，很容易学习，处理很多程序管理，并且运行的很快。
PyGame
    用户输入处理（鼠标、键盘、手柄）和通过屏幕进行游戏输出（形状图、图片、字体渲染）和声音（效果和声音）。2d 图片。
PyOpenGL
    让 Python 可以利用 OpenGL 进行 3d 渲染。
    （Soya3d,PGU）
上面的附加库为您的世界模拟、游戏地图绘制代码、模型加载、事件管理等提供了坚实的基础。

## 管理屏幕--基础

基本的屏幕初始化看起来像：

    from pygame.locals import *
    screen = pygame.display.set_mode((1024,768))
    screen = pygame.display.set_mode((1024,768),FULLSCREEN)


你可以在程序中调用 `set_mode` 从窗口切换的到全屏。其他显示模式标志（只需要用 `|` 放到一起）

DOUBLEBUF  : 必须用于平滑的动画
OPENGL     :  让你用 PyOpenGL 画 3D 场景，但不会让你调用 pygame 绘图函数

这是一个可选的标志位。一般情况下最好不要有。

如果有使用 DOUBLEBUF 然后，在渲染窗口前，你需要使用 `flip` 函数区 flip 窗口。例如：
 `pygame.display.filp()`

##　画一个赛车

我们打算画一个车在屏幕。我们利用画图原语来实现这个：BLIT(块图像传输).它复制一个图片从一个图片（例如你的资源图片）到另一个地方
（例如 屏幕中 X=50，Y=100）:

    car = pygame.image.load('car.png')
    screen = blit(car, (50, 100))
    pygame.display.flip()

在这个点，这个“车”会显示到以屏幕左上角为原点的（50，100）处。x 表示离窗口左边的距离，y 表示离窗口上边的距离。我们也可以旋转图片:

    import math
    rotated = pygame.transform.rotate(car, 45 * math.pi / 180)
    screen.blit(car, (150, 100))
    pygame.display.filp()

“车”动画:

    制作动画屏幕上的任何涉及及绘制的场景，清理并重新绘制它略有不同：
    
    for i in range(100):
        screen.fill((0, 0, 0))  
        screen.blit(car, (i,0))

## 时间处理

   在 PyGame 有很多方式去获取用户输入，最重要的是：

      import pygame
      pygame.event.wait()
      pygame.event.poll()
      pygame.event.get()
      
    wait 相当于 input()
    get  相当于 kbhit()
    poll 看看是否有事件等待处理。如果没有事件，则返回 NOEVENT 你可以处理一些其他事情。
    我们也应该在这里提到时间，因为这个对用户体验很重要。

        clock = pygame.time.Clock()
        FRAMES_PER_SECOND = 30
        deltat = clock.tick(FRAMES_PER_SECOND)
        
    tick 支持 clock 对象刷新 1/30 秒每次。

## 汇聚一些元素
    下面的代码将根据用户输入控制小汽车的移动，大致由4个部分组成：
    （初始化、用户输入、动画和渲染）
    `见 code_1.py`

## 更多结构

在上面的 代码增加一些特设。 大多数游戏都希望组织一些东西，以便更好地控制模拟和渲染。

