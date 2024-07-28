# 하이아크 후학 양성 프로젝트 3팀

## 📌 간단한 규칙
- 매일 주어지는 문제셋을 풉니다 (8월에는 solved.ac class2 ~ class3 문제 위주)
- 푼 문제의 `소스코드`, `간단한 풀이` (못 풀었다면 어디서 막혔는지) 를 자정 전까지 PR로 올립니다.
- 다음날 자정 전까지 올라온 PR에 서로 어떻게 풀었는지 보고 댓글을 답니다. (저랑 똑같이 푸셨네요!, 이렇게 풀 수도 있군요, 이렇게 풀면 더 쉬워요 등)

## 🔍 자세한 방법
`CMD` 또는 터미널을 열고 아래 과정을 따라하시면 됩니다.   

**1. 이 레포지토리를 컴퓨터 내 원하는 위치에 `clone` 해주세요.**
  ```shell
  git clone https://github.com/kckc0608/hiarc-icpc-study.git
  ```

**2. 자신의 아이디(백준이나 깃허브)로 브랜치를 만들어주세요.**
    
    ```shell
    git checkout -b 아이디  (ex. git checkout -b kckc0608)
    ```

  ![image](https://github.com/user-attachments/assets/9a71a448-293d-4d62-9138-f1dd7c3127ef)

  `git branch` 명령어를 실행했을 때, 자신의 아이디에 *가 보이면 잘 된거에요.
  
**3. 백준 문제를 푼 뒤, 자신 아이디 이름의 폴더 안에 새로 문제 번호를 이름으로 한 파일을 만들어 제출한 소스코드를 작성합니다.**
  ```
  자신 이름의 폴더 안에 문제 번호를 이름으로 한 소스코드 파일을 만듭니다.
  만약 1000 번 문제를 파이썬으로 풀었다면 파일 이름은 '1000.py' 와 같이 작성하고, 그 안에 제출한 소스코드를 적습니다.
  ```

**4. 이제 커밋하고, 레포지토리에 push 합니다.**
  ```shell
  git add .                # . 도 같이 적어주세요!
  git commit -m "자유롭게 커밋 메세지 적기(1000 - A+B) 등"
  git push
  ```

![image](https://github.com/user-attachments/assets/b0d5218f-bfc6-48ec-bb00-4e6fe08982b9)

`git add .`, `git commit -m "commit message"` 명령어를 실행한 모습입니다.

![image](https://github.com/user-attachments/assets/0a3d9aea-713f-4cf8-bb06-25256dec5231)

`git push` 를 실행했을 때 처음에 이런 오류가 나올 수 있습니다.

![image](https://github.com/user-attachments/assets/81a487cc-62e1-4563-bdc8-544a71b142ff)

입력하라는대로 `git push --set-upstream origin 브랜치이름` 를 입력해줍니다.
다음에 push 할 때는 이 과정을 거칠 필요 없이 `git push` 만 하면 됩니다.


**5. PR을 양식에 맞게 작성합니다.**

![image](https://github.com/user-attachments/assets/23c6392e-0ea9-4213-ac87-848d2a4f72a0)

`git push` 를 한 이후에는 이렇게 PR(Pull Request)을 작성할 수 있는 UI가 보입니다.

![image](https://github.com/user-attachments/assets/4f7eed3f-c2d5-4bea-8fae-d32f7cdea990)

해당 UI를 클릭한 뒤, 이렇게 양식에 맞춰 PR을 작성해주세요.


**6. 서로 댓글을 남겨주고, 머지하면 끝납니다!**
