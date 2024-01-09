from django.urls import path

from measurement import views

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor_create/', views.CreateSensor.as_view()),
    path('sensor_update/<int:pk>', views.UpdateSensor.as_view()),
    path('sensors_list/', views.GetSensorsList.as_view()),
    path('sensor/<int:pk>', views.GetSensorData.as_view()),
    path('measurements/', views.CreateMeasurement.as_view())
]
