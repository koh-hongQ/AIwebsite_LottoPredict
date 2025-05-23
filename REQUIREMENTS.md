김준엽 조사 내용 :

(https://tykimos.github.io/2020/01/25/keras_lstm_lotto_v895/)<br>
python deep learnning을 이용한 로또 당첨 프로그램으로<br>
로또가 독립시행(매 시행마다 특정 결과가 나올 확률이 변하지 않는 것)이 아니다라는 가설을 시작으로<br>
전제1. 로또 번호는 과거부터 미래까지 이미 정해져 있다.<br>
전제2. 지금까지의 로또 번호를 딥러닝에게 외우게 하면 딥러닝이 어떠한 원리를 깨달아서 다음회차의  로또 번호를 예측할 수 있을것이다.
를 가정합니다.
<br><br>
동행복권 사이트에 올라와 있는 지난 회차 정보를 웹 크롤링으로 파일로 가져와 딥러닝을 시킵니다.<br>
1등 예측뿐만 아니라 다른 등수의 번호를 예측하는것 또한 의미가 있기에 메트릭 추가를 이전회차와 현재회차를 비교분석하는 프로그램을 새롭게 만들어 실행.<br>
<br>
https://www.youtube.com/watch?v=3G3zExNItj0&t=1379s
<br>(youtube: 조코딩/ title:딥러닝이 예측한 로또 번호는 당첨이 잘될까?)
<br>위 유튜브 영상은 유튜버가 (https://tykimos.github.io/2020/01/25/keras_lstm_lotto_v895/) 위 사이트의 내용을 바탕으로 코딩을하여 만든 로또 예측 프로그램에 대한 영상입니다.
 
=======

고홍규 조사 내용 : <br>
관련 웹사이트 : https://ai-lottosolutions.com/ <br>
관련 오픈소스 : https://github.com/kimwooseob-pixel/lottosolutions <br>
UI가 깔끔하고 참고해도 좋을 것 같습니다. <br>

========

유승열 조사 내용 : <br>
관련 website<br>
https://tykimos.github.io/2020/01/25/keras_lstm_lotto_v895/<br>
https://github.com/youtube-jocoding/lotto-deeplearning?tab=readme-ov-file <br>
https://animalface.site/lotto <br>
<br>

========

김성은 조사내용

링크: https://philarchive.org/archive/ALGPAO
Kaggle에서 수집한 과거 로또 데이터를 활용하여 딥러닝 및 시계열 분석 기법을 통해 로또 번호를 예측하는 모델을 개발하였다. 연구 결과는 AI가 로또 예측에 일정한 가능성을 보이지만 무작위성의 한계를 극복하지 못했다는 것을 강조한다.
링크: https://patents.google.com/patent/KR102306385B1/ko
이 특허는 과거 회차별 당첨번호를 포함하여 grouping한 후 인공지능을 학습시켜 각 케이스 별로 복수개의 로또 복권 번호를 조함하여 추출한 후 당첨 번호와 비교하여 높은 당첨 확률을 갖는 케이스를 선별한다.


