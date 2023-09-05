    import gradio as gr
    import numpy as np
    from time import time
    from random import choice


    def cat_btn_clicked(last_time):
        now = time()
        elapsed_time = now-last_time
        elapsed_time = round(elapsed_time, 2)
        return f"Cat, {elapsed_time}", now, f'https://loremflickr.com/500/500/{choice(["cat","dog"])}'

    def dog_btn_clicked(last_time):
        now = time()
        elapsed_time = now-last_time
        elapsed_time = round(elapsed_time, 2)
        return f"Dog, {elapsed_time}", now, f'https://loremflickr.com/500/500/{choice(["cat","dog"])}'


    if __name__ == '__main__':
        with gr.Blocks() as demo:
            last_time = gr.State(time())
            with gr.Row():
                image_box = gr.Image('https://loremflickr.com/500/500/cat', shape=(500, 500), height=500, width=500)
            with gr.Row():
                cat_btn = gr.Button("cat")
                dog_btn = gr.Button("dog") 
            timer_box = gr.Textbox("0")
            cat_btn.click(cat_btn_clicked, inputs=[last_time], outputs=[timer_box, last_time, image_box])
            dog_btn.click(dog_btn_clicked, inputs=[last_time], outputs=[timer_box, last_time, image_box])
        demo.launch(share=True)
