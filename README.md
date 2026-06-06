# InterviewGPT

基于 Ollama + Qwen3 + Gradio 的 AI 模拟面试系统。

## 项目简介

InterviewGPT 是一个本地运行的大模型面试助手，支持多轮技术面试、自动评分和能力评估。

用户可以选择目标岗位进行模拟面试，系统会自动提出技术问题，对回答进行分析并给出反馈，帮助求职者提升面试能力。

---

## 功能演示

### V2.0

✅ 多轮面试

✅ AI自动评分

✅ 面试题自动切换

✅ 回答记录保存

✅ 成绩统计

✅ 本地运行

---

## 技术栈

* Python
* Gradio
* Ollama
* Qwen3
* Prompt Engineering

---

## 项目结构

```text
interview-gpt
│
├── app.py
├── scorer.py
├── questions.py
├── README.md
└── requirements.txt
```

---

## 工作流程

```text
开始面试
    ↓
生成面试题
    ↓
用户作答
    ↓
Qwen3评分
    ↓
生成反馈
    ↓
自动切换下一题
    ↓
统计成绩
    ↓
结束面试
```

---

## 当前支持题库

### AI应用开发工程师

* 什么是RAG？
* 什么是Embedding？
* LangChain有什么作用？
* 什么是Prompt Engineering？
* 什么是Agent？

---

## 安装

### 克隆仓库

```bash
git clone https://github.com/你的用户名/interview-gpt.git
cd interview-gpt
```

### 创建虚拟环境

```bash
python -m venv venv
```

Windows：

```bash
venv\Scripts\activate
```

### 安装依赖

```bash
pip install gradio ollama
```

### 安装模型

```bash
ollama run qwen3:8b
```

---

## 启动项目

```bash
python app.py
```

访问：

```text
http://127.0.0.1:7860
```

---

## 示例

### 面试题

```text
什么是RAG？
```

### 用户回答

```text
RAG是一种检索增强生成技术。
```

### AI评价

```text
评分：8

优点：
回答了核心概念

缺点：
未说明向量检索流程
```

---

## 项目亮点

### 多轮面试机制

支持连续面试流程，而非单次问答。

### AI自动评分

利用大模型分析回答质量。

### 成绩统计

自动计算平均分。

### 可扩展题库

新增岗位只需增加问题配置。

---

## 开发路线

### V1.0

* 单题面试
* AI评分

### V2.0（当前版本）

* 多轮面试
* 自动切换题目
* 成绩统计

### V3.0（开发中）

* AI面试报告
* 能力画像
* 学习建议
* PDF导出

### V4.0

* 多岗位支持
* 数据分析师
* Python开发工程师
* 机器学习工程师

### V5.0

* FastAPI接口
* Docker部署
* 用户系统

---


---

## 作者

连明凡

数据科学与大数据技术专业

方向：

* AI应用开发
* 大模型应用
* RAG系统
* Agent开发

---

## License

MIT License
