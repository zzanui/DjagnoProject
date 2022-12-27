import os
import sys
import urllib.request




class papagoapi():
    
    def __init__(self):
        self.__client_id = "eLByxNU5CZEfxT69X1lA" # 개발자센터에서 발급받은 Client ID 값
        self.__client_secret = "waM6Pd00jU" # 개발자센터에서 발급받은 Client Secret 값
        
    #네이버 Papago 번역 API 예제
    def papago_translation(self,text):
        encText = urllib.parse.quote(text)
        data = "source=ko&target=en&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",self.__client_id)
        request.add_header("X-Naver-Client-Secret",self.__client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            print("papago_translation : ")
            print(response_body.decode('utf-8'))
            return(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
    # 네이버 Papago 언어감지 API 예제
    def papago_sensing(self,text):
        encQuery = urllib.parse.quote(text)
        data = "query=" + encQuery
        url = "https://openapi.naver.com/v1/papago/detectLangs"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",self.__client_id)
        request.add_header("X-Naver-Client-Secret",self.__client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            print(response_body.decode('utf-8'))
            return(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)

    def papago_to_rome(self,text):
        encText = urllib.parse.quote(text)
        url = "https://openapi.naver.com/v1/krdict/romanization?query=" + encText
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",self.__client_id)
        request.add_header("X-Naver-Client-Secret",self.__client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            print(response_body.decode('utf-8'))
            return(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
            
            
