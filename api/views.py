from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from api.models import Customer,Work

from api.serializers import CustomerSerializer,WorkSerializer

from rest_framework import authentication,permissions

from rest_framework.decorators import action

from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView

class CustomerViewSetView(ModelViewSet):

    serializer_class=CustomerSerializer

    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):

        serializer.save(technician=self.request.user)

    @action(methods=["POST"],detail=True)
    def add_work(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        customer_instance=Customer.objects.get(id=id)

        serializer_instance=WorkSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(customer=customer_instance)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)


class WorkCreationView(CreateAPIView):

    serializer_class=WorkSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):

        id=self.kwargs.get("pk")

        customer_instance=Customer.objects.get(id=id)

        serializer.save(customer=customer_instance)

class WorkDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class=WorkSerializer

    queryset=Work.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]