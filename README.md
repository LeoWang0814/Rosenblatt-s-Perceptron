# Rosenblatt's Perceptron 可视化 / Visualization of Rosenblatt's Perceptron

本项目展示了 Rosenblatt 感知机（Perceptron）算法在逻辑门学习中的训练过程，并以表格形式打印出每次迭代中权重的变化、预测输出和权重更新值，帮助理解其学习机制。

This project visualizes the training process of the Rosenblatt Perceptron algorithm with an example of learning a logic gate (e.g., AND gate). The output shows each epoch’s weight updates, predictions, and learning deltas in a clear tabular format, helping users understand how the perceptron learns.

---

## 📌 特性 Features

- 使用 Python 实现感知机核心训练算法  Use Python to implement the perceptron core training algorithm.
- 支持自定义训练数据（默认为 AND 门数据）  Support custom training data (default is AND gate data).
- 每一步训练过程的详细可视化输出  Detailed visual output of each step of the training process.
- 无需外部依赖，直接运行  No external dependencies are required.

---

## 🧠 感知机简介 What is a Perceptron?

感知机是一种二分类线性分类器，是人工神经网络的基础构件。它通过调整权重来学习输入与目标输出之间的关系。

The perceptron is a simple binary linear classifier and a fundamental building block in neural networks. It learns to distinguish between two classes by adjusting its weights based on input-output errors.

---

## 📂 项目结构 Project Structure

```

Rosenblatt-s-Perceptron/
├── main.py         # 主程序 Main script for training visualization
├── README.md             # 项目说明文档 This file

````

---

## ▶️ 使用方法 How to Run

确保你已经安装了 Python（无需额外依赖）。

输出内容将展示每一轮 (epoch) 中每一个样本的训练过程，包括：

* 当前权重 (Initial Weights)
* 输入值 (Inputs)
* 目标输出 (Target)
* 实际输出 (Output)
* 更新值 (Deltas)
* 更新后的权重 (Updated Weights)

---

## 🧪 示例数据 Example Data (AND Gate)

```python
testData = [[1, -1, -1, -1],
            [1, 1, -1, -1],
            [1, -1, 1, -1],
            [1, 1, 1, 1]]  # AND gate
```

* 输入前三个值为偏置项 `x0=1` 与两个特征 `x1`, `x2`
* 第四个值为目标输出 `target`
* 感知机通过多个 epoch 迭代训练，使得输出逐渐接近目标

---

## 📊 输出示例 Output Sample

```
 Epoch |   i   |  w0      w1      w2   |  x0      x1      x2   |target  output   delta |deltaW0 deltaW1 deltaW2|finalW0 finalW1 finalW2
   1   |   1   |   0       0       0   |   1      -1      -1   |  -1       1      -2   | -0.2     0.2     0.2  | -0.2     0.2     0.2  
   ...
```

---

## 📖 学习用途 Learning Purpose

这个程序适用于：

* 初学神经网络的学生
* 机器学习课堂教学可视化演示
* 理解感知机算法权重更新机制的用户

This program is ideal for:

* Students new to neural networks
* In-class visualization demos for ML courses
* Anyone wanting to understand how perceptrons update weights during training

---

## 📄 许可证 License

MIT License

---

欢迎 star ⭐ 或 fork 🍴！
Feel free to ⭐ star or 🍴 fork the project!
