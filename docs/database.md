数据库设计
====================

## 总

- 数据库服务   
  -- sqlite3
- 相关数据表   
  -- User  用户表，用来存储教师和学生的信息  
  

## 表设计
### 表名 User
|  字段名   | 数据类型  | desc |
|  ----  | ----  | ---- |
| id  | Integer | 自增主键 |
| username  | String | 用户名 |
| password  | String | 密码 |
| equipment  | string | 设备信息 |
| user_type  | Integer | 区分用户类型是教师还是学生 0教师 1学生 |
| data_tagging  | String | 数据标注网址 |
| model_build  | String | 模型搭建网址 |
| model_check  | String | 模型验证网址 |
