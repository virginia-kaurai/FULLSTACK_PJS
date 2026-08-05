from django.db import models


from django.utils import timezone


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    slogan = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Class(models.Model):


    class ClassObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='active')
        
    name =models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    population = models.IntegerField()
    duration = models.IntegerField(help_text="Duration in months")
    created_at = models.DateTimeField(default=timezone.now)
    options= (
        ('active', 'active'),
        ('graduated', 'graduated'),
    )
    status= models.CharField(max_length=20, choices=options, default='active')


    objects = models.Manager() # default manager
    class_objects = ClassObject() # custom manager


    class Meta:
        ordering = ['-created_at']
        

    def __str__(self):
        return self.name


