from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

import os
from uuid import uuid4
from django.utils import timezone
def uuid_name_upload_to(instance, filename):
    app_label = instance.__class__._meta.app_label
    cls_name = instance.__class__.__name__.lower()
    ymd_path = timezone.now().strftime('%Y/%m/%d’)
    uuid_name = uuid4().hex
# 앱 별로
# 모델 별로
# 업로드하는 년/월/일 별로
extension = os.path.splitext(filename)[-1].lower() # 확장자 추출하고, 소문자로 변환 return '/'.join([
    app_label,
    cls_name,
    ymd_path,
    uuid_name[:2],
    uuid_name + extension,
])
