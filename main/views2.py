from django.shortcuts import render
from openai import OpenAI
import os
import requests
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate

def lotto_predict(request):
        # 파이썬에서 계산한 값이나 데이터
    title = "테스트 페이지"
    q  = "웹페이지에 ai 심기 테스트"



    load_dotenv()  # .env 파일의 변수들을 로드함

    api_key = os.getenv('OPENAI_API_KEY')
    # Store your OpenAI API key in an environment variable or secure file
    client = OpenAI(api_key=api_key)  #여기에 본인의 OpenAI API를 입력하시면 됩니다.

    lottodata= " 7,9,24,40,42,44 / 3,6,7,11,12,17 / 3,13,28,34,38,42 / 5,12,24,26,39,42 / 9,21,24,30,33,37 / 8,23,31,35,39,40 / 14,23,25,27,29,42 / 6,7,27,29,38,45 / 17,18,23,25,38,39 / 2,13,15,16,33,43 "
    # messages = [
    #     ("system", 'you are a helpful assistant. 넌 과거 로또 데이터를 기반으로 6개의 로또 번호를 예측하는 ai야. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45사이의 수야.'),


    #     ("human",  "{lottodata}를 기반으로 6개의 로또 번호를 예측해. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45 사이의 수야. 3,13,28,34,38,42 이런 예시처럼 출력하되 숫자마다 콤마로 구분해."),
    #     ]
    # prompt_template = ChatPromptTemplate.from_messages(messages)
    # prompt = prompt_template.invoke({"lottodata": lottodata})
    # #디폴트로 model변수의 AI 모델을 쓰는거임?
    
    # # llm.invoke(prompt) 

    # # OpenAI API 호출
    # response = client.chat.completions.create(
    #     model="gpt-4.1-nano",  # 모델 이름 수정
    #     messages=prompt
    # )
    # bot_response = response.choices[0].message.content
    messages = [
        {"role": "system", "content": 'you are a helpful assistant. 넌 과거 로또 데이터를 기반으로 6개의 로또 번호를 예측하는 ai야. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45사이의 수야.'},
        {"role": "user", "content": f"{lottodata}를 기반으로 6개의 로또 번호를 예측해. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45 사이의 수야. 3,13,28,34,38,42 이런 예시처럼 출력하되 숫자마다 콤마로 구분해."}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages
    )
    bot_response = response.choices[0].message.content
        
# ====================================
    



    messages2 = [
        {"role": "system", "content": 'you are a helpful assistant. 넌 절대 숫자를 출력하지 않아. 아까 출력한 숫자에 대한 근거를 영어로 알려주는 ai임. '}
    ]




    # 대화에 사용자 메시지 추가
    messages2.append({"role": "user", "content": "방금 출력한 6자리 로또 출력에 대한 근거만 영어로 말해. 답변은 50자 이내여야 해."})

    # OpenAI API 호출
    response2 = client.chat.completions.create(
        model="gpt-4.1-nano",  # 모델 이름 수정
        messages=messages2
    )
    bot_response2 = response2.choices[0].message.content

                        
# =============================================            
            


    messages3 = [
        {"role": "system", "content": 'you are a helpful assistant. Tell me todays financial fortune. Speak in English, be kind, and keep the answer under 300 characters.'}
    ]




    # 대화에 사용자 메시지 추가
    messages3.append({"role": "user", "content" : "Tell me todays financial fortune. Speak in English, be kind, and keep the answer under 300 characters."})

    # OpenAI API 호출
    response3 = client.chat.completions.create(
        model="gpt-4.1-nano",  # 모델 이름 수정
        messages=messages3
    )
    bot_response3 = response3.choices[0].message.content


    # 템플릿에 전달할 데이터
    context = {
        'title': title,
        'q': q,
        '로또번호': bot_response,
        '답변근거': bot_response2,
        '금전운': bot_response3,
        'a' : 8
        # 'map': fig
        # , ax
    }

    return render(request, 'main/lotto_predict.html', context)

def fortune_check(request):
        # 파이썬에서 계산한 값이나 데이터
    title = "테스트 페이지"
    q  = "웹페이지에 ai 심기 테스트"



    load_dotenv()  # .env 파일의 변수들을 로드함

    api_key = os.getenv('OPENAI_API_KEY')
    # Store your OpenAI API key in an environment variable or secure file
    client = OpenAI(api_key=api_key)  #여기에 본인의 OpenAI API를 입력하시면 됩니다.

    lottodata= " 7,9,24,40,42,44 / 3,6,7,11,12,17 / 3,13,28,34,38,42 / 5,12,24,26,39,42 / 9,21,24,30,33,37 / 8,23,31,35,39,40 / 14,23,25,27,29,42 / 6,7,27,29,38,45 / 17,18,23,25,38,39 / 2,13,15,16,33,43 "
    # messages = [
    #     ("system", 'you are a helpful assistant. 넌 과거 로또 데이터를 기반으로 6개의 로또 번호를 예측하는 ai야. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45사이의 수야.'),


    #     ("human",  "{lottodata}를 기반으로 6개의 로또 번호를 예측해. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45 사이의 수야. 3,13,28,34,38,42 이런 예시처럼 출력하되 숫자마다 콤마로 구분해."),
    #     ]
    # prompt_template = ChatPromptTemplate.from_messages(messages)
    # prompt = prompt_template.invoke({"lottodata": lottodata})
    # #디폴트로 model변수의 AI 모델을 쓰는거임?
    
    # # llm.invoke(prompt) 

    # # OpenAI API 호출
    # response = client.chat.completions.create(
    #     model="gpt-4.1-nano",  # 모델 이름 수정
    #     messages=prompt
    # )
    # bot_response = response.choices[0].message.content
    messages = [
        {"role": "system", "content": 'you are a helpful assistant. 넌 과거 로또 데이터를 기반으로 6개의 로또 번호를 예측하는 ai야. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45사이의 수야.'},
        {"role": "user", "content": f"{lottodata}를 기반으로 6개의 로또 번호를 예측해. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45 사이의 수야. 3,13,28,34,38,42 이런 예시처럼 출력하되 숫자마다 콤마로 구분해."}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages
    )
    bot_response = response.choices[0].message.content
        
# ====================================
    



    messages2 = [
        {"role": "system", "content": 'you are a helpful assistant. 넌 절대 숫자를 출력하지 않아. 아까 출력한 숫자에 대한 근거를 영어로 알려주는 ai임. '}
    ]




    # 대화에 사용자 메시지 추가
    messages2.append({"role": "user", "content": "방금 출력한 6자리 로또 출력에 대한 근거만 영어로 말해. 답변은 50자 이내여야 해."})

    # OpenAI API 호출
    response2 = client.chat.completions.create(
        model="gpt-4.1-nano",  # 모델 이름 수정
        messages=messages2
    )
    bot_response2 = response2.choices[0].message.content

                        
# =============================================            
            


    messages3 = [
        {"role": "system", "content": 'you are a helpful assistant. Tell me todays financial fortune. Speak in English, be kind, and keep the answer under 300 characters.'}
    ]




    # 대화에 사용자 메시지 추가
    messages3.append({"role": "user", "content" : "Tell me todays financial fortune. Speak in English, be kind, and keep the answer under 300 characters."})

    # OpenAI API 호출
    response3 = client.chat.completions.create(
        model="gpt-4.1-nano",  # 모델 이름 수정
        messages=messages3
    )
    bot_response3 = response3.choices[0].message.content


    # 템플릿에 전달할 데이터
    context = {
        'title': title,
        'q': q,
        '로또번호': bot_response,
        '답변근거': bot_response2,
        '금전운': bot_response3,
        'a' : 8
        # 'map': fig
        # , ax
    }

    return render(request, 'main/fortune_check.html', context)

def lotto_history(request):
    return render(request, 'main/lotto_history.html')

def lotto_combiner(request):
    return render(request, 'main/lotto_combiner.html')
def fff(request):
    # 파이썬에서 계산한 값이나 데이터
    title = "테스트 페이지"
    q  = "웹페이지에 ai 심기 테스트"



    load_dotenv()  # .env 파일의 변수들을 로드함

    api_key = os.getenv('OPENAI_API_KEY')
    # Store your OpenAI API key in an environment variable or secure file
    client = OpenAI(api_key=api_key)  #여기에 본인의 OpenAI API를 입력하시면 됩니다.

    lottodata= " 7,9,24,40,42,44 / 3,6,7,11,12,17 / 3,13,28,34,38,42 / 5,12,24,26,39,42 / 9,21,24,30,33,37 / 8,23,31,35,39,40 / 14,23,25,27,29,42 / 6,7,27,29,38,45 / 17,18,23,25,38,39 / 2,13,15,16,33,43 "
    # messages = [
    #     ("system", 'you are a helpful assistant. 넌 과거 로또 데이터를 기반으로 6개의 로또 번호를 예측하는 ai야. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45사이의 수야.'),


    #     ("human",  "{lottodata}를 기반으로 6개의 로또 번호를 예측해. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45 사이의 수야. 3,13,28,34,38,42 이런 예시처럼 출력하되 숫자마다 콤마로 구분해."),
    #     ]
    # prompt_template = ChatPromptTemplate.from_messages(messages)
    # prompt = prompt_template.invoke({"lottodata": lottodata})
    # #디폴트로 model변수의 AI 모델을 쓰는거임?
    
    # # llm.invoke(prompt) 

    # # OpenAI API 호출
    # response = client.chat.completions.create(
    #     model="gpt-4.1-nano",  # 모델 이름 수정
    #     messages=prompt
    # )
    # bot_response = response.choices[0].message.content
    messages = [
        {"role": "system", "content": 'you are a helpful assistant. 넌 과거 로또 데이터를 기반으로 6개의 로또 번호를 예측하는 ai야. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45사이의 수야.'},
        {"role": "user", "content": f"{lottodata}를 기반으로 6개의 로또 번호를 예측해. 답변은 6개의 숫자 말고 절대 다른 출력이 있으면 안돼. 각 숫자는 1에서 45 사이의 수야. 3,13,28,34,38,42 이런 예시처럼 출력하되 숫자마다 콤마로 구분해."}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages
    )
    bot_response = response.choices[0].message.content
        
# ====================================
    



    messages2 = [
        {"role": "system", "content": 'you are a helpful assistant. 넌 절대 숫자를 출력하지 않아. 아까 출력한 숫자에 대한 근거를 영어로 알려주는 ai임. '}
    ]




    # 대화에 사용자 메시지 추가
    messages2.append({"role": "user", "content": "방금 출력한 6자리 로또 출력에 대한 근거만 영어로 말해. 답변은 50자 이내여야 해."})

    # OpenAI API 호출
    response2 = client.chat.completions.create(
        model="gpt-4.1-nano",  # 모델 이름 수정
        messages=messages2
    )
    bot_response2 = response2.choices[0].message.content

                        
# =============================================            
            


    messages3 = [
        {"role": "system", "content": 'you are a helpful assistant. Tell me todays financial fortune. Speak in English, be kind, and keep the answer under 300 characters.'}
    ]




    # 대화에 사용자 메시지 추가
    messages3.append({"role": "user", "content" : "Tell me todays financial fortune. Speak in English, be kind, and keep the answer under 300 characters."})

    # OpenAI API 호출
    response3 = client.chat.completions.create(
        model="gpt-4.1-nano",  # 모델 이름 수정
        messages=messages3
    )
    bot_response3 = response3.choices[0].message.content


    # 템플릿에 전달할 데이터
    context = {
        'title': title,
        'q': q,
        '로또번호': bot_response,
        '답변근거': bot_response2,
        '금전운': bot_response3,
        'a' : 8
        # 'map': fig
        # , ax
    }

    return render(request, 'main/index.html', context)
    # return bot_response

    