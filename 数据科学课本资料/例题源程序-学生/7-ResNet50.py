#例7-3 使用keras提供的 ResNet50 图像分类模型，对给定图像进行分类
#模型可自动下载，也可将模型"resnet50_weights_tf_dim_ordering_tf_kernels.h5"放入".keras/models/"文件夹内

from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.applications.resnet50 import decode_predictions
from keras.preprocessing import image
import numpy as np

#导入预训练模型ResNet50
model = ResNet50(weights='imagenet')

# 对输入图片进行处理
img_path = 'elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# 模型预测
preds = model.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])
# Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357),(u'n02504458', u'African_elephant', 0.061040461)]
