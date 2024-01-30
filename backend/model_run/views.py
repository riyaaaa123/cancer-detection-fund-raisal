from django.shortcuts import render
import subprocess
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PredictionResult
from users.models import User

# Create your views here.

def detect_objects(request):
    # Run YOLOv7 command
    command = 'streamlit run model/app.py --server.port 3003'
    subprocess.run(command, shell=True)

    return render(request, 'model_run/detection_result.html')

# @api_view(['GET', 'POST'])
# def save_prediction_result(request):
#     data = request.data
#     prediction = data.get('prediction', None)

#     try:
#         # Save the prediction result to the database
#         if prediction:
#             PredictionResult.objects.create(result=prediction)
#             return Response({'message': 'Prediction result saved successfully'})
#         else:
#             return Response({'message': 'Invalid data'}, status=400)

#     except Exception as e:
#         return Response({'message': f'Error saving prediction result: {str(e)}'}, status=500)


@api_view(['POST', 'GET'])
def save_prediction_result(request):
    data = request.data
    prediction = data.get('prediction', None)
    user_id = data.get('user_id', None)  # Receive user ID from frontend

    try:
        if prediction and user_id:
            user = User.objects.get(pk=user_id)
            PredictionResult.objects.create(user=user, result=prediction)
            return Response({'message': 'Prediction result saved successfully'})
        else:
            return Response({'message': 'Invalid data'}, status=400)

    except Exception as e:
        return Response({'message': f'Error saving prediction result: {str(e)}'}, status=500)