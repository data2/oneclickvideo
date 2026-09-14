# oneclickvideo

## 一键创建环境

conda create -n one-click-video python=3.11 pip -y

conda activate one-click-video

pip install moviepy edge-tts gradio requests 

## 验证

python -c "import gradio, edge_tts, moviepy; print('OK')"

## 访问地址

浏览器打开 http://127.0.0.1:7861




