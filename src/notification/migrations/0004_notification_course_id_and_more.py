# Generated by Django 5.1.1 on 2024-10-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_rename_notifications_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='course_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('comment_post', 'Comment on Post'), ('comment_video', 'Comment on Video'), ('reply_comment', 'Reply to Comment'), ('like_post', 'Like on Post'), ('like_comment', 'Like on Comment'), ('new_course', 'New Course Available'), ('course_update', 'Course Updated')], max_length=50),
        ),
    ]
