## 반복문을 사용해 모양 만들기

정사각형을 만들려면 코드 몇 줄을 반복해야 합니다. 하지만 이것이 가장 효율적인 방법은 아닙니다. 코드를 여러 줄 입력하는 대신 반복문을 사용하는 것이 더 쉽습니다.

사각형을 만들기 위해 이런 코드 대신:

```python
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
```

아래와 같이 바꿀 수 있습니다. 위에 4번씩 들어간 코드를 아래와 같이 효율적으로 **반복**할 수 있습니다.

```python
for i in range(4):
  elsa.forward(100)
  elsa.right(90)
```

시도해보고 코드를 저장한 후 실행하면 어떻게 되는지 확인합니다.

![](images/turtle-loop.png)