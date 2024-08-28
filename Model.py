import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
from tensorflow.keras.models import load_model # type: ignore
import cv2
import os

# 載入訓練好的模型


class MNIST_Model:

    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        model_filename = 'mnist_model_Epoch_60.h5'  # 修改為實際模型文件名
        model_folder = 'models'
        model_path = os.path.join(model_folder, model_filename)

        return load_model(model_path)

    def predict_images(self, image_folder):
        # 獲取資料夾中的所有檔案
        filenames = [f for f in os.listdir(image_folder) if f.endswith('.png')]
        images = []
        valid_filenames = []
        
        for filename in filenames:
            img_path = os.path.join(image_folder, filename)
            img = self._load_and_preprocess_imagePath(img_path)
            if img is not None:  # 只添加有效的圖片
                images.append(img)
                valid_filenames.append(filename)
        
        if len(images) == 0:
            print("沒有有效的圖片進行預測。")
            return valid_filenames, [], []
        
        images = np.array(images)
        predictions = self.model.predict(images)
        predicted_labels = np.argmax(predictions, axis=1)
        
        return valid_filenames, images, predicted_labels

    def predict_result(self, filename_path):
        # 圖片前處理
        img = self._load_and_preprocess_imagePath(filename_path) 

        img = np.expand_dims(img, axis=0)  # 增加一維以匹配模型輸入
        prediction = self.model.predict(img)
        predicted_label = np.argmax(prediction, axis=1)

        return predicted_label

    def predict(self, image):
        img = self._load_and_preprocess_image(image) 

        img = np.expand_dims(img, axis=0)  # 增加一維以匹配模型輸入
        prediction = self.model.predict(img)
        predicted_label = np.argmax(prediction, axis=1)

        predicted_label = predicted_label[0]
        return predicted_label

    # 載入圖片並進行預處理
    def _load_and_preprocess_imagePath(self, img_path):
        if not os.path.exists(img_path):
            print(f"圖片不存在: {img_path}")
            return None
        
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # 讀取為灰度圖
        if img is None:
            print(f"無法讀取圖片: {img_path}")
            return None
    
        img = cv2.resize(img, (28, 28))  # 調整大小為 28x28
        img = img.astype('float32') / 255  # 正規化
        img = np.expand_dims(img, axis=-1)  # 增加一維以匹配模型輸入
        return img

    def _load_and_preprocess_image(self, img):
        if isinstance(img, Image.Image):
            img = np.array(img)
    
        # 檢查 img 是否為 numpy 陣列
        if not isinstance(img, np.ndarray):
            print(f"無效的圖片數據類型: {type(img)}")
            return None
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 灰階
    
        img = cv2.resize(img, (28, 28))  # 調整大小為 28x28
        img = img.astype('float32') / 255  # 正規化
        img = np.expand_dims(img, axis=-1)  # 增加一維以匹配模型輸入
        return img

    def SwitchModel(self, model_path):
        self.model = load_model(model_path)


model = MNIST_Model()
print(model.predict_result("image\\drawing_1862148976.png"))