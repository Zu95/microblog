from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Autor")
    title = models.CharField("Tytuł", max_length=200)
    text = models.TextField("Treść")
    brief = models.TextField("Skrót", max_length=500)
    created_date = models.DateTimeField("Data utworzenia",
                                        default=timezone.now)
    published_date = models.DateTimeField("Data publikacji",
                                          blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Kategoria")
    picture = models.ImageField("Zdjęcie główne", upload_to='images')

    class Meta:
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField("Nazwa", max_length=200)
    description = models.TextField("Opis")
    picture = models.ImageField("Zdjęcie główne", upload_to='category_images')

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class QuestionAnswer(models.Model):
    title = models.CharField("Tytuł", max_length=60)
    question = models.TextField("Treść pytania")
    author = models.CharField("Autor", max_length=100)
    asked_date = models.DateTimeField("Data przesłania", default=timezone.now)
    answer = models.TextField("Odpowiedź", default=None, null=True)
    published = models.BooleanField("Opublikowano", default=False)

    class Meta:
        verbose_name = "Pytanie i odpowiedź"
        verbose_name_plural = "Pytania i odpowiedzi"

    def ask(self):
        self.save()

    def publish(self):
        self.published = True
        self.save()

    def __str__(self):
        if self.published:
            text = self.title + " - opublikowane"
        else:
            text = self.title + " - nieopublikowane"

        return text
