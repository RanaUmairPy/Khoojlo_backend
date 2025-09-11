from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    """Serializer for user signup with validations."""
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'password',
            'profile_picture', 'country', 'contact_number'
        ]

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        contact_number = attrs.get('contact_number')

        # Email uniqueness (case insensitive)
        if email and User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError({"email": "Email is already in use."})

        # Password length (min_length already handles this, but keep if you want custom error)
        if password and len(password) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})

        # Contact number uniqueness
        if contact_number and User.objects.filter(contact_number=contact_number).exists():
            raise serializers.ValidationError({"contact_number": "Contact number is already in use."})

        return attrs

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            profile_picture=validated_data.get('profile_picture'),
            country=validated_data.get('country'),
            contact_number=validated_data.get('contact_number')
        )
        # Use set_password
        user.set_password(validated_data['password'])
        user.save()
        return user
