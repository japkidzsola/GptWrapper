import gradio as gr

def chat_with_gpt5(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

gr.Interface(fn=chat_with_gpt5, inputs="text", outputs="text").launch()
