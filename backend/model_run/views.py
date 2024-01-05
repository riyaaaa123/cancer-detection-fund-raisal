from django.shortcuts import render
import subprocess
# Create your views here.

def detect_objects(request):
    # Run YOLOv7 command
    command = 'streamlit run model/app.py'
    subprocess.run(command, shell=True)

    return render(request, 'model_run/detection_result.html')