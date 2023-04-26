from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegister
from rest_framework.authtoken.models import Token

class helloworldView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"hello world"})
class name(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"how are you....?"})

class AddNumbersView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        result=n1+n2
        return Response({"Addition result=":result})
class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n=request.data.get("x")
        result=n**3
        return Response({"the cube of the number is=":result})
class Fcatorialclass(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n=request.data.get("num1")
        fact=1
        for i in range(1,n+1,):
            fact=fact*i
        return Response({"factorial =":fact})
class primeView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n=request.data.get("num1")
        for i in range(2,n+1):
            if(n%i)==0:
                return Response({"it is a primnumber":n})
            return Response({"it is not a primenumber"})


class register(APIView):
    def post(self,request,format=None):
        data={}
        serializer=UserRegister(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            data['response=']='Registerd'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)
