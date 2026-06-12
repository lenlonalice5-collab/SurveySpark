# InterviewGPT

<p align="center">
  <b>AI-Powered Technical Interview Simulator</b><br>
  基于 Large Language Model 的智能技术面试模拟平台
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue">
  <img src="https://img.shields.io/badge/Gradio-WebUI-orange">
  <img src="https://img.shields.io/badge/DeepSeek-LLM-green">
  <img src="https://img.shields.io/badge/Whisper-ASR-purple">
  <img src="https://img.shields.io/badge/SQLite-Database-yellow">
  <img src="https://img.shields.io/badge/Version-v6.4-red">
</p>

---

# 📖 Project Overview | 项目简介

InterviewGPT is an AI-powered mock interview platform built with Large Language Models.

It automatically generates interview questions, evaluates candidate responses, creates follow-up questions, performs competency analysis, stores interview records, and generates professional interview reports.

InterviewGPT 是一个基于大语言模型（LLM）的智能模拟面试系统。

系统能够自动生成面试题、分析候选人回答、动态追问、能力评估、数据存储，并生成专业面试报告。

---

# ✨ Features | 核心功能

## 🤖 AI Interview Simulation

智能面试模拟

* 岗位定制化面试题生成
* 多岗位扩展支持
* 模拟真实技术面试流程
* 重新生成题目

---

## 🧠 AI Answer Evaluation

AI 回答评分

* 自动评分
* 回答质量分析
* 优缺点反馈
* 综合能力评估

---

## 🔄 Dynamic Follow-up Questions

智能追问机制

* AI 自动生成追问
* 基于回答内容继续深入
* 自动控制追问轮次
* 提高面试真实性

---

## 🎤 Local Speech Recognition

本地语音识别

Powered by Whisper

* 麦克风录音
* 中文语音转文字
* 完全本地运行
* 无需第三方语音服务
* 支持离线环境

---

## 📊 Interview Progress Tracking

面试进度跟踪

* 当前题目进度
* 完成百分比
* 面试时长统计
* 实时更新

---

## 🎯 Skill Profile Analysis

能力画像分析

自动统计：

* Python
* Machine Learning
* Deep Learning
* NLP
* Data Analysis
* LLM Engineering

等能力维度表现。

---

## 📈 Radar Chart Visualization

能力雷达图

自动生成：

* 技能评分
* 能力分布
* 雷达图可视化
* PDF 集成

---

## 📄 AI Interview Report

AI 面试报告

自动生成：

* 综合评价
* 优势分析
* 不足分析
* 学习建议
* 成长方向

---

## 📑 PDF Export

PDF 导出

支持导出：

* AI面试报告
* 技能分析
* 面试统计
* 面试时长
* 雷达图

---

## 💾 Interview History

历史记录管理

* 本地历史记录
* JSON 存档
* 历史成绩查看

---

## 🗄️ SQLite Database

数据库支持（V6.3）

InterviewGPT now supports SQLite persistence.

InterviewGPT 已支持 SQLite 数据存储。

### interviews

存储：

* 岗位信息
* 面试题目
* 用户回答
* AI评分
* 时间记录

### users

存储：

* 用户名
* 累计得分
* 面试次数
* 注册时间

### mistakes

预留错题本功能

---

## 👤 User System

用户系统（V6.4）

支持：

* 用户登录
* 自动创建用户
* 成绩绑定用户
* 用户资料查看
* 累计面试统计

---

# 🏗️ System Architecture | 系统架构

```text
Gradio UI
    │
    ▼
InterviewGPT Core
    │
 ┌──┼───────────────┐
 ▼  ▼               ▼

Question      Scoring
Generator     Engine

 ▼
DeepSeek API

 ▼

Follow-up Engine

 ▼

Report System
 ├─ Statistics
 ├─ Skill Analysis
 ├─ Radar Chart
 └─ PDF Export

 ▼

Whisper ASR
(Voice → Text)

 ▼

SQLite Database
 ├─ Users
 ├─ Interviews
 └─ Mistakes
```

# 📂 Project Structure | 项目结构

```text
InterviewGPT/

├── app.py
├── database.py
├── speech.py
├── scorer.py
├── followup.py
├── report.py
├── history.py
├── radar_chart.py
├── pdf_export.py
├── question_generator.py

├── interview.db
├── history.json

├── reports/
├── charts/

├── requirements.txt
└── README.md
```

# 🚀 Installation | 安装

## 1. Clone Repository

```bash
git clone https://github.com/yourname/interview-gpt.git

cd interview-gpt
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Install Whisper

```bash
pip install openai-whisper
```

## 5. Install FFmpeg

Verify：

```bash
ffmpeg -version
```

# ▶️ Run

```bash
python app.py
```

Open:

```text
http://127.0.0.1:7860
```

# 📊 Current Capabilities | 当前能力

| Module              | Status |
| ------------------- | ------ |
| Question Generation | ✅      |
| AI Scoring          | ✅      |
| Follow-up Questions | ✅      |
| Whisper ASR         | ✅      |
| Progress Tracking   | ✅      |
| Statistics          | ✅      |
| Skill Analysis      | ✅      |
| Radar Chart         | ✅      |
| PDF Export          | ✅      |
| History Records     | ✅      |
| SQLite Database     | ✅      |
| User System         | ✅      |

# 🛣️ Roadmap

## V6.5

Planned Features

* 🏆 Leaderboard
* ❌ Mistake Book
* 📈 Growth Curve
* 👥 Multi-user Statistics
* 🔍 Database Search

## V7.0

Long-term Plan

* RAG Interview System
* Local LLM Support
* Multi-modal Interview
* Online Deployment
* Enterprise Interview Platform

# 🧑‍💻 Author

Developed by Lenlon

Built with:

* Python
* Gradio
* DeepSeek API
* Whisper
* SQLite
* ReportLab
* Matplotlib

# 📜 License

MIT License

Feel free to use, modify and contribute.

欢迎 Star ⭐ 和 Fork 🍴
