# AI 社区核心 API
## 环境准备

- Python 3.8+ 环境

## 1、克隆项目到本地

## 2、安装项目依赖：
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```
## 3、运行项目
### uvicorn启动
   ```bash
   uvicorn main:app --reload
   ```
### docker启动
   ```bash
   docker-compose up -d
   ```
### 4、访问 API 文档：
 http://127.0.0.1:8000/docs

##  API 

##### /posts 新增/查询  --- 新增需要传参
```json
{
    "title":"",
    "content":""
}
```
##### /posts/{post_id}  删帖
##### /posts/{post_id}/comments   加评论 
##### /comments/{comment_id}  删评论 
##### /posts/{post_id}/comments   按根品论分页

## 为什么用 FastAPI、SQLite
性能比肩 Go 了，异步、并发友好，快速开发
SQLite方便demo演示

## 数据库结构设计原因

除了其他必要字段，没创建太多字段
最关键的就是文章id、评论id、评论父级id

## 接口测试
##### 删除评论
![](https://github.com/GalokPeng/qizhi2046-demo/blob/5fa419f6333ae1cccde3eb835f18a56636ef2fec/del_comment.png)
##### 删除文章
![](https://github.com/GalokPeng/qizhi2046-demo/blob/5fa419f6333ae1cccde3eb835f18a56636ef2fec/del_posts.png)
##### 查询评论
![](https://github.com/GalokPeng/qizhi2046-demo/blob/5fa419f6333ae1cccde3eb835f18a56636ef2fec/select_comments.png)
##### 查询文章
![](https://github.com/GalokPeng/qizhi2046-demo/blob/5fa419f6333ae1cccde3eb835f18a56636ef2fec/select_posts.png)
##### 添加品论
![](https://github.com/GalokPeng/qizhi2046-demo/blob/5fa419f6333ae1cccde3eb835f18a56636ef2fec/add_comment.png)
##### 添加文章
![](https://github.com/GalokPeng/qizhi2046-demo/blob/5fa419f6333ae1cccde3eb835f18a56636ef2fec/add_posts.png)
