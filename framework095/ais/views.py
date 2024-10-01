from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentsForm
from .models.students import Students  # Pastikan ini mengimpor kelas model

# CREATE Mahasiswa
def student_create(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data mahasiswa ke database
            messages.success(request, 'Mahasiswa berhasil dibuat!')  # Pesan sukses
            return redirect('student_index')  # Redirect ke halaman index mahasiswa
    else:
        form = StudentsForm()
    return render(request, 'student/create.html', {'form': form})

# READ Mahasiswa
def student_index(request):
    student_list = Students.objects.all()  # Gunakan nama variabel yang berbeda
    return render(request, 'student/index.html', {'students': student_list})

# Halaman lainnya
def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')
