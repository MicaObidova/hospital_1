from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializer import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view



class Info(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_info(self,request):
            info = Info.objects.all()
            data = {
                "info": info
            }
            return Response(data)

class Patients(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.types == 1 or user.types == 2:
            patient = AnalysisPatient.objects.all()
            ser = AnalysisPatientSerializer(patient,many=True)
            return Response(ser.data)


class Categoryview(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user
        if user.types ==3 or user.types ==2 or user.types ==1:
            category = Category.objects.all()
            ser = CategorySerializer(category,many=True)
            return Response(ser.data)


class CreatePatient(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        user = request.user
        if user.types == 1 or user.types == 2:
            category = request.POST.get('category')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            age = request.POST.get('age')
            injury = request.POST.get('injury')
            adress = request.POST.get('adress')
            doctorname = request.POST.get('doctorname')
            query = RegisterPatient.objects.create(category_id=category,name=name,phone=phone,age=age,injury=injury,adress=adress,doctorname_id=doctorname)
            ser = RegPatientSerializer(query)
            return Response(ser.data)
        else:
             return Response('siz doktor emassiz')

class ViewSPecialists(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
            query = User.objects.filter(types=1)
            ser = UserSerializer(query,many=True)
            return Response(ser.data)


class IsInjury(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user
        if user.types == 1 or user.types == 2:
          query = AnalysisPatient.objects.filter(is_injury=1)
          return Response(AnalysisPatientSerializer(query,many=True).data)
        else:
            return Response('xatolik')



class FilterForDoctors(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user
        if user.types == 1:
            query = RegisterPatient.objects.filter(doctorname=user)
            ser = RegPatientSerializer(query,many=True)
            return Response(ser.data)


class PatientMedicines(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk):
        user = request.user
        if user.types ==3:
            get = AnalysisPatient.objects.get(id=pk)
            if get.is_injury==True:
               summa = 0
               summa +=get.pharmacy.price * get.quantitymedicine
               name = get.patient.name
               medicine = get.pharmacy.name
               return Response({'summa': summa, 'patient': name, 'dori nomi': medicine})
            else:
                return Response('Siz soglomsiz solomat ')
        else:
            return Response('boshqa user!!!')


class AllThose(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        use = ThoseTreated.objects.all()
        return Response(ThoseSerializer(use,many=True).data)



class FilterThose(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user
        if user.types == 1:
            g = ThoseTreated.objects.filter(doctorname=user)
            listlar = []
            for i in g:
                 if i.patient.is_injury == 1:
                     data = {
                         'ismi': i.patient.patient.name,
                         'umumiy narxi': i.patient.quantitymedicine * i.patient.pharmacy.price,
                         'tolov': i.is_paid,
                         'davolangan manzili':i.patient.typetreatment
                     }
                     listlar.append(data)
            return Response({'kasallar': listlar})




