from rest_framework import serializers
from apps.assignments.models import StudentAnswer

class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = [
            'id',
            'question', 'question_title',
            'student', 'student_name',
            'selected_option', 'selected_option_text',
            'text_answer', 'file_answer', 'code_answer',
            'is_correct', 'points_earned', 'feedback',
            'created_at', 'updated_at',
        ]
        read_only_fields = [
            'is_correct', 'points_earned', 'feedback',
            'created_at', 'updated_at',
            'student_name', 'question_title', 'selected_option_text'
        ]
