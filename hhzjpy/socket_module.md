---
title: py网络编程
date: 2020-03-19 16:42:05
categories: [python,]  
tags: [python,]
---

learn python
<!-- more -->

# py网络编程

Socket API调用流程 以及TCP数据流
![2020-03-19-16-43-10](http://img.noback.top/2020-03-19-16-43-10.png)
从上到下三次分别表述了TCP中的三次握手


Socket有两种类型，一种是Socket.SOCK_STREAM采用TCP 而Socket.SOCK_DGRAM采用的是UDP，但是我们采用的是TCP协议，他是一种有序可靠的协议。