from ollama import chat
import re

def score_answer(question, answer):

    prompt = f"""
你是AI面试官。

问题：
{question}

候选人回答：
{answer}

评分规则：

10分：回答完整准确
8-9分：回答基本正确
6-7分：部分正确
4-5分：理解不足
0-3分：错误或无关

请严格按照以下格式输出：

评分：

优点：
xxx

缺点：
xxx
"""

    response = chat(
        model="qwen3:8b",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    content = response["message"]["content"]

    match = re.search(r"评分[:：]\s*(\d+)", content)

    score = int(match.group(1)) if match else 0

    return score, content