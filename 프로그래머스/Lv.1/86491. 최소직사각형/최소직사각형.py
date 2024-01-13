def solution(sizes):
    # 각 명함의 가로와 세로 길이 중 더 큰 길이를 가로로 설정
    max_width = max_height = 0
    for size in sizes:
        max_width = max(max_width, max(size))
        max_height = max(max_height, min(size))
    # 가장 큰 가로와 세로 길이를 곱해서 지갑 크기를 계산
    return max_width * max_height