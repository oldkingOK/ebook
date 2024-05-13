<center>

# E-Book

</center>

## 关于

本地部署 e-book

## Docker

构建

```shell
docker build -t ebook .
```

运行

```shell
docker run --name ok_ebook -p 8080:8080 ebook
```