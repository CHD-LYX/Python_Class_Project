import turtle

def draw_star(size, color, x, y):
    """
    使用turtle模块绘制一个五角星
    :param size: 五角星的大小（边长）
    :param color: 五角星的颜色
    :param x: 五角星起始点的x坐标
    :param y: 五角星起始点的y坐标
    """
    # 创建一个turtle对象
    star = turtle.Turtle()
    
    # 设置画笔颜色
    star.color(color)
    
    # 提起画笔移动到起始位置
    star.penup()
    star.goto(x, y)
    
    # 放下画笔开始绘制
    star.pendown()
    
    # 五角星的五个顶点角度分别为 72, 144, 216, 288, 360 度
    for _ in range(5):
        star.forward(size)
        star.right(144)
    
    # 完成绘制后隐藏turtle光标
    star.hideturtle()

def main():
    # 设置屏幕
    screen = turtle.Screen()
    screen.title("五角星图案")
    screen.bgcolor("white")
    
    # 设置五角星的大小、颜色和位置
    size = 600 # 边长
    color = "red"  # 颜色
    x = -250 # 起始点x坐标（屏幕中心）
    y = 100 # 起始点y坐标（屏幕中心下方）
    
    # 调用绘制函数
    draw_star(size, color, x, y)
    
    # 保持窗口打开直到用户关闭
    screen.mainloop()

if __name__ == "__main__":
    main()