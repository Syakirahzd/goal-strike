import json
from django.http import HttpResponse
from django.core import serializers
# from main.models import Employee

from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'title': '== GoalStrike ==',
        'npm': '2406353950',
        'name': 'Syakirah Zahra Dhawini',
        'class': 'PBP D',
        'product_list': product_list,
        'username': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_product()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'pk': str(product.id), # Ubah 'id' menjadi 'pk'
            'model': 'main.product',
            'fields': { # Buat nested object 'fields'
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'category': product.category,
                'thumbnail': product.thumbnail,
                'product_views': product.product_views,
                'is_featured': product.is_featured,
                'user': product.user_id,
            }
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'content': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)




def login_user(request):
    if request.method == 'POST':
        # Check if it's an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'success': True,
                    'message': 'Login successful!',
                    'redirect': reverse('main:show_main')
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid username or password. Please try again.'
                }, status=400)
        
        # Handle normal form submission (fallback)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        # Check if it's an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                user = form.save()
                login(request, user)
                return JsonResponse({
                    'success': True,
                    'message': 'Account created successfully!',
                    'redirect': reverse('main:show_main')
                })
            else:
                # Format errors for JSON response
                errors = {}
                for field, error_list in form.errors.items():
                    if field == '__all__':
                        errors['general'] = error_list
                    else:
                        errors[field] = error_list
                
                return JsonResponse({
                    'success': False,
                    'message': 'Please correct the errors below.',
                    'errors': errors
                }, status=400)
        
        # Handle normal form submission (fallback)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('main:show_main')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)


def logout_user(request):
    # Check if it's an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        logout(request)
        return JsonResponse({
            'success': True,
            'message': 'You have been logged out successfully.',
            'redirect': reverse('main:login')
        })
    
    # Handle normal request (fallback) - NO Django messages
    logout(request)
    return redirect('main:login')

def edit_product(request, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        # Tambahkan baris ini
        messages.success(request, 'Product updated successfully!')
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product_name = product.name # Simpan nama sebelum dihapus
    product.delete()
    # Tambahkan baris ini
    messages.info(request, 'Product deleted successfully!')
    return redirect('main:show_main')

@csrf_exempt
@require_POST
@csrf_exempt
def create_product_ajax(request):
    if request.method == 'POST':
        # Gunakan ProductForm untuk validasi dan keamanan
        form = ProductForm(request.POST) 
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            # Kembalikan respons JSON yang jelas
            return JsonResponse({'status': 'success', 'message': 'Product created successfully!'}, status=201)
        else:
            # Jika form tidak valid, kembalikan error dalam format JSON
            errors = json.loads(form.errors.as_json())
            error_message = list(errors.values())[0][0]['message']
            return JsonResponse({'status': 'error', 'message': error_message}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

# views.py

@require_POST
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, id=id, user=request.user)
        product.delete()
        return JsonResponse({'status': 'success', 'message': 'Product deleted successfully!'}, status=200)
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found or you do not have permission.'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    

# main/views.py

# ... (import lain yang sudah ada)

# View untuk mengambil data satu produk sebagai JSON
def get_product_json(request, id):
    try:
        product = Product.objects.get(pk=id)
        data = {
            'pk': str(product.id),
            'fields': {
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'category': product.category,
                'thumbnail': product.thumbnail,
            }
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)

# View untuk memproses update produk via AJAX
@csrf_exempt
def update_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id, user=request.user)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Product updated successfully!'})
        else:
            errors = json.loads(form.errors.as_json())
            error_message = list(errors.values())[0][0]['message']
            return JsonResponse({'status': 'error', 'message': error_message}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


### DEMO Tugas 2 ##
# def add_employee(request):
#     new_employee = Employee.objects.create(
#         name = "Syakirah",
#         age = 19,
#         persona = "terserah",
#         )
    
#     context = {
#         "name" : new_employee.name,
#         "age" : new_employee.age,
#         "persona" : new_employee.persona
#     }

#     return render(request, "employee.html", context)
