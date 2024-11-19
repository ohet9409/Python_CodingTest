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

# 상속
class Human:
  def __init__(self, weight, height):
    self.w = weight;
    self.h = height;

  def walk(self):
    print("걷습니다.");

h1 = Human(60,120);
h1.walk();

class Athelte(Human):
  def __init__(self, weight, height, fat_rate=10):
    super().__init__(weight, height)
    self.fat_rate = fat_rate

  def workout(self):
    print("운동을 합니다.");

h2 = Athelte(50,100);
h2.walk();

h3 = Athelte(50,100,11);
h3.workout();

class SoccerPalyer(Athelte):
  # 덮어씌우기
  def workout(self):
    print("축구를 한다.");

h4 = SoccerPalyer(50,180,30);
h4.workout();

# 클래스 관점에서 바라보는 파이썬 자료형
a = [1,2,3];
a.append(4);
print(a);

c = {"c" : 123, "d": "aaa"};
print(c.keys());

class SP:
  def __init__(self, weight):
    self.weight = weight;
  
a = SP(10);
print(a.weight);

a1 = SP([100,10,90]);
print(a1.weight)

class SC:
  def __init__(self, numY):
    self.numY = numY

class Team:
  def __init__(self, coach, playerList):
    self.coach = coach
    self.playerList = playerList

pl1 = SP(70);
pl2 = SP(80)

coach = SC(10);

team = Team(coach=coach, playerList=[pl1,pl2]);
print(team.coach.numY)
print(team.playerList[0].weight)