# InterviewGPT

基于 Ollama + Qwen3 + Gradio 构建的本地 AI 模拟面试系统。

## 项目简介

InterviewGPT 是一个面向 AI 应用开发岗位的智能面试助手。

系统能够模拟真实技术面试流程，通过大模型自动生成反馈、评估回答质量，并在面试结束后生成完整的 AI 面试报告与能力画像。

项目完全本地运行，无需调用云端 API。

---

## 功能版本

### V1.0

* 单轮技术面试
* AI自动评分
* 回答反馈

### V2.0

* 多轮面试
* 自动切换题目
* 成绩统计
* 面试记录保存

### V3.0（当前版本）

* AI面试报告生成
* 能力画像分析
* 优势分析
* 不足分析
* 学习建议
* 录用建议

---

## 项目流程

```text
开始面试
    ↓
AI提出问题
    ↓
用户回答
    ↓
Qwen3评分
    ↓
记录成绩
    ↓
进入下一题
    ↓
完成面试
    ↓
生成AI面试报告
    ↓
生成能力画像
```

---

## 技术栈

### AI模块

* Ollama
* Qwen3:8B
* Prompt Engineering

### 应用开发

* Python
* Gradio

### 数据处理

* JSON
* Python Dict/List

---

## 项目结构

```text
interview-gpt
│
├── app.py
├── scorer.py
├── report.py
├── questions.py
├── README.md
├── requirements.txt
└── screenshots
```

---

## 核心功能

### 1. 多轮面试

支持连续技术面试流程。

示例：

* 什么是RAG？
* 什么是Embedding？
* LangChain有什么作用？
* 什么是Prompt Engineering？
* 什么是Agent？

---

### 2. AI自动评分

根据回答质量自动评估：

* 准确性
* 完整性
* 专业性

输出示例：

```text
评分：8

优点：
理解了核心概念

缺点：
缺少实际应用说明
```

---

### 3. AI面试报告

面试结束后自动生成：

* 总体评价
* 优势分析
* 不足分析
* 学习建议
* 录用建议

示例：

```text
总体评价：

具备基础AI应用开发能力。

优势：

理解RAG与Prompt工程。

不足：

Agent与系统设计经验较少。

建议：

学习CrewAI、FastAPI、Docker。

录用建议：

适合作为初级AI应用开发工程师培养。
```

---

### 4. 能力画像

根据不同知识点统计得分：

```text
RAG         8/10
Embedding   7/10
LangChain   8/10
Prompt      9/10
Agent       5/10
```

帮助用户快速发现薄弱环节。

---

## 安装教程

### 克隆项目

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

### 下载模型

```bash
ollama run qwen3:8b
```

---

## 启动项目

```bash
python app.py
```

启动后访问：

```text
http://127.0.0.1:7860
```

---

## 当前支持岗位

### AI应用开发工程师

题库包含：

* RAG
* Embedding
* LangChain
* Prompt Engineering
* Agent

---

## 项目亮点

### 本地大模型应用

无需 OpenAI API 即可运行。

### 多轮面试机制

模拟真实技术面试流程。

### AI自动分析

自动生成结构化反馈。

### 能力画像

基于知识点维度分析能力。

### 可扩展架构

支持新增岗位与题库。

---

## 开发路线

### 已完成

* [x] V1 单轮面试
* [x] V2 多轮面试
* [x] V3 AI面试报告

### V4（计划开发）

* [ ] PDF报告导出
* [ ] 多岗位题库
* [ ] 历史记录系统
* [ ] 成绩排行榜

### V5（计划开发）

* [ ] FastAPI后端
* [ ] SQLite数据库
* [ ] 用户系统
* [ ] Docker部署

---

## 项目截图

后续补充：

```text
screenshots/
├── home.png
├── interview.png
├── report.png
└── skill_report.png
```

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
