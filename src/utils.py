"""
Team Utility Functions
각 팀원이 하나 이상의 유틸 함수를 추가합니다.
"""


def hello(name: str) -> str:
    """팀원 이름을 받아 인사말을 반환합니다."""
    return f"안녕하세요, {name}님! Git Collaboration 프로젝트에 오신 것을 환영합니다."


if __name__ == "__main__":
    print(hello("팀원"))
