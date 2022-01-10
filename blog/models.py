from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish"),
)


### Add New.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default= " WebPres Today Post")
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='add_post')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now= True)
    # The rest of the fields..

    #class Meta:
        #ordering = ['-created_on'}
        #abstract = True


    def __str__(self):
        return self.title + '|' + str(self.author)
    def complete_update(self):
        self.status = 'Complete'
        self.save()


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)