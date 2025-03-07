# 1. 배경 & 목적
---
+ 주제명
  + LSTM 기반 리튬 가격 예측 모델링 및 중단기 공급위기 요소 분석
+ 배경
  + 핵심 광물의 특정국에 대한 높은 의존도로 인한 공급 불확실성 확대
  + 전기차 수요와 공급만 문제로 인한 리튬 가격의 높은 변동성 발생
+ 목표
  + 리튬 가격 예측 모델을 개발하여 공급망의 리스크를 최소화하고, 정부 및 민간 기업에 수급 안정화 정보 제공

# 2. 주최 & 기간 & 인원
---
+ 주최
  + 산업통상자원부
+ 기간
  + 2024.05-2024.07
+ 인원
  + 기획 1인, FE 1인, BE 1인(본인) 팀 프로젝트

# 3. 데이터 설명
---
1. 리튬 가격 예측 데이터 / 한국광해광업공단 / 공모전 제공자료
   + 2018-01-01 ~ 2026-10-01 (분기별 데이터)
2. 리튬 수급안정화지수 / 한국광해광업공단 / 공모전 제공자료
   + 2018-01 ~ 2022-03 (월별 데이터)
3. 리튬 시장위험지수 / 한국광해광업공단 / 공모전 제공자료
   + 2023-01-08 ~ 2023-12-22 (일별 데이터)
4. 국가별 광종 수출입 현황 / 관세청 / 공모전 제공자료
   + 2020 ~ 2021
5. 리튬 시장전망지표 / KOMIS 한국자원정보서비스
   + 2008-01 ~ 2024-04 (월별 데이터)
6. 리튬 기준가격 및 등락가 / KOMIS 한국자원정보서비스
   + 2007-12-07 ~ 2024-05-22 (일별 데이터)
7. 광물종합지수 / KOMIS 한국자원정보서비스
   + 2013-01-02 ~ 2024-05-28 (일별 데이터)
8. 달러환율 / 하나은행
   + 2003-09-24 ~ 2024-05-28 (일별 데이터)
9. 위안환율 / 하나은행
    + 2003-09-24 ~ 2024-05-28 (일별 데이터)
10. 구글 키워드 검색 / 구글트렌드
    + 2004-01 ~ 2024-05 (월별 데이터)
   
# 4. 담당 역할
---
+ 시계열 데이터 핸들링
  + 다양한 출처의 시계열 데이터를 단일 시간 단위로 통합 및 전처리
  + 리튬 가격의 변동 추이를 시각화하여 가시적으로 표현
  + 결측치, 이상치 처리 및 시계열 특성을 고려한 데이터 정규화 진행
  + 상관관계 분석을 통해 리튬 가격과 높은 연관성을 보이는 핵심 변수 도출 (달러 환율, 광물종합지수 등)
![Image](https://github.com/user-attachments/assets/b24fdbd7-cd83-4be3-8378-2715762391f9)
+ 파생 변수 생성
  + 광물변동지수, 경제지수 등 논문과 정책에 근거하여 파생 변수를 생성해 모델의 예측력 향상
+ LSTM 모델링
  + 시계열 데이터를 활용한 LSTM 모데링 진행 및 리튬 가격 예측
![Image](https://github.com/user-attachments/assets/1915158f-44b7-4711-8d01-4fe94440f116)
 
# 5. 결론
---
![Image](https://github.com/user-attachments/assets/d7134891-013a-412c-973d-5a52fe578c2b)
![Image](https://github.com/user-attachments/assets/1ba37331-aec0-4b50-b232-bee31ab06fb6)
+ 광물 가격 지표와 가격에 영향을 미치는 요인을 시각적으로 제공하는 플랫폼 개발
+ 특정 지표 변동 시 회원 등급에 따라 알림을 제공, 기업의 자원 배분 효율성을 높일 수 있도록 지원

# 6. 느낀점
---
예측 정확도를 높이기 위해 다양한 파생변수를 추가하고 LSTM 아키텍처를 개선하는 과정을 통해 도메인 지식의 중요성과 딥러닝 지식은 높은 시너지를 발휘한다는 것을 배웠습니다. 또한 실제 데이터의 복잡성을 다루는 경험과 팀원들과의 협업의 중요성을 배웠습니다. 분석 결과와 예측 모델을 활용하여 실제 비즈니스 문제 해결을 위한 종합적 접근 방식의 필요성을 깊이 이해하였습니다.






