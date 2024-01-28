def min_bags(N):
  # 5kg 봉지의 개수는 0이상, N 나누기 5 이하
  for five_kg_bags in range(N//5, -1, -1):
      # 5kg로 나뉘어지지 않고 남은 양 체크
      remaining_sugar = N - (five_kg_bags * 5)

      # 남은 양이 3kg로 나뉘어질 수 있는 지를 체크
      if remaining_sugar % 3 == 0:
          three_kg_bags = remaining_sugar // 3
          return five_kg_bags + three_kg_bags  # 5kg, 3kg 합쳐서 반환

  # 결국 3kg으로 나뉘어지지 않고 잔여량이 발생한다면
  return -1

kilos = int(input())
print(min_bags(kilos))