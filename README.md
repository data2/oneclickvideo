# oneclickvideo

## 一键创建环境

conda create -n one-click-video python=3.11 pip -y

conda activate one-click-video

pip install moviepy edge-tts gradio requests 

python -c "import gradio, edge_tts, moviepy; print('OK')"





