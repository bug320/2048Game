# pygame.sprite.Sprite

## 给出的例子是一个 CarSprite ：`class CarSprite(pygame.sprite.Sprite)`

def __init__(self,image,position): 初始化中的属性有以下：

- self.src_image  # 贴图     ---  重点属性
- self.position   # 粘贴位置 ---  重点属性   
- self.speed      # 速度
- self.direction  # 方向
- self.k_left = self.k_up = self.k_down = self.k_up = 0  # 上下左右控制键

def update(self,deltat): 更新 Sprite

- 更新 速度
- 更新 位置（x,y） 
- 
