# 🚀 AI-Stock-Analyzer

AI-VLM을 활용하여 주식 차트 이미지를 분석하고, 가상 투자 시뮬레이션 기능을 제공하는 소프트웨어공학 팀 프로젝트입니다.

## Getting Started (프로젝트 시작하기)

이 섹션은 프로젝트를 자신의 로컬 컴퓨터에 설정하고 실행하는 방법을 안내합니다.

### 사전 준비물 (Prerequisites)

아래 프로그램들이 컴퓨터에 미리 설치되어 있어야 합니다.

-   [Git](https://git-scm.com/downloads)
-   [Python](https://www.python.org/downloads/) (버전 3.9 이상 권장)

### 설치 및 실행 순서 (Installation & Setup)

1.  **원격 저장소 복제 (Clone Repository)**

    터미널(Terminal) 또는 Git Bash를 열고, 원하는 디렉토리로 이동한 후 아래 명령어를 실행하여 프로젝트를 복제합니다.

    ```bash
    git clone [https://github.com/hllojune/AI-Stock-Analyzer.git](https://github.com/hllojune/AI-Stock-Analyzer.git)
    ```

2.  **프로젝트 폴더로 이동 (Navigate to Project Directory)**

    ```bash
    cd AI-Stock-Analyzer
    ```

3.  **가상 환경(Virtual Environment) 설정 및 활성화**

    프로젝트별 라이브러리 충돌을 방지하기 위해 가상 환경을 사용하는 것을 강력히 권장합니다.

    ```bash
    # 'venv'라는 이름의 가상 환경 생성
    python -m venv venv

    # 가상 환경 활성화 (macOS/Linux)
    source venv/bin/activate

    # 가상 환경 활성화 (Windows PowerShell 또는 CMD	)
    .\venv\Scripts\activate

    # 가상 환경 활성화 (Windows Git Bash)
    source venv/Scripts/activate

    ```

    > **Tip:** 가상 환경이 성공적으로 활성화되면 터미널 프롬프트 앞에 `(venv)`가 표시됩니다.

4.  **의존성 라이브러리 설치 (Install Dependencies)**

    프로젝트에 필요한 모든 라이브러리를 `requirements.txt` 파일을 통해 한번에 설치합니다.

    ```bash
    # 모든 팀원은 이 명령어만 실행하면 됩니다.
    pip install -r requirements.txt
    ```

5.  **프로젝트 실행 (Run the Project)**

    이제 백엔드 서버를 실행할 준비가 되었습니다.

    ```bash
    python app.py
    ```

    서버가 성공적으로 실행되면 터미널에 `Running on http://localhost:5000` 와 같은 메시지가 나타납니다. 이제 웹 브라우저에서 `http://localhost:3000` (프론트엔드 주소)으로 접속하여 개발을 진행할 수 있습니다.
