import base64
from ollama import generate

def analyze_image(image_path):
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    response = generate(
        model="llava:latest",
        prompt="이 캔들차트를 보고 주요 기술적 지표를 분석해 투자 조언을 해줘. 한국어로 말해줘",
        images=[img_b64]
    )
    return response['response']

def main():
    image_path = input("분석할 차트 경로를 입력하세요: ")
    result = analyze_image(image_path)
    print("\n투자 조언:\n", result)
    

if __name__ == "__main__":
    main()
