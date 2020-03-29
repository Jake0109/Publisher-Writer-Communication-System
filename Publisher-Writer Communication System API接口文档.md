# Publisher-Writer Communication System API接口文档

[toc]

## 通用说明：

### 接口环境

> 测试环境：http://127.0.0.1:5000
>
> 生产环境：待定

### 接口通用返回

```json
{
    "status": 200, 	// HTTP状态码，正确码为2XX,错误码为4XX,5XX 
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

- 说明

> 获取单个合同信息
>
> 需要admin用户登录
>
> 测试账号：admin=jake

- 请求URL

> 127.0.0.1:5000/admin/contract/\<int:contract_id>/

- 请求方式

> GET

- 请求参数

| 请求参数    | 必选 | 参数类型 | 说明                           |
| ----------- | ---- | -------- | ------------------------------ |
| token       | 是   | String   | admin用户的token，登陆时获取。 |
| contract_id | 是   | Integer  | 请求的contract的ID             |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "contract successfully got.",
    "status": 200,
    "data": {
        "name": "jake-jake-contract",
        "publisher_id": 1,
        "writer_id": 1,
        "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
        "is_signed": true,
        "is_completed": false
    }
}
```

#### 获取所有合同信息

- 说明

> 获取所有合同信息
>
> 需要admin用户登录

- 请求URL

> 127.0.0.1:5000/admin/contracts/

- 请求方式

> GET

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                         |
| -------- | ---- | -------- | ---------------------------- |
| token    | 是   | String   | admin用户token，在登陆时获得 |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "contracts successfully got.",
    "status": 200,
    "data": [
        {
            "name": "jake-jake-contract",
            "publisher_id": 1,
            "writer_id": 1,
            "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "is_signed": true,
            "is_completed": false
        },
        {
            "name": "jake-jake-contract1",
            "publisher_id": 1,
            "writer_id": 1,
            "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "is_signed": false,
            "is_completed": false
        },
        {
            "name": "jake-jim-contract2",
            "publisher_id": 1,
            "writer_id": 2,
            "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "is_signed": false,
            "is_completed": false
        }
    ]
}
```

#### 删除合同

- 说明

> 删除合同
>
> 需要admin用户登录

- 请求URL

> 127.0.0.1:5000/admin/admin/\<int:contract_id>

- 请求方式

> DELETE

- 请求参数

| 请求参数    | 必选 | 参数类型 | 说明                      |
| ----------- | ---- | -------- | ------------------------- |
| token       | 是   | String   | 验证是否是Super admin用户 |
| contract_id | 是   | String   | 删除的contract的ID        |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "contract successfully deleted",
    "status": 200
}
```

### 标签接口

#### 添加标签

- 说明

> 添加一个标签
>
> 需要admin用户登录

- 请求URL

> 127.0.0.1:5000/admin/tags/

- 请求方式

> POST

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明       |
| -------- | ---- | -------- | ---------- |
| name     | 是   | String   | 标签的名字 |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "tag successfully created",
    "status": 201,
    "data": {
        "id": 2,
        "name": "Information Technology"
    }
}
```

#### 删除标签

- 说明

> 添加一个标签
>
> 需要admin用户登录

- 请求URL

> 127.0.0.1:5000/admin/tag/\<int:tag_id>/

- 请求方式

> DELETE

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明             |
| -------- | ---- | -------- | ---------------- |
| token    | 是   | String   | admin用户的token |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "tag successfully deleted",
    "status": 203
}
```

#### 获取复数标签

- 说明

> 获取所有标签
>
> 需要admin用户登录

- 请求URL

> 127.0.0.1:5000/admin/tags/

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
    "msg": "tags successfully got",
    "status": 200,
    "data": [
        {
            "id": 2,
            "name": "Information Technology"
        },
        {
            "id": 3,
            "name": "Python"
        },
        {
            "id": 4,
            "name": "Golang"
        }
    ]
}
```

## 出版社模块

### 出版社接口

#### 获取单个出版社信息

- 说明

> 获取单个出版社信息

- 请求URL

> 127.0.0.1:5000/publisher/publisher/\<int:publisher_id>/

- 请求方式

> GET

- 请求参数

| 请求参数     | 必选 | 参数类型 | 说明             |
| ------------ | ---- | -------- | ---------------- |
| publisher_id | 是   | Integer  | 出版社的数据库ID |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "status": 200,
    "msg": "successfully get writer",
    "data": {
        "username": "Jake",
        "name": "Jake Publisher",
        "identifier": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/52500049_p0.jpg",
        "tel": "Jake Publisher",
        "address": "White House"
    }
}
```

#### 注册出版社

- 说明

> 注册出版社
>

- 请求URL

> 127.0.0.1:5000/publisher/publisher/?action=register

- 请求方式

> POST

- 请求参数

| 请求参数   | 必选 | 参数类型 | 说明                      |
| ---------- | ---- | -------- | ------------------------- |
| username   | 是   | String   | 出版社的用户名            |
| password   | 是   | String   | 密码                      |
| name       | 是   | String   | 出版社名称                |
| identifier | 是   | File     | 出版社的认证文件          |
| tel        | 是   | String   | 出版社的联系电话          |
| mail       | 是   | String   | 出版社的联系邮箱/投稿邮箱 |
| address    | 是   | String   | 出版社地址                |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "status": 200,
    "msg": "successfully saved publisher",
    "data": {
        "username": "Jake",
        "name": "Jake Publisher",
        "identifier": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/52500049_p0.jpg",
        "tel": "Jake Publisher",
        "address": "White House"
    }
}
```

#### 出版社登录

- 说明

> 出版社用户登录

- 请求URL

> 127.0.0.1:5000/publisher/publisher/?action=login

- 请求方式

> POST

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明           |
| -------- | ---- | -------- | -------------- |
| username | 是   | String   | 出版社的用户名 |
| password | 是   | String   | 密码           |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "status": 200,
    "msg": "successfully login",
    "token": "publisher722ad22a673a4ebf9cde1ee341529c20",
    "data": {
        "username": "Jake",
        "name": "Jake Publisher",
        "identifier": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/52500049_p0.jpg",
        "tel": "Jake Publisher",
        "address": "White House"
    }
}
```

#### 修改出版社信息

- 说明

> 出版社用户登录

- 请求URL

> 127.0.0.1:5000/publisher/publisher/?action=login

- 请求方式

> POST

- 请求参数

| 请求参数   | 必选 | 参数类型 | 说明             |
| ---------- | ---- | -------- | ---------------- |
| identifier | 否   | String   | 出版社的认证材料 |
| tel        | 否   | String   | 出版社的联系电话 |
| mail       | 否   | String   | 出版社的投稿邮箱 |
| address    | 否   | String   | 出版社地址       |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "successfully patched",
    "status": 200,
    "data": {
        "username": "Jake",
        "name": "Jake Publisher",
        "identifier": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/52500049_p0.jpg",
        "tel": "Jake Publisher",
        "address": "White House"
    }
}
```

#### 删除出版社

- 说明

> 出版社用户逻辑删除，即将该出版社用户的is_deleted 参数设为True
>
> 需要admin用户的登录

- 请求URL

> 127.0.0.1:5000/publisher/publisher/\<int:publisher_id>/

- 请求方式

> DELETE

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
    "status": 203,
    "msg": "publisher successfully deleted"
}
```

#### 获取复数出版社信息

- 说明

> 获取复数个出版社的信息

- 请求URL

> 127.0.0.1:5000/publisher/publisher/

- 请求方式

> DELETE

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                         |
| -------- | ---- | -------- | ---------------------------- |
| tag_id   | 否   | String   | 需要查找相应出版社的标签的ID |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "status": 200,
    "msg": "publishers of certain tag successfully got",
    "data": [
        {
            "username": "Jake",
            "name": "Jake Publisher",
            "identifier": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/52500049_p0.jpg",
            "tel": "Jake Publisher",
            "address": "White House"
        },
        {
            "username": "Jim",
            "name": "Jim Publisher",
            "identifier": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "tel": "Jim Publisher",
            "address": "White House"
        }
    ]
}
```

### 出版社-标签关系接口

#### 添加出版社-标签关系

- 说明

> 为本出版社增加一个需求标签
>
> 需要出版社用户登录

- 请求URL

> 127.0.0.1:5000/publisher/pub_tag_relation/

- 请求方式

> POST

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                   |
| -------- | ---- | -------- | ---------------------- |
| tag_id   | 是   | String   | 需要添加的标签的tag_id |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "publisher-tag relationship successfully created",
    "status": 200,
    "data": {
        "publisher_id": 1,
        "tag_id": 1
    }
}
```

#### 删除出版社-标签关系

- 说明

> 为本出版社删除一个需求标签
>
> 需要出版社用户登录

- 请求URL

> 127.0.0.1:5000/publisher/pub_tag_relation/

- 请求方式

> POST

- 请求参数

| 请求参数    | 必选 | 参数类型 | 说明                   |
| ----------- | ---- | -------- | ---------------------- |
| relation_id | 是   | String   | 需要添加的标签的tag_id |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "publisher-tag relationship successfully deleted",
    "status": 200
}
```

### 选题接口

#### 获取单个选题

- 说明

> 获取单个选题信息

- 请求URL

> 127.0.0.1:5000/publisher/topic/\<int:topic_id>

- 请求方式

> GET

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                 |
| -------- | ---- | -------- | -------------------- |
| topic_id | 是   | Integer  | 查询的选题的topic_id |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "seccessfully get",
    "status": 200,
    "data": {
        "name": "Jake-jake",
        "writer_id": 1,
        "publisher_id": 1,
        "is_approved": false,
        "is_completed": false
    }
}
```

#### 删除单个选题

- 说明

> 获取单个选题信息

- 请求URL

> 127.0.0.1:5000/publisher/topic/\<int:topic_id>

- 请求方式

> DELETE

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                 |
| -------- | ---- | -------- | -------------------- |
| topic_id | 是   | Integer  | 删除的选题的topic_id |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "topic successfully deleted",
    "status": 200
}
```

#### 添加选题

- 说明

> 获取单个选题信息

- 请求URL

> 127.0.0.1:5000/publisher/topics/

- 请求方式

> POST

- 请求参数

| 请求参数  | 必选 | 参数类型 | 说明                |
| --------- | ---- | -------- | ------------------- |
| writer_id | 是   | Integert | 投稿作者的writer_id |
| name      | 是   | String   | 选题的名字          |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "topic successfully created",
    "status": 201,
    "data": {
        "name": "Jake-jake",
        "writer_id": 1,
        "publisher_id": 1,
        "is_approved": false,
        "is_completed": false
    }
}
```

#### 获取多个选题

- 说明

> 获取多个选题信息
>
> 传递 writer_id 则查询作家申请过的所有选题信息
>
> 如果不传递 writer_id 则是查询所有选题信息

- 请求URL

> 127.0.0.1:5000/publisher/topics/

- 请求方式

> GET

- 请求参数

| 请求参数  | 必选 | 参数类型 | 说明            |
| --------- | ---- | -------- | --------------- |
| writer_id | 否   | Integert | 作者的writer_id |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "successfully get",
    "status": 200,
    "data": [
        {
            "name": "Jake-jake",
            "writer_id": 1,
            "publisher_id": 1,
            "is_approved": false
        },
        {
            "name": "Jake-jake3",
            "writer_id": 1,
            "publisher_id": 1,
            "is_approved": false
        },
        {
            "name": "Jake-jim4",
            "writer_id": 2,
            "publisher_id": 1,
            "is_approved": false
        }
    ]
}
```

#### 更改选题状态

- 说明

> 更改选题信息
>
> 只是在选题申请通过以后用于更改选题的状态。
>
> 

- 请求URL

> 127.0.0.1:5000/publisher/topic/\<int:topic_id>

- 请求方式

> PATCH

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                             |
| -------- | ---- | -------- | -------------------------------- |
| token    | 是   | String   | publisher的token，登录的时候获取 |
| topic_id | 是   | Integer  | 更改的topic_id                   |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "topic status successfully changed",
    "status": 200,
    "data": {
        "name": "Jake-jake",
        "writer_id": 1,
        "publisher_id": 1,
        "is_approved": true
    }
}
```

### 合同接口

#### 获取单个合同信息

- 说明

> 获取单个合同信息
>
> 需要publisher用户登录

- 请求URL

> 127.0.0.1:5000/publisher/contract/\<int:contract_id>

- 请求方式

> GET

- 请求参数

| 请求参数    | 必选 | 参数类型 | 说明                           |
| ----------- | ---- | -------- | ------------------------------ |
| token       | 是   | String   | publisher的token，在登陆时获取 |
| contract_id | 是   | Integer  | 查找的合同的ID                 |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "contract successfully got",
    "status": 200,
    "data": {
        "name": "jake-jake-contract",
        "publisher_id": 1,
        "writer_id": 1,
        "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
        "is_signed": false,
        "is_completed": false
    }
}
```

#### 创建合同

- 说明

> 创建新的合同
>
> 需要publisher用户登录

- 请求URL

> 127.0.0.1:5000/publisher/contracts/

- 请求方式

> POST

- 请求参数

| 请求参数      | 必选 | 参数类型 | 说明                        |
| ------------- | ---- | -------- | --------------------------- |
| token         | 是   | String   | 出版商的token，在登陆时获取 |
| name          | 是   | Integer  | 合同的名字                  |
| writer_id     | 是   | Integer  | 签订合同的作家ID            |
| contract_file | 是   | File     | 合同文件                    |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "contract successfully created",
    "status": 201,
    "data": {
        "name": "jake-jake-contract",
        "publisher_id": 1,
        "writer_id": 1,
        "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
        "is_signed": false,
        "is_completed": false
    }
}

```

#### 更改合同状态

- 说明

> 更改**自己的**合同状态
>
> 需要publisher用户登录

- 请求URL

> 127.0.0.1:5000/publisher/contract/\<int:contract_id>

- 请求方式

> PATCH

- 请求参数

| 请求参数      | 必选 | 参数类型 | 说明                        |
| ------------- | ---- | -------- | --------------------------- |
| token         | 是   | String   | 出版商的token，在登陆时获取 |
| name          | 是   | Integer  | 合同的名字                  |
| writer_id     | 是   | Integer  | 签订合同的作家ID            |
| contract_file | 是   | File     | 合同文件                    |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "contract already completed",
    "status": 200,
    "data": {
        "name": "jake-jake-contract",
        "publisher_id": 1,
        "writer_id": 1,
        "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
        "is_signed": true,
        "is_completed": true
    }
}
```

#### 获取出版社所有合同信息

- 说明

> 获取本出版社的所有合同信息
>
> 需要publisher用户登录

- 请求URL

> 127.0.0.1:5000/publisher/contracts/

- 请求方式

> GET

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                        |
| -------- | ---- | -------- | --------------------------- |
| token    | 是   | String   | 出版商的token，在登陆时获取 |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "contracts of certain publisher successfully got.",
    "status": 200,
    "data": [
        {
            "name": "jake-jake-contract",
            "publisher_id": 1,
            "writer_id": 1,
            "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "is_signed": false,
            "is_completed": false
        },
        {
            "name": "jake-jake-contract1",
            "publisher_id": 1,
            "writer_id": 1,
            "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "is_signed": false,
            "is_completed": false
        },
        {
            "name": "jake-jim-contract2",
            "publisher_id": 1,
            "writer_id": 2,
            "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "is_signed": false,
            "is_completed": false
        }
    ]
}
```

## 作家模块

### 作家接口

#### 获取单个作家信息

- 说明

> 获取单个作家信息

- 请求URL

> 127.0.0.1:5000/writer/writer/\<int:writer_id>/

- 请求方式

> GET

- 请求参数

| 请求参数  | 必选 | 参数类型 | 说明            |
| --------- | ---- | -------- | --------------- |
| writer_id | 是   | Integer  | 作家的writer_id |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "status": 200,
    "msg": "successfully get",
    "data": {
        "username": "Jake",
        "name": "Jake",
        "tel": "110",
        "mail": "jake@xxx.com"
    }
}
```

#### 作家注册

- 说明

> 作家用户注册

- 请求URL

> 127.0.0.1:5000/writer/writers/?action=register

- 请求方式

> POST

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明           |
| -------- | ---- | -------- | -------------- |
| username | 是   | String   | 出版社的用户名 |
| password | 是   | String   | 密码           |
| name     | 是   | String   | 用户姓名       |
| tel      | 是   | String   | 联系电话       |
| mail     | 是   | String   | 联系邮箱       |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "successfully post",
    "status": 201,
    "data": {
        "username": "Jake",
        "name": "Jake",
        "tel": "110",
        "mail": "jake@xxx.com"
    }
}
```

#### 作家登录

- 说明

> 作家用户登录

- 请求URL

> 127.0.0.1:5000/writer/writers/?action=login

- 请求方式

> POST

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                       |
| -------- | ---- | -------- | -------------------------- |
| ident    | 是   | String   | 用户名/注册手机号/注册邮箱 |
| password | 是   | String   | 密码                       |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "successfully login",
    "status": 200,
    "data": {
        "username": "Jake",
        "name": "Jake",
        "tel": "110",
        "mail": "jake@xxx.com"
    },
    "token": "writer4fb0f37849664d5ab16b3c1aa30d783b"
}
```

#### 修改作家信息

- 说明

> 修改作家信息
>
> 需作家用户登录，且只能修改自己的信息

- 请求URL

> 127.0.0.1:5000/writer/writers/

- 请求方式

> PATCH

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                        |
| -------- | ---- | -------- | --------------------------- |
| token    | 是   | String   | 作家用户的token，登陆时生成 |
| mail     | 否   | String   | 修改的邮箱                  |
| tel      | 否   | String   | 修改的手机号                |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "successfully patched",
    "status": 200,
    "data": {
        "username": "Jake",
        "name": "Jake",
        "tel": "110",
        "mail": "jake@shanbay.com"
    }
}
```

#### 删除作家

- 说明

> 作家用户逻辑删除
>
> 需要管理员用户权限

- 请求URL

> 127.0.0.1:5000/writer/writer/\<int:writer_id>/

- 请求方式

> DELETE

- 请求参数

| 请求参数  | 必选 | 参数类型 | 说明                          |
| --------- | ---- | -------- | ----------------------------- |
| token     | 是   | String   | 管理员用户的token，登陆时生成 |
| writer_id | 是   | Integer  | 需要删除的作家的writer_id     |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "status": 203,
    "msg": "writer successfully deleted"
}
```

#### 获取所有作家信息

- 说明

> 获取所有的作家的信息

- 请求URL

> 127.0.0.1:5000/writer/writers/

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
    "status": 200,
    "msg": "writer list fetched",
    "data": [
        {
            "username": "Jake",
            "name": "Jake",
            "tel": "110",
            "mail": "jake@xxx.com"
        },
        {
            "username": "jim",
            "name": "Jim",
            "tel": "911",
            "mail": "jim@xxx.com"
        },
        {
            "username": "yuchen",
            "name": "Yuchen",
            "tel": "120",
            "mail": "yuchen@xxx.com"
        }
    ]
}
```

### 合同接口

#### 获取单个合同信息

- 说明

> writer用户查看单个合同信息
>
> 需要writer用户登录

- 请求URL

> 127.0.0.1:5000/writer/contract/\<int:contract_id>

- 请求方式

> GET

- 请求参数

| 请求参数    | 必选 | 参数类型 | 说明                      |
| ----------- | ---- | -------- | ------------------------- |
| token       | 是   | String   | 作家的token，在登陆时获取 |
| contract_id | 是   | Interger | 查看的合同的ID            |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "contract successfully got.",
    "status": 200,
    "data": {
        "name": "jake-jake-contract",
        "publisher_id": 1,
        "writer_id": 1,
        "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
        "is_signed": true,
        "is_completed": false
    }
}
```

#### 修改合同状态

- 说明

> writer用户修改合同信息
>
> 只能在签字以后使用
>
> 需要writer用户登录

- 请求URL

> 127.0.0.1:5000/writer/contract/\<int:contract_id>

- 请求方式

> PATCH

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                      |
| -------- | ---- | -------- | ------------------------- |
| token    | 是   | String   | 作家的token，在登陆时获取 |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "contract successfully changed.",
    "status": 200,
    "data": {
        "name": "jake-jake-contract",
        "publisher_id": 1,
        "writer_id": 1,
        "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
        "is_signed": true,
        "is_completed": false
    }
}
```

#### 获取作家所有合同信息

- 说明

> writer用户的所有合同信息
>
> 需要writer用户登录

- 请求URL

> 127.0.0.1:5000/writer/contracts/

- 请求方式

> GET

- 请求参数

| 请求参数 | 必选 | 参数类型 | 说明                      |
| -------- | ---- | -------- | ------------------------- |
| token    | 是   | String   | 作家的token，在登陆时获取 |

- 返回字段

| 返回字段 | 字段类型 | 说明           |
| -------- | -------- | -------------- |
| status   | Integer  | http状态码     |
| msg      | String   | 返回的状态信息 |

- 返回示例

```json
{
    "msg": "contracts of certain writer successfully got.",
    "status": 200,
    "data": [
        {
            "name": "jake-jake-contract",
            "publisher_id": 1,
            "writer_id": 1,
            "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "is_signed": true,
            "is_completed": false
        },
        {
            "name": "jake-jake-contract1",
            "publisher_id": 1,
            "writer_id": 1,
            "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "is_signed": false,
            "is_completed": false
        },
        {
            "name": "jake-jake-contract2",
            "publisher_id": 1,
            "writer_id": 1,
            "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "is_signed": false,
            "is_completed": false
        },
        {
            "name": "jake-jake-contract3",
            "publisher_id": 1,
            "writer_id": 1,
            "contract_file": "D:\\Publisher-Writer-Communication-System\\App\\static/uploads/42655195_p0.jpg",
            "is_signed": false,
            "is_completed": false
        }
    ]
}
```

