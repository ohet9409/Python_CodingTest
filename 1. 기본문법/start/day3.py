# 클래스
# 클래스 안에 함수에 인자 값이 없을 경우 에러 발생
class SoccerPalyer:

  def shoot(self):
    print("슛을 날립니다.");
    print("슈웃");

  def passTheBall(self):
    print("패스를 합니다.");

player = SoccerPalyer();
player.shoot();
player.passTheBall();

# 초기화 - 생성자
# 선언을 안해주면 기본적으로 선언되어 있음
class Soccer2:
  def __init__(self, heigth, weight):
    print("초기화");
    self.h = heigth;
    self.w = weight;

  def shoot(self):
    self.h = 999;
    print("슛이에요! :: ");

player2 = Soccer2(180,75);
print(player2.h);

player3 = Soccer2(180,75);
player3.shoot();
print(player3.h);

print(player2.h);


# player2.shoot(2);