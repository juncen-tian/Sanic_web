apis
==========

## login接口

```http request
method: post
path: /panel/v1/login

入参：
params: username  string   required
        password  string   required
        valid_code  string   required

{
    "code": 0,
    "msg": "成功",
    "data": {
        "user_id": 1,
        "username": "teacher",
        "user_type": 0,
        "token": "xxx.xxx.xxx"  // 所有接口都增加了token校验，过期时间设置为24小时，token需要在request的header里面传递 {"token":token}
    }
}
```

## valid_image接口

```http request
method: get
path: /panel/v1/valid/image

入参：
params:

response:
{
    "code": 0,
    "msg": "成功",
    "data": {
        "image": "base64编码的图片",
    }
}
```

## user/list接口

```http request
method: get
path: /panel/v1/user/list

入参：
params: page  int  默认值为1 从1开始
        limit  int  默认值为10 最小值为1 最大值为100

{
    "code": 0,
    "msg": "成功",
    "data": {
        "data": [
            {
                "username": "test654322",
                "password": "test",
                "user_type": 1,
                "data_tagging": "asdasdasdasdzxcxzcqweqwarqfasfdas",
                "model_build": "",
                "model_check": "",
                "equipment": "asdasdasdsa"
            }
        ]
    }
}
```

## user/insert接口

```http request
method: post
path: /panel/v1/user/inster

入参：
params: username  string   required
        password  string   required
        equipment  string  
        data_tagging  string 
        model_build  string
        model_check  string
        user_type  int   默认值为1 传值为0可以新增老师账号  创建学生账号可以不传这个参数

{
    "code": 0,
    "msg": "成功",
    "data": {
        "user_id": 1
    }
}
```

## user/update接口

```http request
method: post
path: /panel/v1/user/update

入参：
params: username  string   required
        password  string   required
        user_id  int   required
        equipment  string  
        data_tagging  string 
        model_build  string
        model_check  string
        user_type  int   默认值为1 传值为0可以修改老师账号  创建学生账号可以不传这个参数

{
    "code": 0,
    "msg": "成功",
    "data": {
        "user_id": 1
    }
}
```

## user/delete接口

```http request
method: post
path: /panel/v1/user/delete

入参：
params: user_id  int   required

{
    "code": 0,
    "msg": "成功",
    "data": {
        "user_id": 1
    }
}
```

## user/panel接口

```http request
method: get
path: /panel/v1/user/panel

入参：

response:
{
    "code": 0,
    "msg": "成功",
    "data": {
        "user": {
            "username": "test",
            "user_type": 1,
            "data_tagging": "",
            "model_build": "",
            "model_check": ""
        }
    }
}
```