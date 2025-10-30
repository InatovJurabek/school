from rest_framework import serializers
from apps.assignments.models import AnswerOption, StudentAnswer


class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = ['id', 'option_text', 'is_correct', 'order']

class StudentAnswerSerializer(serializers.ModelSerializer):
    selected_option = AnswerOptionSerializer(read_only=True)
    
    class Meta:
        model = StudentAnswer
        fields = [
            'id',
            'question', 'question_title',
            'student', 'student_name',
            'selected_option', 'selected_option_text',
            'text_answer', 'file_answer', 'code_answer',
            'is_correct', 'points_earned', 'feedback',
        ]
        read_only_fields = ['is_correct', 'points_earned', 'feedback', 'created_at'
        ]
