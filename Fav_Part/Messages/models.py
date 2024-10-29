from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)  # Allow blank titles initially
    content = models.TextField()
    signed = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    incremental_id = models.PositiveIntegerField(editable=False, unique=True, null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)  # Field to track likes

    def save(self, *args, **kwargs):
        # Set the incremental_id if it's not already set
        if self.incremental_id is None:
            last_post = Post.objects.all().order_by('incremental_id').last()
            if last_post:
                self.incremental_id = last_post.incremental_id + 1
            else:
                self.incremental_id = 1
        
        # If no title is provided, set a default title based on the incremental_id
        if not self.title:
            self.title = f"Note {self.incremental_id}"
        
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.incremental_id}: {self.title}"
