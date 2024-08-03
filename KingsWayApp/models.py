from django.db import models

# Create your models here.
def validate_name(value):
    if not re.match("^[a-zA-Z ]*$", value):
        raise ValidationError(
            '%(value)s is not a valid name. Only letters and spaces are allowed.',
            params={'value': value},
        )

class Subscription(models.Model):
    name = models.CharField(max_length=100, blank=True, validators=[validate_name])
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email