# 一问一答机器人web api接口
访问此api接口之前，请按照[机器人管理平台部署指南](机器人管理平台部署指南.md)完成Anyq平台的部署。

**注：发送请求时根据机器人部署的服务器地址与端口对请求进行调整**

## 创建机器人
**http请求示例**
```http
POST http://localhost:8080/robot_manager/single/create_robot HTTP/1.1
Content-Type: application/json

{
    "robot_code": "你好"
}
```
**参数说明**
- robot_code: 机器人编号（唯一标识）

**http返回示例**
```http
HTTP/1.1 200 OK
Connection: close
Server: TornadoServer/6.0.1
Content-Type: text/html; charset=UTF-8
Date: Fri, 27 Dec 2019 07:18:17 GMT
Content-Length: 18

{
  "status_code": 0
}
```
**返回参数说明**
- status_code: 状态码，0为请求成功，其他状态码为请求失败

## 向机器人添加数据
**http请求示例**
```http
POST http://localhost:8080/robot_manager/single/add_items HTTP/1.1
Content-Type: application/json

{
    "documents":[
        {
            "answer": "测试答案", 
            "question": "测试问题", 
            "id": "test_question_id_1"
        },
        {
            "answer": "测试答案", 
            "question": "测试问题", 
            "id": "test_question_id_2"
        }
    ],
    "robot_id": "test_robot_id"
}
```
**参数说明**
- robot_code: 机器人编号（唯一标识）
- documents: 需要添加的文档，每个文档应该有question, answer, id字段。其中id字段一定要是全局唯一标识

**http返回示例**
```http
HTTP/1.1 200 OK
Connection: close
Server: TornadoServer/6.0.1
Content-Type: text/html; charset=UTF-8
Date: Fri, 27 Dec 2019 07:24:47 GMT
Content-Length: 18

{
  "status_code": 0
}
```
**返回参数说明**
- status_code: 状态码，0为请求成功，其他状态码为请求失败


## 删除机器人的某些数据
**http请求示例**
```http
POST http://localhost:8080/robot_manager/single/delete_items HTTP/1.1
Content-Type: application/json

{
    "q_ids": ["test_question_id_2"],
    "robot_code": "test_robot_id"
}
```
**参数说明**
- robot_code: 机器人编号（唯一标识）
- q_ids: 问答对的id列表，其中的id对应添加问答对时的id。其中id字段一定要是全局唯一标识

**http返回示例**
```http
HTTP/1.1 200 OK
Connection: close
Server: TornadoServer/6.0.1
Content-Type: text/html; charset=UTF-8
Date: Fri, 27 Dec 2019 07:24:47 GMT
Content-Length: 18

{
  "status_code": 0
}
```
**返回参数说明**
- status_code: 状态码，0为请求成功，其他状态码为请求失败

## 删除整个机器人
**http请求示例**
```http
POST http://localhost:8080/robot_manager/single/delete_robot HTTP/1.1
Content-Type: application/json

{
    "robot_code": "test_robot_id"
}
```
**参数说明**
- robot_code: 机器人编号（唯一标识）

**http返回示例**
```http
HTTP/1.1 200 OK
Connection: close
Server: TornadoServer/6.0.1
Content-Type: text/html; charset=UTF-8
Date: Fri, 27 Dec 2019 07:27:22 GMT
Content-Length: 18

{
  "status_code": 0
}
```
**返回参数说明**
- status_code: 状态码，0为请求成功，其他状态码为请求失败


## 向机器人提问
**http请求示例**
```http
POST http://localhost:8080/robot_manager/single/ask HTTP/1.1
Content-Type: application/json

{
    "robot_code": "test_robot_id",
    "service_type": "一问一答",
    "data": {
        "question": "测试问题"
    }
}
```
**参数说明**
- robot_code: 机器人编号（唯一标识）
- service_type: 服务类型，目前暂时填写`一问一答`
- data: 包含唯一字段question，为用户提问的问题

**http返回示例**
```http
HTTP/1.1 200 OK
Connection: close
Content-Length: 339
Server: TornadoServer/6.0.1
Content-Type: text/html; charset=UTF-8
Date: Fri, 27 Dec 2019 07:38:12 GMT

{
  "data": {
    "relatedQuestions": [],
    "text": "测试答案",
    "video_url": [],
    "img_url": []
  },
  "robot_code": "test_robot_id",
  "service_code": "d64585a6-287b-11ea-8aec-0242ac11000c",
  "answer_code": "d64585a6-287b-11ea-8aec-0242ac11000c",
  "answer_type": "text",
  "service_type": "一问一答",
  "ask_code": "d64585a6-287b-11ea-8aec-0242ac11000c"
}
```
**返回参数说明**
- answer_type: 答案类型，目前仅为text，为预留参数
- robot_code: 机器人编号（唯一标识）
- service_code: 当前服务的唯一标识
- ask_code: 当前问题的唯一标识
- answer_code: 当前答案的唯一标识
- service_type: 服务类型，目前暂时填一问一答
