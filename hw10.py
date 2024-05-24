import pickle
import os

def input_score():
  scores = []
  i = 1
  while True:
    score = int(input(f'#{i}? '))
    if score < 0:
      break
    scores.append(score)
    i += 1
  return scores

def get_average(scores):
  return sum(scores)/len(scores)

def show_scores(scores):
  print('개인점수: ', end='')
  for score in scores:
    print(score, end=' ')

filename = 'data/score.bin'
# 사용자 정의 함수


def save(scores):
  with open(filename, 'wb') as file:
    pickle.dump(scores, file)

def load():
  with open(filename, 'rb') as file:
    scores = pickle.load(file)
    return scores
  
# 주 프로그램 부
if os.path.exists(filename):
  print('[파일 읽기]')
  print('\n[점수 출력]')
  s = load()
  show_scores(s)
  average = get_average(s)
  print(f'\n평균: {average}')

else:
    print('[점수 입력]')
    s = input_score()
    save(s)
    average = get_average(s)

    print('\n[점수 출력]')
    show_scores(s)
    print(f'\n평균: {average}')