from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0005_auto_20200930_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='pessoa',
           field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
