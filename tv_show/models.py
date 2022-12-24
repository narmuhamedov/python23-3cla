from django.db import models

class TvShow(models.Model):
    GENRE = (
        ('Detective', 'Detective'),
        ('Horror', 'Horror'),
        ('Anime', 'Anime'),
        ('Comedy', 'Comedy'),
        ('Document', 'Document')
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, choices=GENRE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class CommentTvShow(models.Model):
    choice_show = models.ForeignKey(TvShow, on_delete=models.CASCADE,
                                    related_name='comment_object')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
