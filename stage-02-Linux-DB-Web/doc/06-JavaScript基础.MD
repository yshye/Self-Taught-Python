## JavaScript基础

[<< 返回目录](../README.MD)

`JavaScript`是运行在浏览器端的脚步语言, 是由浏览器解释执行的, 简称`js`, 它能够让网页和用户有交互功能, 增加良好的用户体验效果。

前端开发三大块 
1. `HTML：`负责网页结构 
2. `CSS：`负责网页样式 
3. `JavaScript：`负责网页行为

### 1 使用方式
#### 1.1 行内式（主要用于事件）
```html
<input type="button" name="" onclick="alert('ok！');">
```
#### 1.2 内嵌式
```html
<script type="text/javascript">        
    alert('ok！');
</script>
```
#### 1.3 外链式
```html
<script type="text/javascript" src="js/index.js"></script>
```
### 2. 变量和数据类型  
#### 2.1 定义变量
> JavaScript 是一种弱类型语言，也就是说不需要指定变量的类型，JavaScript的变量类型由它的值来决定， 定义变量需要用关键字 'var', 一条JavaScript语句应该以“;”结尾

定义变量的语法格式:
```text
var 变量名 = 值;
var iNum = 123;
var sTr = 'asd';
//同时定义多个变量可以用","隔开，公用一个‘var’关键字
var iNum = 45,sTr='qwe',sCount='68';
```
#### 2.2 JavaScript注释
JavaScript的注释分为单行注释(//注释内容)和多行注释(/多行注释/)
```html
<script type="text/javascript">    
// 单行注释
var iNum = 123;
/*  
    多行注释
    1、...
    2、...
*/
var sTr = 'abc123';
</script>
```
#### 2.3 数据类型
> js中有六种数据类型，包括五种基本数据类型和一种复杂数据类型(object)。

##### 5种基本数据类型：
1. number 数字类型
2. string 字符串类型
3. boolean 布尔类型 true 或 false
4. undefined undefined类型，变量声明未初始化，它的值就是undefined
5. null null类型，表示空对象，如果定义的变量将来准备保存对象，可以将变量初始化为null,在页面上获取不到对象，返回的值就是null

##### 1种复合类型：
1、object 后面学习的数组、函数和JavaScript对象都属于复合类型
```javascript
//1.1 数字 number
var iOne = 10.1;

//1.2 字符串 string
var sStr = '1234';

//1.3 布尔 boolean; 
var bIsTrue = false;

//1.4 未定义 undefined
var unData;

//1.5 null 表示空对象
var nullData = null;

//1.6 object 表示对象类型
var oObj = {
   name:"隔壁老王",
   age:88
}
// 获取变量的类型
var type = typeof(oObj);
alert(type);
// 获取对象的name属性
alert(oObj.name);
```
#### 2.4 变量命名规范
1. 区分大小写
2. 第一个字符必须是字母、下划线（_）或者美元符号（$）
3. 其他字符可以是字母、下划线、美元符或数字
#### 2.5 匈牙利命名风格
- 对象o `Object` 比如：oDiv
- 数组a `Array` 比如：aItems
- 字符串s `String` 比如：sUserName
- 整数i `Integer` 比如：iItemCount
- 布尔值b `Boolean` 比如：bIsComplete
- 浮点数f `Float` 比如：fPrice
- 函数fn `Function` 比如：fnHandler

### 3. 函数
#### 3.1 函数定义
函数就是可以重复使用的代码块, 使用关键字 function 定义函数。
```html
<script type="text/javascript">
    // 函数定义
    function fnAlert(){
        alert('hello!');
    }
</script>
```

#### 3.2 函数调用
函数调用就是函数名加小括号，比如:函数名(参数[参数可选])
```html
<script type="text/javascript">
    // 函数定义
    function fnAlert(){
        alert('hello!');
    }
    // 函数调用
    fnAlert();
</script>
```

#### 3.3 定义有参数有返回值的函数
定义函数时，函数如果有参数，参数放到小括号里面，函数如果有返回值，返回值通过 return 关键字来返回
```html
<script type="text/javascript">
function fnAdd(iNum01,iNum02){
    var iRs = iNum01 + iNum02;
    return iRs;
    alert('here!');
}

var iCount = fnAdd(3,4);
alert(iCount);  //弹出7
</script>
```

##### 函数中`return`关键字的作用
1. 返回函数中的值
2. 执行完return函数执行结束

### 4. 变量作用域
#### 4.1 局部变量
局部变量就是在函数内使用的变量，只能在函数内部使用。
```html
<script type="text/javascript">
    function myalert()
    {
        // 定义局部变量
        var b = 23;
        alert(b);
    }
    myalert(); // 弹出23
    alert(b);  // 函数外使用出错
</script>
```

#### 4.2 全局变量
全局变量就是在函数外定义的变量，可以在不同函数内使用。
```html
<script type="text/javascript">
    // 定义全局变量
    var a = 12;
    function myalert()
    {
        // 修改全局变量
        a++;
    }
    myalert();
    alert(a);  // 弹出13    
</script>
```

### 5. 条件语句
#### 5.1 基本语法
- `if` 语句: 只有当指定条件为 `true` 时，使用该语句来执行代码
- `if...else` 语句 : 当条件为 `true` 时执行代码，当条件为 `false` 时执行其他代码
- `if...else if....else` 语句 : 使用该语句来判断多条件，执行条件成立的语句

#### 5.2 比较运算符

比较运算符|描述
---|---
==	|等于	
===	|全等(值和类型)	
\!=	|不等于	
\>	|大于	
\<	|小于	
\>=	|大于或等于	
\<=	|小于或等于	

#### 5.3 逻辑运算符
比较运算符|描述
---|---
&&	|and	
||	|or	
!	|not	

### 6. 获取标签元素
> 可以使用内置对象 `document` 上的 `getElementById` 方法来获取页面上设置了`id`属性的标签元素，获取到的是一个`html`对象，然后将它赋值给一个变量，比如：

```html
<script type="text/javascript">
    var oDiv = document.getElementById('div1');
    alert(oDiv);
</script>
<div id="div1">这是一个div元素</div>
```
- 说明: 上面的代码，如果把`javascript`写在元素的上面，就会出错，因为页面上从上往下加载执行的，`javascript`去页面上获取元素`div1`的时候，元素`div1`还没有加载。

**解决方法有两种** 
- 第一种方法：将`javascript`放到页面最下边
```html
<div id="div1">这是一个div元素</div>

<script type="text/javascript">
    var oDiv = document.getElementById('div1');
    alert(oDiv);
</script>
```
- 第二种方法：设置页面加载完成执行的函数，在执行函数里面获取标签元素。
```html
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
    }
</script>
```
说明: `onload`是页面所有元素加载完成的事件，给`onload`设置函数时，当事件触发就会执行设置的函数。

### 7. 操作标签元素属性
#### 7.1 属性的操作
首先获取的页面标签元素，然后就可以对页面标签元素的属性进行操作，属性的操作包括:
- 属性的读取
- 属性的设置

属性名在js中的写法
- html的属性和js里面属性大多数写法一样，但是“`class`” 属性写成 “`className`”
- “`style`” 属性里面的属性，有横杠的改成驼峰式，比如：“`font-size`”，改成”`style.fontSize`”
```html
<style>
    .sty01{
        font-size:20px;
        color:red;
    }
    .sty02{
        font-size:30px;
        color:pink;
        text-decoration:none;
    }

</style>

<script type="text/javascript">

    window.onload = function(){
        var oInput = document.getElementById('input1');
        var oA = document.getElementById('link1');
        // 读取属性值
        var sValue = oInput.value;
        var sType = oInput.type;
        var sName = oInput.name;
        var sLinks = oA.href;

        // 操作class属性,需要写成“className”
        oA.className = 'sty02';

        // 写(设置)属性
        oA.style.color = 'red';
        oA.style.fontSize = sValue;
    }

</script>

<input type="text" name="setsize" id="input1" value="20px">
<a href="#" id="link01" class="sty01">这是一个链接</a>
```
#### 7.2 innerHTML
innerHTML可以读取或者设置标签包裹的内容

```html
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
        //读取
        var sTxt = oDiv.innerHTML;
        alert(sTxt);
        //写入
        oDiv.innerHTML = '<a href="http://www.itcast.cn">传智播客<a/>';
    }
</script>


<div id="div1">这是一个div元素</div>
```

### 8. 数组
#### 8.1 数组的介绍
数组就是一组数据的集合，`javascript` 中，数组里面的数据可以是不同类型的数据，好比 `python` 里面的列表。

#### 8.2 数组的定义
```javascript
// 实例化对象方式创建
var aList = new Array(1,2,3);

// 字面量方式创建，推荐使用
var aList2 = [1,2,3,'asd'];
```
#### 8.3 多维数组
多维数组指的是数组的成员也是数组，把这样的数组叫做多维数组。
```js
var aList = [[1,2,3],['a','b','c']];
```

#### 8.4 数组的操作
##### 1、 获取数组的长度
```javascript
var aList = [1,2,3,4];
alert(aList.length); // 弹出4
```

##### 2、 根据下标取值
```js
var aList = [1,2,3,4];
alert(aList[0]); // 弹出1
```

##### 3、 从数组最后添加和删除数据
```javascript
var aList = [1,2,3,4];
aList.push(5);
alert(aList); //弹出1,2,3,4,5
aList.pop();
alert(aList); // 弹出1,2,3,4
```

##### 4、根据下标添加和删除元素
```js
arr.splice(start,num,element1,.....,elementN)
```

参数解析：
- `start`：必需，开始删除的索引。
- `num`：可选，删除数组元素的个数。
- `elementN`：可选，在start索引位置要插入的新元素。

此方法会删除从start索引开始的num个元素，并将elementN参数插入到start索引位置。
```js
var colors = ["red", "green", "blue"];
colors.splice(0,1);  //删除第一项
alert(colors);  //green,blue

colors.splice(1, 0, "yellow", "orange");  //从第一个索引位置插入两项数据
alert(colors);  //green,yellow,organge,blue

colors.splice(1, 1, "red", "purple");  //删除一项，插入两项数据
alert(colors);  //green,red,purple,orange,blue
```

### 9. 循环
循环语句就是让一部分代码重复执行，javascript中常用的循环语句有:
- for
- while
- do-while

#### 9.1 for循环
```js
var array = [1, 4, 5];

for(var index = 0; index < array.length; index++){
    result = array[index];
    alert(result);
}
```
#### 9.3 while循环
```js
var array = [1, 4, 5];        
var index = 0;

while (index < array.length) {
    result = array[index];
    alert(result);
    index++;
}
```

说明: 当条件成立的时候, while语句会循环执行

#### 9.4 do-while循环
```js
var array = [1, 4, 5];
var index = 0;

do {
    result = array[index];
    alert(result);
    index++;
} while (index < array.length);
```
说明: 当条件不成立的时候do语句也会执行一次

### 10. 字符串拼接
字符串拼接使用: "+" 运算符
```javascript
var iNum1 = 10;
var fNum2 = 11.1;
var sStr = 'abc';

result = iNum1 + fNum2;
alert(result); // 弹出21.1

result = fNum2 + sStr;
alert(result); // 弹出11.1abc
```
`数字和字符串拼接会自动进行类型转换(隐士类型转换)，把数字类型转成字符串类型进行拼接`

### 11. 定时器
> 定时器就是在一段特定的时间后执行某段程序代码。

#### 11.1 定时器的使用：
js 定时器有两种创建方式：
```text
setTimeout(func[, delay, param1, param2, ...]) ：以指定的时间间隔（以毫秒计）调用一次函数的定时器
setInterval(func[, delay, param1, param2, ...]) ：以指定的时间间隔（以毫秒计）重复调用一个函数的定时器
```
###### setTimeout
```text
第一个参数 func , 表示定时器要执行的函数名
第二个参数 delay, 表示时间间隔，默认是0，单位是毫秒
第三个参数 param1, 表示定时器执行函数的第一个参数，一次类推传入多个执行函数对应的参数。
```
```html
<script> 
    function hello(){ 
        alert('hello'); 
    } 

    // 执行一次函数的定时器
    setTimeout(hello, 500);
</script>
```

###### setInterval
```text
第一个参数 func , 表示定时器要执行的函数名
第二个参数 delay, 表示时间间隔，默认是0，单位是毫秒
第三个参数 param1, 表示定时器执行函数的第一个参数，一次类推传入多个执行函数对应的参数。
``` 
```html
<script> 
    function hello(){ 
        alert('hello'); 
    } 
    // 重复执行函数的定时器
    setInterval(hello, 1000);
</script>
```

#### 11.2 清除定时器
- js 清除定时器分别是:
```text
clearTimeout(timeoutID) 清除只执行一次的定时器(setTimeout函数)
clearInterval(timeoutID) 清除反复执行的定时器(setInterval函数)
```

###### clearTimeout

timeoutID 为调用 setTimeout 函数时所获得的返回值，使用该返回标识符作为参数，可以取消该 setTimeout 所设定的定时执行操作。
```html
<script>
    function hello(){
        alert('hello');
        // 清除只执行一次的定时器
        clearTimeout(t1)
    }
    // 执行一次函数的定时器
    t1 = setTimeout(hello, 500);
</script>
```
###### clearInterval

timeoutID 为调用 setInterval 函数时所获得的返回值，使用该返回标识符作为参数，可以取消该 setInterval 所设定的定时执行操作。
```html
<script> 
    function hello(){ 
        alert('hello'); 
    } 
    // 重复执行函数的定时器
    var t1 = setInterval(hello, 1000);

    function stop(){
        // 清除反复执行的定时器
        clearInterval(t1); 
    }  

</script> 

<input type="button" value="停止" onclick="stop();">
```












