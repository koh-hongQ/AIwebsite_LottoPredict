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
        {"role": "system", "content": 'you are a helpful assistant. 넌 사랑에 대해 잘 알려주는 ai야. '}
    ]




    # 대화에 사용자 메시지 추가
    messages.append({"role": "user", "content": "사랑이란 뭐라고 생각해? 10자 이내로 대답해."})

    # OpenAI API 호출
    response = client.chat.completions.create(
        model="gpt-4.1-nano",  # 모델 이름 수정
        messages=messages
    )
    bot_response = response.choices[0].message.content

            
            
            
            
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
        'a' : 8
        # 'map': fig
        # , ax
    }

    return render(request, 'main/index.html', context)
    # return bot_response

    