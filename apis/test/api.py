import pandas as pd

import matplotlib.pyplot as plt
import os
# 假設 select_data 函數已經被正確導入

def bar(df_filtered,colunm:str):
    plt.figure(figsize=(8, 6))
    df_filtered[colunm].value_counts().plot(kind='bar')
    plt.xlabel(colunm)
    plt.ylabel('count')
    # plt.title('Target bar chart')

    # 確定圖片保存路徑，這裡將圖片保存在臨時目錄下
    image_dir = '.'
    image_path = os.path.join(image_dir, f'API_1_bar_chart.png')
    plt.savefig(image_path)
    plt.close()  # 關閉 plt 對象釋放資源s
    return image_path

def line(df_filtered,colunm:str):
    plt.figure(figsize=(8, 6))
    df_filtered[colunm].plot(kind='line')
    plt.xlabel('UDI')
    plt.ylabel(colunm)
    # plt.title('Target bar chart')

    # 確定圖片保存路徑，這裡將圖片保存在臨時目錄下
    image_dir = '.'
    image_path = os.path.join(image_dir, f'API_1_line_chart.png')
    plt.savefig(image_path)
    plt.close()  # 關閉 plt 對象釋放資源s
    return image_path
def pie(df_filtered,colunm:str):

    labels, values = df_filtered[colunm].value_counts().keys(), df_filtered[colunm].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    # plt.title('Target bar chart')

    # 確定圖片保存路徑，這裡將圖片保存在臨時目錄下
    image_dir = '.'
    image_path = os.path.join(image_dir, f'API_1_pie_chart.png')
    plt.savefig(image_path)
    plt.close()  # 關閉 plt 對象釋放資源s
    return image_path
def select_data(csv_path, count):
    df = pd.read_csv(csv_path)
    # 篩選出指定範圍的 UDI
    # df['UDI'].head(20)
    df_filtered = df.head(count)
    return df_filtered  # 返回篩選後的數據


if __name__ == "__main__":
    path = "/home/mingyen/Desktop/SideProject/Toolformer/test_maintenance.csv"
    df = select_data(path,20)
    pie(df_filtered=df,colunm='Air temperature [K]')
    # "Rotational speed [rpm]"
    # print(df['Air temperature [K]'])