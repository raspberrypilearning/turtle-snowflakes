## 눈송이를 그리기 위해 함수 사용하기

여러분의 평행사변형 눈송이는 멋지지만 눈송이처럼 보이지는 않습니다. 고쳐봅시다!

이를 고치려면, 거북이를 창의 가운데로 이동시켜야 합니다. `penup()` 과 `pendown()` 코드는 우리가 실제로 그림을 그릴 때 펜을 집어 들고 시작할 곳으로 움직이는 것처럼 선을 그리지 않은 채로 거북이를 움직일 수 있게 합니다.

- `colours` 리스트 아래에 다음 코드를 입력하세요:
    
    ```python
    elsa.penup()
    elsa.forward(90)
    elsa.left(45)
    elsa.pendown()
    ```

눈송이의 한 부분을 그려서 **함수** 에 넣는 코드를 작성합시다! 그런 다음 단순히 계속 반복해서 완전한 눈송이를 만들 수 있습니다.

![부분](images/branch.PNG)

- 다음을 입력해 `branch`라는 함수를 정의하세요:
    
    ```python
    def branch():
    ```

- 평행사변형 눈송이 반복문의 코드를 지우세요. 다음의 코드를 들여쓰기해서 `branch` 함수에 추가하세요:
    
    ```python
    for i in range(3):
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)
    ```
    
    **참고**: 들여쓰기가 중요하다는 사실을 기억하세요. 들여쓰기가 전부 올바르게 되어 있는지 확인하세요. 그렇지 않으면 코드가 제대로 작동하지 않을 것입니다!

- `branch` 함수를 8번 **호출**(실행)해서 코드의 마지막 부분을 작성하세요. 마지막 눈송이에 반복문을 다시 적용할 수 있습니다.
    
    ```python
    for i in range(8):
      branch()
      elsa.left(45)
    ```

- `elsa.color(random.choice(colours))`의 앞에 `#`을 입력해서 코드를 **주석**으로 바꾸세요. 이것은 컴퓨터가 그 코드가 있는 줄을 무시한다는 것을 의미합니다. 해당 줄을 삭제할 수도 있지만 나중에 눈송이에 색을 추가하는 데 사용할 수도 있습니다.

- 코드를 저장하고 실행하면 눈 앞에 눈송이가 나타납니다!

![](images/snowflake2.png)