from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_open_jsonplaceholder_page():
    # 1. 크롬 옵션 설정
    options = webdriver.ChromeOptions()
    
    # [실습] 로컬에서 브라우저를 보고 싶으면 아래 한 줄을 주석 처리(#) 하세요.
    # 깃헙 액션(서버)에서 돌릴 때는 반드시 이 옵션이 켜져 있어야 합니다.
    options.add_argument('--headless') 
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # 2. 크롬 드라이버 실행
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # 3. JSONPlaceholder 사이트 접속
        driver.get("https://jsonplaceholder.typicode.com/")
        
        # 4. 브라우저 제목(Title) 확인
        page_title = driver.title
        print(f"\n[결과] 접속한 페이지 제목: {page_title}")

        # 5. 검증
        assert "JSONPlaceholder" in page_title

    finally:
        # 6. 테스트 종료 후 브라우저 닫기
        time.sleep(2)
        driver.quit()