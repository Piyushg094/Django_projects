from django.http import JsonResponse
from .models import User
from rest_framework import status

def list_of_users(request):
    users = User.objects.all()

    response_data = []
    for user in users:
        response_data.append({
           "created_by":{
            "name": user.name,
           }
        })

    return JsonResponse({
        "message": "List of the users",
        "data": response_data
    }, status=status.HTTP_200_OK)




    #  response_data = []
    #     for tag in tags:
    #         response_data.append(
    #             "created_by":{
    #             {
    #                 "name": tag.name,
    #                 "uuid": tag.uuid
    #             }
    #             }
    #         )
