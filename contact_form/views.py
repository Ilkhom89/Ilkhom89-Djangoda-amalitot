from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_form(request):
    if request.method == 'POST':
        # POST so‘rov bo‘lsa, ma’lumotlarni saqlash
        ContactMessage.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            message=request.POST['message'],
        )
        return redirect('messages')  # yuborilgandan keyin xabarlar sahifasiga yo‘naltirish

    # GET so‘rov bo‘lsa, form sahifasini ko‘rsatish
    return render(request, 'contact_form/form.html')


def messages_list(request):
    # Bazadagi barcha xabarlarni olish
    messages = ContactMessage.objects.all()
    return render(request, 'contact_form/messages.html', {'messages': messages})
