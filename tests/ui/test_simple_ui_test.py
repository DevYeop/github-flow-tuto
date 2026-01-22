from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_open_jsonplaceholder_page():
    # 1. 크롬 드라이버 설정 (브라우저 창이 뜨도록 함)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # 2. JSONPlaceholder 사이트 접속
        driver.get("https://jsonplaceholder.typicode.com/")
        
        # 3. 브라우저 제목(Title) 확인 (정상 접속 여부 검증)
        # 페이지 상단 탭에 적힌 글자를 가져옵니다.
        page_title = driver.title
        print(f"\n[결과] 접속한 페이지 제목: {page_title}")

        # 4. 검증: 제목에 'JSONPlaceholder'라는 단어가 포함되어 있는가?
        assert "JSONPlaceholder" in page_title

    finally:
        # 5. 테스트 종료 후 브라우저 닫기
        time.sleep(2)  # 눈으로 확인하기 위해 2초 대기
        driver.quit()