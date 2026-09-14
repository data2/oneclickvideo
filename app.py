# -*- coding: utf-8 -*-
"""
本地 TTS 工具：输入文案，选择音色，生成音频和字幕
"""

import subprocess
import sys
from pathlib import Path
import gradio as gr

# 输出目录
OUTPUT_DIR = Path(r"D:\soft\moneyPrinterTurbo\素材库")

# Edge TTS 常用中文音色列表
VOICES = {
    "云健（沉稳男声）": "zh-CN-YunjianNeural",
    "云希（年轻男声）": "zh-CN-YunxiNeural",
    "云扬（专业男声）": "zh-CN-YunyangNeural",
    "晓晓（温柔女声）": "zh-CN-XiaoxiaoNeural",
    "晓伊（沉稳女声）": "zh-CN-XiaoyiNeural",
    "辽宁小北（东北女声）": "zh-CN-liaoning-XiaobeiNeural",
    "陕西小妮（陕西方言）": "zh-CN-shaanxi-XiaoniNeural",
}


def generate(text, voice_label):
    """生成音频和字幕"""
    if not text.strip():
        return None, None, "文案不能为空"

    voice = VOICES.get(voice_label, "zh-CN-YunjianNeural")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    audio_file = OUTPUT_DIR / "audio.mp3"
    subtitle_file = OUTPUT_DIR / "subtitle.srt"

    cmd = [
        sys.executable, "-m", "edge_tts",
        "--text", text,
        "--voice", voice,
        "--write-media", str(audio_file),
        "--write-subtitles", str(subtitle_file)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    if result.returncode != 0:
        return None, None, f"生成失败：{result.stderr[-300:]}"

    return str(audio_file), str(subtitle_file), "生成成功！"


def build_ui():
    with gr.Blocks(title="TTS 音频字幕生成器") as demo:
        gr.Markdown("## 🎙️ TTS 音频字幕生成器")
        gr.Markdown("输入文案，选择音色，一键生成音频和字幕。")

        with gr.Row():
            with gr.Column(scale=2):
                text_input = gr.Textbox(
                    label="文案",
                    placeholder="在这里粘贴文案...",
                    lines=8
                )
                voice_select = gr.Dropdown(
                    label="音色",
                    choices=list(VOICES.keys()),
                    value="云健（沉稳男声）"
                )
                generate_btn = gr.Button("生成音频和字幕", variant="primary")

            with gr.Column(scale=1):
                audio_output = gr.Audio(label="生成的音频", type="filepath")
                subtitle_output = gr.File(label="生成的字幕文件")
                status = gr.Textbox(label="状态", interactive=False)

        generate_btn.click(
            fn=generate,
            inputs=[text_input, voice_select],
            outputs=[audio_output, subtitle_output, status]
        )

    return demo


if __name__ == "__main__":
    app = build_ui()
    app.launch(server_name="127.0.0.1", server_port=7861)