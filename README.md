# 中国铁路机车图片分类工具
**这个工具使用下关站数据训练，基于*YOLOv8-cls*实现，可识别图片中最突出的常见国铁机车或动车组型号.** 

**下关站数据集*top1*准确率达*99.4%*！** 

![image](https://github.com/user-attachments/assets/1bdf253a-0b4b-4e41-894d-ad9f441a3293)

## Getting started
**确保你安装了必要的*python*依赖库，若未安装，可通过以下命令安装**
```python
pip install ultralytics
pip install gradio
pip install pillow
```
**安装好后，运行*gui.py*，待终端出现``` Running on local URL:  http://127.0.0.1:7860 ```后打开网址即可使用.**

## 图片要求
**提交的图片最好满足以下要求，以便得到更准确的结果**
* 图片中主体应为**需识别的机车**，其牵引的车厢不应占比过大
* 图片中机车最好同时包含**正面和侧面**以便识别
* 图片中机车**不能被站台设施、接触网、桥梁等遮挡**，否则会得出无厘头的结果
* 图片要有**适当饱和度**，过于艳丽或暗淡都会影响识别
* 图片应保证一定**对比度和锐度**
* 图片中机车不能**过于“细长”**
### 举例说明
<img src='https://github.com/user-attachments/assets/6b92b135-8911-40b3-b5f0-3c3bc007068b' width='450' height='300'/>
<img src='https://github.com/user-attachments/assets/e9de8979-2b66-4c20-a4e0-961f32f9ab97' width='450' height='300'/>

上面两图中列车**被大桥钢梁和站台设施遮挡**，无法较好识别. 建议挑选角度更好的图片.

<img src='https://github.com/user-attachments/assets/71a522ae-200e-4bbb-9635-06dc651af4c2' width='450' height='300'/>
<img src='https://github.com/user-attachments/assets/16b3e9bf-66a2-4994-8dc5-83977c3f8da4' width='450' height='300'/>

上面两图中机车都**不位于主体部分**，易识别为其他物体. 建议提高对比度或进行裁切.

<img src='https://github.com/user-attachments/assets/d4b1ecac-b76a-43b9-ac67-eeaab97ca7b9' width='450' height='300'/>
<img src='https://github.com/user-attachments/assets/453d4e67-35d9-47ee-8c31-87b807d484b8' width='450' height='300'/>

上面两图中**颜色太过鲜艳或暗淡**，不易识别. 建议调整下方的 *Color滑动条* 加以调整.

## 使用方法
***gradio*** **界面清晰易懂，上传图片，调整图片，点击*Submit*按钮，等待结果即可.** 

**若识别不准确，不妨试试用*rotate*滑块将图片进行小角度旋转，可能有奇效（** 
### *Autocrop*说明
*Autocrop*会自动裁切出图中最大的火车元素以便识别，默认勾选. 但在**识别错误**、**无法识别**或**识别结果中仅有列车侧面**时建议***不要*** 勾选.

## 文件说明
* ***gui.py*** 主体程序，构建交互框架 
* ***best.pt*** 用于机车分类的模型 
* ***yolov8m-seg.pt*** 用于*Autocrop*的模型 

## 存在问题
* 由于下关站数据集规模限制，针对动车组的识别准确率有待提高
* 由于涂装类似，可能无法区分部分智动、城际列车及CRH3A
* 易混淆DF8与DF11
* 部分型号暂不支持识别

---
## 觉得项目还不错，就给个*Star*鼓励一下吧!  :blush:
  ***混淆矩阵***
<img src='https://github.com/user-attachments/assets/e815f686-939a-4d5a-be8f-025f9f7b9c7c' width='1000' height='750'/>

   ***最终网络结构***

<img src='https://github.com/user-attachments/assets/30f22fd5-4aaf-4c74-b19e-30fb36875729' width='300' height='7840'/>

