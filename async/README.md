https://qiita.com/maueki/items/8f1e190681682ea11c98

async defはコルーチン関数定義


```
import asyncio

async def hello_world():
    print("Hello World!")

hello_world()
```

```
$ python3 hello.py
hello.py:6: RuntimeWarning: coroutine 'hello_world' was never awaited
  hello_world()
```

コルーチンがawaitされてないよ

https://docs.python.org/ja/3/reference/compound_stmts.html#coroutine-function-definition

Functions defined with async def syntax are always coroutine functions, even if they do not contain await or async keywords.

```
import asyncio

async def hello_world():
    print("Hello World!")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
```

```
$ python3 hello.py
Hello World!
```


次の例はどうか

```
import asyncio
import time

async def hello_world(n):
    time.sleep(1)
    print("{}: Hello World!".format(n))

async def call_hello_world1():
    print("call_hello_world1()")
    await hello_world(1)

async def call_hello_world2():
    print("call_hello_world2()")
    await hello_world(2)

loop = asyncio.get_event_loop()
loop.create_task(call_hello_world1())
loop.run_until_complete(call_hello_world2())
```


```
$ python3 hello.py
call_hello_world1()
# 1秒待つ
1: Hello World!
call_hello_world2()
# 1秒待つ
2: Hello World!
```

以下のようにはならない

```
call_hello_world1()
call_hello_world2()
# 1秒待つ
1: Hello World!
2: Hello World!
```

上記のように実行したければ以下のように書く


```
import asyncio

async def hello_world(n):
    await asyncio.sleep(1)
    print("{}: Hello World!".format(n))

async def call_hello_world1():
    print("call_hello_world1()")
    await hello_world(1)

async def call_hello_world2():
    print("call_hello_world2()")
    await hello_world(2)

loop = asyncio.get_event_loop()
loop.create_task(call_hello_world1())
loop.run_until_complete(call_hello_world2())
```
