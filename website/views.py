from django.shortcuts import render
import os
from django.conf import settings

def home(request):
    # Get images from proizvodi folder
    proizvodi_images = []
    images_path = os.path.join(settings.BASE_DIR, 'website', 'static', 'website', 'images', 'proizvodi')
    
    if os.path.exists(images_path):
        for filename in os.listdir(images_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                image_info = {
                    'filename': filename,
                    'url': f'website/images/proizvodi/{filename}',
                    'name': os.path.splitext(filename)[0].replace('_', ' ').replace('-', ' ').title()
                }
                proizvodi_images.append(image_info)
    
    context = {
        'proizvodi_images': proizvodi_images
    }
    return render(request, 'website/home.html', context)
