from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from.models import Book
from .models import Address
from django.shortcuts import redirect
from .models import Student,Address, ImageModel
from .forms import AddressForm , StudentForm , ImageForm
#def book(request):
   # return render(request,'book/book.html')
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='d') # <- multiple objects
    return render(request, 'book/book.html', {'books':mybooks})
def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='a').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'book/book.html', {'books':mybooks})
    else:
         bo= Book.objects.all()
         return render(request, 'book/books.html')

def task1_view(request):
    # Filter books with price less than or equal to 50
    affordable_books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'book/task1.html', {'books': affordable_books})
def task2_view(request):
    # Filter books with edition > 2 and either 'qu' in title or author
    filtered_books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'book/task2.html', {'books': filtered_books})
def task3_view(request):
    # Filter books with edition <= 2 and neither 'qu' in title nor author
    filtered_books = Book.objects.filter(
        Q(edition__lte=2) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu')
    )
    return render(request, 'book/task3.html', {'books': filtered_books})
def task4_view(request):
    # Retrieve all books and order by title
    books_ordered_by_title = Book.objects.all().order_by('title')
    return render(request, 'book/task4.html', {'books': books_ordered_by_title})
def task5_view(request):
    # Aggregate the required values
    book_stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'book/task5.html', {'book_stats': book_stats})
def students(request):
    # Aggregate the number of students per city
    city_student_counts = Address.objects.annotate(student_count=Count('students'))
    return render(request, 'book/students.html', {'city_student_counts': city_student_counts})
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'book/last_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        Book.objects.create(title=title, author=author)
        return redirect('/books/lab9_part1/last_list')
    return render(request, 'book/add_book.html')

def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('/books/lab9_part1/last_list')
    return render(request, 'book/edit_book.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books/lab9_part1/last_list')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'book/student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            form.save_m2m()  # Save the many-to-many relationship
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'book/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list view
    else:
        form = StudentForm(instance=student)
    return render(request, 'book/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')

def image_list(request):
    # Fetch all images from the database
    images = ImageModel.objects.all()
    return render(request, 'book/image_list.html', {'images': images})

def upload_image(request):
    # Handle form submission
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)  # Include the FILES parameter for handling images
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('image_list')  # Redirect to the image list after successful upload
    else:
        form = ImageForm()  # Display an empty form if the request is GET
    return render(request, 'book/upload_image.html', {'form': form})
    