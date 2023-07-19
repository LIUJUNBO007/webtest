import openai

# 设置OpenAI API密钥
openai.api_key = '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'


# 定义一个函数，用于与ChatGPT进行交互
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # 使用Chat模型
        prompt=prompt,
        max_tokens=1024,  # 生成的回复长度限制
        temperature=0.7,  # 控制生成回复的创造性，值越高越随机
        n=1,  # 生成1个回复
        stop=None  # 停止生成回复的条件，None表示没有特定的停止条件
    )
    reply = response.choices[0].text.strip()
    return reply


# 提供一个初始的对话上下文
conversation = "User: Hello\nAI: Hi, how can I help you today?"

# 循环与ChatGPT进行交互
while True:
    user_input = input("User: ")
    conversation += "\nUser: " + user_input

    # 将对话上下文发送给ChatGPT进行生成回复
    reply = chat_with_gpt(conversation)
    print("AI: " + reply)

    # 更新对话上下文
    conversation += "\nAI: " + reply