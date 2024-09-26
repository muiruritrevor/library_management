from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13)
    description = models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
class Transaction(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    book = models.ForeignKey('Library_api.Book', on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.book.title