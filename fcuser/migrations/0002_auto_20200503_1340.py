# Generated by Django 3.0.5 on 2020-05-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '패스트 캠퍼스 사용자', 'verbose_name_plural': '패스트 캠퍼스 사용자'},
        ),
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='test@naver.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]
