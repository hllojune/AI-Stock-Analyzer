# simulation.py (가짜 모듈)

# 가짜 포트폴리오 데이터
mock_portfolio = {
    "cash": 1000000,
    "stocks": [
        {"ticker": "005930", "quantity": 10, "name": "삼성전자"},
        {"ticker": "035720", "quantity": 5, "name": "카카오"}
    ]
}

def get_user_portfolio():
    print("포트폴리오 조회 요청 받음... (테스트 중)")
    return mock_portfolio

def buy_stock(ticker, quantity):
    print(f"{ticker} 종목 {quantity}주 매수 요청 받음... (테스트 중)")
    mock_portfolio["cash"] -= 10000 * quantity # 가격은 10000원으로 가정
    return f"성공: {ticker} 종목 {quantity}주 매수 완료. (테스트 응답)"

def sell_stock(ticker, quantity):
    print(f"{ticker} 종목 {quantity}주 매도 요청 받음... (테스트 중)")
    mock_portfolio["cash"] += 10000 * quantity # 가격은 10000원으로 가정
    return f"성공: {ticker} 종목 {quantity}주 매도 완료. (테스트 응답)"