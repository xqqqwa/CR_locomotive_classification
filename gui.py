import gradio as gr
from ultralytics import YOLO
from PIL import Image,ImageEnhance
model1=YOLO('best.pt')
model2=YOLO('yolov8m-seg.pt')
def pre(x):
    prd=model2.predict([x])
    tmp=prd[0]
    mx=0; p=[0,0,0,0]
    boxes=tmp.boxes.xyxy.numpy(); classes=tmp.boxes.cls.numpy()
    for box,cls in zip(boxes,classes):
        if not cls==6:
            continue
        area=(box[2]-box[0]+1)*(box[3]-box[1]+1)
        if(area>mx):
            mx=area; p=box
    # print(box)
    if(p[2]==0 and p[3]==0):
        return x,-1
    img=x
    cropped=img.crop((p[0],p[1],p[2],p[3]))
    return cropped,1

def pred(x,iscrop,rot,bri,cot,col,srp):
    img=Image.fromarray(x)
    img=img.rotate(rot)
    img=img.crop(img.getbbox())
    img=ImageEnhance.Brightness(img).enhance(bri)
    img=ImageEnhance.Contrast(img).enhance(cot)
    img=ImageEnhance.Color(img).enhance(col)
    img=ImageEnhance.Sharpness(img).enhance(srp)
    x=img
    if iscrop:
        x,sta=pre(x)
        if(sta==-1):
            iscrop=0
            gr.Warning('No trains got. Check your image!')
    res=model1.predict([x],task="classify")
    rat=x.size[1]/x.size[0]
    if x.size[0]>600 and rat<=1:
        x=x.resize((600,int(600*rat)))
    elif x.size[1]>600 and rat>1:
        x=x.resize((int(600/rat),600))
    top1p=res[0].probs.top1conf.item()
    # top1n=res[0].names[res[0].probs.top1]
    if(top1p<0.35):
        gr.Warning('Probably not a train!')
    elif(top1p<0.8):
        gr.Warning('Not sure about the answer.')
    oup={}; j=0
    for i in res[0].probs.top5:
        if j==3:
            break
        oup[res[0].names[i]]=res[0].probs.top5conf[j]
        j+=1
    return [x,oup]
demo=gr.Interface(
    fn=pred,
    inputs=[gr.Image(label='upload .jpg',show_download_button=False),gr.Checkbox(label='Autocrop',value=True),gr.Slider(minimum=-180,maximum=180,step=1,value=0,label='Rotate'),
            gr.Slider(minimum=0.1,maximum=3,step=0.05,value=1,label='Brightness'),gr.Slider(minimum=0.1,maximum=2,step=0.1,value=1.2,label='Contrast'),
            gr.Slider(minimum=0.1,maximum=2,step=0.1,value=1.2,label='Color'),gr.Slider(minimum=0.5,maximum=4,step=0.1,value=1.5,label='Sharpness')],
    outputs=[gr.Image(label='Processed',show_download_button=False),gr.Label(num_top_classes=3,label='Result')],
    title='CR locomotives classification tool',
    description='made by xqqqwa | Enjoy!',
    article='data from www.xiaguanzhan.com'
)
demo.launch()
