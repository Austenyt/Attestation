from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    choices = (
        (USER, USER),
        (ADMIN, ADMIN),
    )


class User(AbstractBaseUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        null=True,
        blank=True
    )
    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name="Роль пользователя",
        help_text="Выберите роль пользователя",
    )
    is_employee = models.BooleanField(
        default=False,
        verbose_name="Пользователь-сотрудник"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Аккаунт активен",
        help_text="Укажите, активен ли аккаунт"
    )

    @property
    def is_superuser(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_staff(self):
        """
        Это поле нужно для определения админа сотрудником автоматически.
        Таким образом, пользователь при регистрации определяется как не сотрудник, если он не суперюзер и,
        соответственно, не админ. После регистрации пользователь на усмотрение админа назначается
        сотрудником из админ-панели
        """
        return self.is_employee or self.role == UserRoles.ADMIN

    def has_perm(self, perm, obj=None):
        """ Предполагаем, что только активные сотрудники имеют разрешения """
        return self.is_staff and self.is_active

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]
