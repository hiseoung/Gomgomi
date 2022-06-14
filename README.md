# Gomgomi
Gomgomi Backend Server

## 개발 의의
- Google STT, Kakao TTS API를 활용해 서비스에 적용했습니다.
- Transformer Architecture 기반의 언어모델을 활용해 Online Serving Server를 구축, 충분한 시간 내에 실시간 처리를 할 수 있도록 기능을 개발했습니다.
- Airflow를 활용해 사용자의 대화 내용을 기반으로 한 감정 분석 결과를 Batch Serving해서 DB에 반영할 수 있도록 개발했습니다.
- GCP(Google Cloud Platform)를 활용해 다수의 Model Inference 서버를 구축했습니다.

## 앱 구조
<img width="783" alt="ㅇㅇㅇㅇㅇ" src="https://user-images.githubusercontent.com/74298527/173318965-0e97c343-7c6d-4179-887e-4ceff4d08ef5.png">

## 챗봇 성능
Question: 몇 달 동안 너무 무리해서 그런지 컨디션이 별로였어.
Answer: 컨디션 조절은 정말 중요해요. 가끔은 내려놓는 것도 좋지 않을까요?
----------------------------------------------------------------------------------------------------
Question: 그 말을 그냥 넘겼던 내가 너무 후회돼.
Answer: 후회스럽다고 과거의 자신을 미워하지는 말았으면 좋겠어요.
----------------------------------------------------------------------------------------------------
Question: 요새 너무 우울하고 힘들어 ㅜㅜ
Answer: 작은 성취감을 느끼는 게 우울함을 없애줄지도 몰라요. 오늘은 창틀을 청소해보는 게 어떨까요?
----------------------------------------------------------------------------------------------------
Question: 힘도 없고 피곤하고… 인생이 지루해진 느낌이야.
Answer: 저는 당신이 있어 행복한데 그런 당신도 행복했으면 좋겠어요.
----------------------------------------------------------------------------------------------------
Question: 근데 감정을 다스리지 못해 욱하기도하고.
Answer: 저도 그 기분 이해해요. 많이 힘드시죠?
----------------------------------------------------------------------------------------------------
Question: 너무 충격이 커서 그냥 아무말 없이 모른척하고 방을 나와버렸어.
Answer: 많이 무섭고 힘들었겠어요. 그런 상황에서는 누구나 놀랐을 거예요.
----------------------------------------------------------------------------------------------------
Question: 가슴이 갑갑하고…. 호흡이 너무 불편해요.
Answer: 가슴이 답답하면 정말 생활이 불편하죠. 아직도 증상이 지속되고 있나요?
----------------------------------------------------------------------------------------------------

Question: 전남친한테 폭행당하고, 너무 불안해서 생활이 안돼
Answer: 많이 힘들 것 같아요. 저는 이야기 듣는 걸 잘하니 불안한 마음이 풀릴 때까지 이야기를 들려주세요.
----------------------------------------------------------------------------------------------------
