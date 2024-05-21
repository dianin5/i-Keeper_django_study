from django.conf import settings
from django.db import models
from django.utils import timezone


# 모델을 정의하는 코드입니다. 
# models.Model -> Post가 장고 모델임을 밝힙니다. 

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
'''
- models.CharField
    - 글자 수 제한 / max_length = 200
- models.TextField
    - 글자 수 제한이 없는 긴 텍스트를 위한 속성입니다.
- models.DateTimeField
    - 날짜와 시간을 의미합니다.
- models.Foreignkey
    - 다른 모델에 대한 링크를 의미합니다.

- def publish(self):
    - publish 라는 메서드입니다.
    - published_date 값을 업데이트하고, 저장하는 역할을 수행합니다.
    - (글 공개)

- __str__(self):
    - 호출시 Post 모델의 제목 테스트 / String 제공
    '''
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)