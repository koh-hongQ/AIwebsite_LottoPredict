from django.shortcuts import render
from openai import OpenAI
import os
import requests
from dotenv import load_dotenv

def fff(request):
    # 파이썬에서 계산한 값이나 데이터
    title = "테스트 페이지"
    q  = "웹페이지에 ai 심기 테스트"



    load_dotenv()  # .env 파일의 변수들을 로드함

    api_key = os.getenv('OPENAI_API_KEY')
    # Store your OpenAI API key in an environment variable or secure file
    client = OpenAI(api_key=api_key)  #여기에 본인의 OpenAI API를 입력하시면 됩니다.



    
    messages = [
        {"role": "system", "content": 'you are a helpful assistant. 넌 과거 로또 데이터를 기반으로 6자리의 로또 번호를 예측하는 ai야. 답변은 6자리의 숫자 말고 절대 다른 출력이 있으면 안돼. '}
    ]




    # 대화에 사용자 메시지 추가
    messages.append({"role": "user", "content": "과거 로또 데이터를 기반으로 6자리의 로또 번호를 예측해. 답변은 6자리의 숫자 말고 절대 다른 출력이 있으면 안돼. 6자리의 숫자는 1234567890 이런 거 안돼. "})

    # OpenAI API 호출
    response = client.chat.completions.create(
        model="gpt-4.1-nano",  # 모델 이름 수정
        messages=messages
    )
    bot_response = response.choices[0].message.content


    



    messages2 = [
        {"role": "system", "content": 'you are a helpful assistant. 넌 절대 숫자를 출력하지 않아. 아까 출력한 숫자에 대한 근거를 알려주는 ai임. '}
    ]




    # 대화에 사용자 메시지 추가
    messages2.append({"role": "user", "content": "방금 출력한 6자리 로또 출력에 대한 근거만 한글로 말해. 답변은 50자 이내여야 해."})

    # OpenAI API 호출
    response2 = client.chat.completions.create(
        model="gpt-4.1-nano",  # 모델 이름 수정
        messages=messages2
    )
    bot_response2 = response2.choices[0].message.content

                        
            
            
            
        # #동대문구 지도
        # G = ox.graph_from_place('동대문구, 서울, 대한민국', network_type="drive", truncate_by_edge=True)

        # # 원점과 목적지 노드 찾기
        # orig_node = ox.nearest_nodes(G, float(user_input1_x), float(user_input1_y))  # 출발지 (경도, 위도)
        # dest_node = ox.nearest_nodes(G, float(user_input2_x), float(user_input2_y))   # 도착치 (경도, 위도)

        # # 최단 경로 계산
        # route = nx.shortest_path(G, orig_node, dest_node, weight='length')


    # 템플릿에 전달할 데이터
    context = {
        'title': title,
        'q': q,
        'bot_response': bot_response,
        'bot_response2': bot_response2,
        'a' : 8
        # 'map': fig
        # , ax
    }

    return render(request, 'main/index.html', context)
    # return bot_response

    