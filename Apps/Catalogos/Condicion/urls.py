from django.urls import path
from .views import ConditionLvl_ApiView, Condition_PPPD_ApiView

urlpatterns = [

    path("", ConditionLvl_ApiView.as_view()), #Listar Bebidas (Público)
    path('<int:pk>', Condition_PPPD_ApiView.as_view()),  # POST, PATCH, PUT Y DELETE para las bebidas (Con autenticacion JWT)

]