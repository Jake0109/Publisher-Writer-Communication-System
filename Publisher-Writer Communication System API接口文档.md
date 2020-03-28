# Publisher-Writer Communication System API接口文档

## 通用说明：

### 接口环境

> 测试环境：http://127.0.0.1:5000
>
> 生产环境：待定

### 接口通用返回

```
{
    "status": 200, 	// 正确码为2XX,错误码为4XX,5XX 
    "msg": "", 		// 正确返回和错误返回的信息
    "data":{		// 正确返回时的数据   
    }
}
```

## 管理员模块

### 管理员接口

#### 获取单个管理员信息

- 说明

> 获取单个管理员信息

- 请求URL

> 127.0.0.1:5000/admin/admin/\<int:admin_id>/

- 请求方式

> GET

- 请求参数

> 无

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "admin successfully got",
    "status": 200,
    "data": {
        "username": "jake",
        "password": "pbkdf2:sha256:150000$7eCCXiQj$03f6400c1f33ba1b123dfd1dddae013ae795e002f1e1781e6e371e62fcb70912"
    }
}
```

#### 注册管理员

- 说明

> 用于管理员注册
>
> 测试账号：username=jake password=jakepassword

- 请求URL

> 127.0.0.1:5000/admin/admins/?action=register

- 请求方式

> POST

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明   |
| -------- | ---- | -------- | ------ |
| usernam  | 是   | String   | 用户名 |
| password | 是   | String   | 密码   |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "admin successfully created",
    "status": 201,
    "data": {
        "username": "jake",
        "password": "pbkdf2:sha256:150000$7eCCXiQj$03f6400c1f33ba1b123dfd1dddae013ae795e002f1e1781e6e371e62fcb70912"
    }
}
```

#### 管理员登录

- 说明

> 管理员登录
>
> 测试账号：username=jake password=jakepassword

- 请求URL

> 127.0.0.1:5000/admin/admins/?action=login

- 请求方式

> POST

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明   |
| -------- | ---- | -------- | ------ |
| usernam  | 是   | String   | 用户名 |
| password | 是   | String   | 密码   |

- 返回字段

| 返回字段 | 字段类型 | 说明                                                         |
| -------- | -------- | ------------------------------------------------------------ |
| status   | Integer  | http状态码                                                   |
| msg      | String   | 返回的状态信息                                               |
| token    | String   | 登录成功后生成token保存在后端缓存<br />用户在需要登录的场景需要验证token |

- 返回示例

```json
{
    "msg": "successfully login",
    "status": 200,
    "token": "admin55e1618618f84eb785adc2329ff8d121",
    "data": {
        "username": "jake",
        "password": "pbkdf2:sha256:150000$7eCCXiQj$03f6400c1f33ba1b123dfd1dddae013ae795e002f1e1781e6e371e62fcb70912"
    }
}
```

#### 修改管理员信息

- 说明

> 修改单个管理员信息（密码）

- 请求URL

> 127.0.0.1:5000/admin/admins/

- 请求方式

> PATCH

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                 |
| -------- | ---- | -------- | -------------------- |
| token    | 是   | String   | 用于校验用户登录状态 |
| password | 是   | String   | 密码                 |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "successfully changed",
    "status": 200,
    "data": {
        "username": "jake",
        "password": "pbkdf2:sha256:150000$G4LGSHq4$d854aef0a2f4bd2b2fa4e4bd057263f08edb60f0469800cdf083186a3a9ceb62"
    }
}
```

#### 删除管理员

- 说明

> 删除管理员
>
> 测试账号：super_admin=jake admin=Jake

- 请求URL

> 127.0.0.1:5000/admin/admin/\<int:admin_id>/

- 请求方式

> PATCH

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明           |
| -------- | ---- | -------- | -------------- |
| admin_id | 是   | Integer  | 删除的管理员ID |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "successfully deleted",
    "status": 200
}
```

#### 获取所有管理员信息

- 说明

> 获取所有管理员信息
>
> 测试账号：super_admin=jake admin=Jake

- 请求URL

> 127.0.0.1:5000/admin/admins/

- 请求方式

> GET

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                      |
| -------- | ---- | -------- | ------------------------- |
| token    | 是   | String   | 验证是否是Super admin用户 |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "admins successfully get",
    "status": 200,
    "data": [
        {
            "username": "jake",
            "password": "pbkdf2:sha256:150000$G4LGSHq4$d854aef0a2f4bd2b2fa4e4bd057263f08edb60f0469800cdf083186a3a9ceb62"
        },
        {
            "username": "Jake",
            "password": "pbkdf2:sha256:150000$xuEomeSR$5503e7f9985c8c50c97ba4749509763eacac86a43dd02df8ae3958d529e34a95"
        }
    ]
}
```

### 合同接口

#### 获取单个合同信息

#### 获取所有合同信息

### 标签接口

#### 添加标签

#### 删除标签

#### 获取复数标签

## 出版社模块

### 出版社接口

#### 获取单个出版社信息

#### 注册出版社

#### 出版社登录

#### 修改出版社信息

#### 删除出版社

#### 获取复数出版社信息

### 出版社-标签关系接口

#### 添加出版社-标签关系

#### 删除出版社-标签关系

### 合同接口

#### 获取单个合同信息

#### 上传合同信息

#### 更改合同状态

#### 删除合同

#### 获取出版社所有合同信息

## 作家模块

### 作家接口

#### 获取单个作家信息

#### 作家注册

#### 作家登录

#### 修改作家信息

#### 删除作家

#### 获取所有作家信息

### 合同接口

#### 获取单个合同信息

#### 修改合同状态

#### 获取作家所有合同信息