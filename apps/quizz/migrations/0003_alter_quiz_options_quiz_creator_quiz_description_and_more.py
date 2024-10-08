# Generated by Django 5.1.1 on 2024-10-07 05:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_rename_crated_at_instructor_created_at'),
        ('quizz', '0002_rename_crated_at_choice_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ('created_at',), 'verbose_name': 'Quiz', 'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AddField(
            model_name='quiz',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instructors.instructor'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('choice', models.CharField(max_length=1000)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quizz.question')),
            ],
            options={
                'verbose_name': 'Choice',
                'verbose_name_plural': 'Choices',
            },
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('score', models.IntegerField(default=0)),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='quizz.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_attempts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quiz Attempt',
                'verbose_name_plural': 'Quiz Attempts',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attempt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='quizz.quizattempt')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='quizz.question')),
                ('selected_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='quizz.answer')),
            ],
            options={
                'verbose_name': 'User Answer',
                'verbose_name_plural': 'User Answers',
            },
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
