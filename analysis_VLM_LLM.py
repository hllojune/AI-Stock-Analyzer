import base64
from ollama import generate

def analyze_image(image_path):
    with open(image_path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    response = generate(
        model="llava:latest",
        prompt="이 이미지를 분석해서 투자 관련 조언을 해줘. 그리고 한국어로 대답해줘",
        images=[image_base64]
    )
    return response['response']

def ask_question_with_analysis(analysis_result, user_question):
    prompt = f"""다음은 주식 차트 이미지를 분석한 결과입니다:

{analysis_result}

사용자가 이에 대해 다음과 같은 질문을 했습니다:
"{user_question}"

위 분석을 참고하여 질문에 대한 상세한 투자 조언을 전문가처럼 제공해 주세요."""

    response = generate(
        model="gemma3:4b",
        prompt=prompt
    )
    return response['response']

def main():
    image_path = "E:/image_ollama/candle_chart.png"
    analysis=None

    while True:
        if(analysis==None):
            print("차트를 분석 중입니다...")
            analysis = analyze_image(image_path)
            print("분석 결과:\n", analysis)
        user_question = input("\n---------------------------------------------------------------------"
        "                      \n종료 입력 시 프로그램 종료 " 
                              "\n재업로드 입력 시 이미지 재업로드 "
                              "\n투자 관련 질문을 입력해주세요: ")
        if(user_question=="종료"):
             break
        elif(user_question=="재업로드"):
            analysis=None
            image_path="E:/image_ollama/candle_chart.png"
        else:  
            answer = ask_question_with_analysis(analysis, user_question)
            print("AI의 응답:\n", answer)
    print("프로그램 종료")        
    
    
if __name__ == "__main__":
    main()
