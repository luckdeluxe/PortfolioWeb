from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(verbose_name="Image", upload_to="projects")
    link = models.URLField(verbose_name="Web address", null=True, blank=True)
    cfuente = models.URLField(verbose_name="Source code", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edition date")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-created"]

    def __str__(self):
        return self.title