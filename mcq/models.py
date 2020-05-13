from django.db import models
from django.utils.translation import ugettext_lazy as _
from exam.models import Question 
# Create your models here.
CHOICE_ORDER_OPTIONS = (
    ('content', _('Content')),
    ('random', _('Random')),
    ('none', _('None'))
)
class MCQ(Question):
    choice_order = models.CharField(
    max_length=30, null=True, blank=True,
    choices=CHOICE_ORDER_OPTIONS,
    help_text=_("The order in which multichoice "
                "choice options are displayed "
                "to the user"),
    verbose_name=_("choice Order"))

    def check_if_correct(self, guess):
        choice = Choice.objects.get(id=guess)

        if choice.correct is True:
            return True
        else:
            return False

    def order_choices(self, queryset):
        if self.choice_order == 'content':
            return queryset.order_by('content')
        if self.choice_order == 'random':
            return queryset.order_by('?')
        if self.choice_order == 'none':
            return queryset.order_by()
        return queryset

    def get_choices(self):
        return self.order_choices(Choice.objects.filter(question=self))

    def get_choices_list(self):
        return [{'id': choice.id, 'text': choice.choice_text} for choice in
                self.order_choices(Choice.objects.filter(question=self.pk))]

    def choice_choice_to_string(self, guess):
        return Choice.objects.get(id=guess).choice_text

    class Meta:
        verbose_name = _("Multiple Choice Question")
        verbose_name_plural = _("Multiple Choice Questions")

class Choice(models.Model):
    question = models.ForeignKey(MCQ, verbose_name=_("Question"), on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=1000,
                               blank=False,
                               help_text=_("Enter the choice text"),
                               verbose_name=_("Choice Text"))

    is_correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text=_("Is this a correct choice?"),
                                  verbose_name=_("Correct"))

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")

