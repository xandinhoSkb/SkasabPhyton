"""
Definition of models.
"""

from django.db import models
from django.db.models import Sum

class Poll(models.Model):
    """Um objeto de pesquisa para uso nas visualizações e no repositório do aplicativo."""
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def total_votes(self):
        """Calcula o número total de votos para esta enquete"""
        return self.choice_set.aggregate(Sum('votes'))['votes__sum']

    def __unicode__(self):
        """Retorna uma representação de string de uma pesquisa."""
        return self.text

class Choice(models.Model):
    """A poll choice object for use in the application views and repository."""
    poll = models.ForeignKey(Poll)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def votes_percentage(self):
        """Calculates the percentage of votes for this choice."""
        total = self.poll.total_votes()
        return self.votes / float(total) * 100 if total > 0 else 0

    def __unicode__(self):
        """Retorna uma representação de string de uma escolha."""
        return self.text
