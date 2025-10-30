# apps/api_endpoints/answers/serializers.py
from rest_framework import serializers
from apps.assignments.models import StudentAnswer, AnswerOption

class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = ['id', 'option_text', 'is_correct', 'order']


class StudentAnswerSerializer(serializers.ModelSerializer):
    selected_option = AnswerOptionSerializer(read_only=True)
    class Meta:
        model = StudentAnswer
        fields = ['id','question','student','selected_option','text_answer',
            'file_answer','code_answer','is_correct','points_earned',
            'feedback','created_at',
        ]
        read_only_fields = ['is_correct', 'points_earned', 'feedback', 'created_at']

    def create(self, validated_data):
        return StudentAnswer.objects.create(**validated_data)
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    def validate(self, data):
        if not any([data.get('selected_option'), data.get('text_answer'),
                    data.get('file_answer'), data.get('code_answer')]):
            raise serializers.ValidationError(
                "At least one type of answer must be provided."
            )
        return data
