#7.2.2 Python图像处理

from skimage import io, color
robot = io.imread("data/Robot.jpg")  
print(robot.shape)  #  图像像素
print(type(robot))  # 数据类型
io.imshow(robot)  
#io.show()

print( robot[91,221]  )   ##取指定坐标像素的颜色
print( robot[91,221, 0] )       #取指定坐标像素的R值
print( robot[77:80,221:231, 0]) #取一部分图像的R值

head = robot[40:165,180:305]    #给出图像局部 head的坐标范围
io.imshow(head)
io.show()
io.imsave('RobotHead.jpg', head)   #将图像数据保存为文件

