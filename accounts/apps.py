from django.apps import AppConfig
import os

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from django.contrib.auth import get_user_model
        if os.environ.get("CREATE_SUPERUSER") == "true":
            try:
                User = get_user_model()
                if not User.objects.filter(username="admin").exists():
                    User.objects.create_superuser(
                        username="admin",
                        email="admin@test.com",
                        password="admin123"
                    )
                    print("Superuser created")
            except Exception as e:
                print(f"Superuser creation skipped: {e}")