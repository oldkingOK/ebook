<div align="center">

# E-Book

</div>

## 关于

本地部署 e-book

## 构建和运行

#### Docker

```shell
docker run --name ebook -p 8080:8080 oldkingok/ebook:latest
```

或手动构建

```shell
docker build -t username/ebook .
docker run --name ebook -p 8080:8080 username/ebook
```

#### 从源码运行

推荐使用 Python>3.10 + venv虚拟环境

```shell
pip install -r requirements.txt
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```

## 借物表

| 元素 | 来源 |
|------|------|
| 封面图（左）| [Pixiv @ハブリー](https://www.pixiv.net/en/artworks/113922651) |
| 阿尼亚Live2D | [Bilibili @天才设计学家](https://www.bilibili.com/video/BV1qC4y1S7yo) |
| L2D组件 | [oh-my-live2d](https://github.com/oh-my-live2d/oh-my-live2d) |
| 鼠标指针 | [shuiche-it/cnblog-mouse](https://github.com/shuiche-it/cnblog-mouse) |