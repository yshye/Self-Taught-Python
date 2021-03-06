## JsonPath基本使用

[<< 返回目录](../README.MD)


> JsonPath是一种简单的方法来提取给定JSON文档的部分内容。 JsonPath有许多编程语言，如Javascript，Python和PHP，Java。

**jsonpath可以按照key对python字典进行批量数据提取**

### 1. 安装
```shell script
pip install jsonpath
```
### 2. 基本使用
#### 2.1 提取数据
```python
from jsonpath import jsonpath
ret = jsonpath(json_object,'jsonpath语法规定的字符串')
```

#### 2.2 jsonpath语法规则
##### 操作符
操作	|说明
---|---
`$`	|查询根元素。这将启动所有路径表达式。
`@`	|当前节点由过滤谓词处理。
`*`	|通配符，必要时可用任何地方的名称或数字。
`..`	|深层扫描。 必要时在任何地方可以使用名称。
`.<name>`	|点，表示子节点
`['<name>' (, '<name>')]`	|括号表示子项
`[<number> (, <number>)]`	|数组索引或索引
`[start:end]`	|数组切片操作
`[?(<expression>)]`	|过滤表达式。 表达式必须求值为一个布尔值。

##### 函数
函数可以在路径的尾部调用，函数的输出是路径表达式的输出，该函数的输出是由函数本身所决定的。

函数|	描述|	输出
---|---|---
min()	|提供数字数组的最小值	|Double
max()	|提供数字数组的最大值	|Double
avg()	|提供数字数组的平均值	|Double
stddev()	|提供数字数组的标准偏差值	|Double
length()	|提供数组的长度	|Integer

##### 滤器运算符
过滤器是用于筛选数组的逻辑表达式。一个典型的过滤器将是`[?(@.age > 18)]`，其中@表示正在处理的当前项目。 可以使用逻辑运算符&&和||创建更复杂的过滤器。 字符串文字必须用单引号或双引号括起来([?(@.color == 'blue')] 或者 [?(@.color == "blue")]).

操作符	|描述
---|---
`==`	|left等于right（注意1不等于'1'）
`!=`	|不等于
`<`	    |小于
`<=`	|小于等于
`>`	    |大于
`>=`	|大于等于
`=~`	|匹配正则表达式[?(@.name =~ /foo.*?/i)]
`in`	|左边存在于右边 [?(@.size in ['S', 'M'])]
`nin`   |左边不存在于右边
`size`	|（数组或字符串）长度
`empty`	|（数组或字符串）为空

#### 2.3 示例
```json
{
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}
```
JsonPath (点击链接测试)	|结果
---|---
[$.store.book[*].author](http://jsonpath.herokuapp.com/?path=$.store.book[*].author)	|获取json中store下book下的所有author值
[$..author](http://jsonpath.herokuapp.com/?path=$..author)	|获取所有json中所有author的值
[$.store.*](http://jsonpath.herokuapp.com/?path=$.store.*)	|所有的东西，书籍和自行车
[$.store..price](http://jsonpath.herokuapp.com/?path=$.store..price)	|获取json中store下所有price的值
[$..book[2]](http://jsonpath.herokuapp.com/?path=$..book[2])	|获取json中book数组的第3个值
[$..book[-2]](http://jsonpath.herokuapp.com/?path=$..book[-2])	|倒数的第二本书
[$..book[0,1]](http://jsonpath.herokuapp.com/?path=$..book[0,1])	|前两本书
[$..book[:2]](http://jsonpath.herokuapp.com/?path=$..book[:2])	|从索引0（包括）到索引2（排除）的所有图书
[$..book[1:2]](http://jsonpath.herokuapp.com/?path=$..book[1:2])	|从索引1（包括）到索引2（排除）的所有图书
[$..book[-2:]](http://jsonpath.herokuapp.com/?path=$..book[-2:])	|获取json中book数组的最后两个值
[$..book[2:]](http://jsonpath.herokuapp.com/?path=$..book[2:])	|获取json中book数组的第3个到最后一个的区间值
[$..book[?(@.isbn)]](http://jsonpath.herokuapp.com/?path=$..book[?(@.isbn)])	|获取json中book数组中包含isbn的所有值
[$.store.book[?(@.price < 10)]](http://jsonpath.herokuapp.com/?path=$.store.book[?(@.price%20%3C%2010)])	|获取json中book数组中price<10的所有值
[$..book[?(@.price <= $['expensive'])]](http://jsonpath.herokuapp.com/?path=$..book[?(@.price%20%3C=%20$[%27expensive%27])])	|获取json中book数组中price<=expensive的所有值
[$..book[?(@.author =~ /.*REES/i)]](http://jsonpath.herokuapp.com/?path=$..book[?(@.author%20=~%20/.*REES/i)])	|获取json中book数组中的作者以REES结尾的所有值（REES不区分大小写）
[$..*](http://jsonpath.herokuapp.com/?path=$..*)	|逐层列出json中的所有值，层级由外到内
[$..book.length()](http://jsonpath.herokuapp.com/?path=$..book.length())	|获取json中book数组的长度
