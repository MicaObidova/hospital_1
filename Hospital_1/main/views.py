from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializer import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view



class Info(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_info(self,request):
        if User.STATUS == User.STATUS:
            info = Info.objects.get(user=User)
            data = {
                "info" : info
            }
            return Response(request,data)

class Patients(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_patient(self,request):
        if User.STATUS == 1 or 2:
            patient = AnalysisPatient.objects.get(user=User)
            data = {
                "patient": patient
            }
            return Response(request,data)


class Category(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_category(self,request):
        if User.STATUS == User.STATUS:
            category = Category.objects.all()
            data = {
                "category": category
            }
            return Response(request,data)


class Analys(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_analys(self, request):
        if User.STATUS == 3:
            if AnalysisPatient.STATUS == 1:
                return AnalysisPatient.STATUS == 1
            else:
                return AnalysisPatient.STATUS == 2


# umida qiz
# -------------
# Infoni chqarib beruvchi APIView (hamma user ko'raverishi kerak)
# barcha bemorlarni chiqarib beruvchi APIView (faqat doctor yoki reception uchun)
# Barcha categoriyalarni chiqarib beruvchi APIView (hamma user uchun)
# Har bir Bemor o'zini analizini chiqarib beruvchi apiview (faqat bemor ko'rishi kerak)


