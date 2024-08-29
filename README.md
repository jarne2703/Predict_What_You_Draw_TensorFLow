# Predict_What_You_Draw (Number)

這是一個基於 Tkinter 和 PIL 庫的手繪圖像識別應用程式。用戶可以在應用程式中手繪數字，並使用訓練好的 MNIST 模型進行預測。

# Install 

```
git clone https://github.com/Luffy1225/Mnist_Machine_Learning_Practice.git
pip install -r requirements.txt
mkdir -p font
wget -O font/taipei_sans_tc_beta.ttf "https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download"

```


# Run

```
python run.py
```


## 功能
1. 手繪畫布：

    用戶可以在應用程式提供的畫布上自由繪製數字。
1. 模型選擇：

    提供多個訓練好的模型，讓用戶選擇並切換進行預測。
1. 預測結果顯示：

    應用程式會在畫布下方顯示模型預測的數字。
1. 清除畫布：

    用戶可以清除畫布上的所有內容，重新繪製數字。
1. 保存圖像：

    可以將繪製的圖像保存到本地。