import requests
import pytest

class TestPostAPI:
    # 테스트 대상 URL 하드코딩
    base_url = "https://jsonplaceholder.typicode.com"

    def test_get_posts_status_check(self):
        """1. 전체 포스트 조회: 상태 코드 200 확인"""
        url = f"{self.base_url}/posts"
        # timeout은 실무에서 필수이므로 5초로 고정
        response = requests.get(url, timeout=5)
        
        assert response.status_code == 200, f"서버 응답 에러: {response.status_code}"

    def test_get_posts_data_type(self):
        """2. 데이터 형식 확인: 결과가 리스트(List) 형태인가?"""
        url = f"{self.base_url}/posts"
        response = requests.get(url)
        data = response.json()
        
        assert isinstance(data, list), "응답 데이터가 리스트 형식이 아닙니다."
        assert len(data) > 0, "조회된 데이터가 없습니다."

    def test_get_single_post_detail(self):
        """3. 단일 포스트 조회: 1번 글의 상세 데이터 검증"""
        post_id = 1
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.get(url)
        data = response.json()
        
        # 필드 값 및 존재 여부 검증
        assert data['id'] == post_id, f"요청 ID({post_id})와 응답 ID({data['id']}) 불일치"
        assert 'title' in data, "응답 데이터에 'title' 필드가 없습니다."
        assert 'body' in data, "응답 데이터에 'body' 필드가 없습니다."