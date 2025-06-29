# quiz/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# View สำหรับ GET /quiz/question
def question(request):
    if request.method == 'GET':
        # ข้อมูลตัวอย่างที่จะส่งกลับไปเป็น JSON
        data = {
            "id": 1,
            "text": "ประเทศไทยมีกี่จังหวัด",
            "choices": [50, 68, 72, 77]
        }
        return JsonResponse(data)


# View สำหรับ POST /quiz/question/create
@csrf_exempt  # ใช้ decorator นี้เพื่ออนุญาต POST request จากภายนอกโดยไม่มี CSRF token (สำหรับการทดสอบ)
def create_question(request):
    if request.method == 'POST':
        # รับข้อมูล JSON จาก body ของ request
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        # ในตัวอย่างนี้ เราจะส่งข้อมูลที่ได้รับกลับไปเลย
        # ในการใช้งานจริง ควรมีการบันทึกข้อมูลลงฐานข้อมูล
        # และสร้าง id ใหม่ที่ไม่ซ้ำกัน

        # สมมติว่าข้อมูลที่ส่งมามีรูปแบบตามที่คาดหวัง
        # {"text": "some question", "choices": ["a", "b", "c"]}
        response_data = {
            "id": body_data.get('id', 9),  # ใช้ id ที่ส่งมา หรือใช้ 9 เป็นค่าเริ่มต้น
            "text": body_data.get('text'),
            "choices": body_data.get('choices')
        }

        return JsonResponse(response_data, status=201)  # ตอบกลับด้วย status 201 Created