from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils  import timezone
from django.contrib.auth.models import User
# Create your models here.



class Exam(models.Model):
    sub_code = models.CharField(max_length = 10, verbose_name='Subject Code')
    exam_title = models.CharField(max_length = 100, verbose_name='Exam Title', null=True)
    max_marks = models.PositiveIntegerField(default = 0)
    show_answer_after_exam = models.BooleanField(default = False, verbose_name=_('Show answers after the exam?'))
    date_open = models.DateTimeField(default = timezone.now,verbose_name=_('Opening Date and Time')) # This allows us to modify the date if we want.
    date_closed = models.DateTimeField(default = timezone.now, verbose_name=_('Closing Date and Time')) # This allows us to modify the date if we want.
    date_modified = models.DateTimeField(auto_now=True,null= True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    draft = models.BooleanField(default=False)

    def __str__(self):
            return self.sub_code +":" + self.exam_title


class Category(models.Model):
    category = models.CharField(max_length = 100, verbose_name = 'Category Name', blank=True,
        unique=True, null=True)
    exam_name = models.ForeignKey(Exam,null=True, blank=True,
        verbose_name=_("Exam Name"), on_delete=models.CASCADE)
    num_qns_from_cat = models.PositiveIntegerField(default=1, verbose_name = _('Number of Questions from this Category'))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category



class Question(models.Model):
    question_text = models.TextField(max_length=2000,verbose_name=_('Question'))
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    exam = models.ManyToManyField(Exam,
                                  verbose_name=_("For which Exam?"),
                                  blank=True, help_text="You can leave it empty if you want to choose random question from a category.")

    figure = models.ImageField(upload_to='questionImages/%Y/%m/%d',
                               blank=True,
                               null=True,
                               verbose_name=_("Figure"))
    mark = models.PositiveIntegerField(verbose_name=_('Marks'),default = 0)


    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['category']

    def __str__(self):
        return self.question_text