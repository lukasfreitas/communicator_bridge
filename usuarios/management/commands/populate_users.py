from django.core.management.base import BaseCommand
from usuarios.models import Usuario

class Command(BaseCommand):
    help = 'Popula o banco de dados com usuários de teste.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando a população do banco de dados com usuários...')

        # Limpa os usuários existentes para evitar duplicatas, exceto superusuários
        Usuario.objects.exclude(is_superuser=True).delete()
        self.stdout.write(self.style.WARNING('Usuários existentes (não superusuários) foram limpos.'))

        # Senha padrão para todos
        password = '123'

        # Criar Administradores
        for i in range(1, 3):
            username = f'admin{i}'
            email = f'admin{i}@example.com'
            Usuario.objects.create_user(
                username=username,
                email=email,
                password=password,
                tipo_usuario=Usuario.TipoUsuario.ADMINISTRADOR
            )
            self.stdout.write(self.style.SUCCESS(f'Usuário Administrador criado: {username}'))

        # Criar Atendentes
        for i in range(1, 3):
            username = f'atendente{i}'
            email = f'atendente{i}@example.com'
            Usuario.objects.create_user(
                username=username,
                email=email,
                password=password,
                tipo_usuario=Usuario.TipoUsuario.ATENDENTE
            )
            self.stdout.write(self.style.SUCCESS(f'Usuário Atendente criado: {username}'))

        # Criar Contatos
        for i in range(1, 3):
            username = f'contato{i}'
            email = f'contato{i}@example.com'
            Usuario.objects.create_user(
                username=username,
                email=email,
                password=password,
                tipo_usuario=Usuario.TipoUsuario.CONTATO
            )
            self.stdout.write(self.style.SUCCESS(f'Usuário Contato criado: {username}'))

        self.stdout.write(self.style.SUCCESS('\nBanco de dados populado com sucesso!'))
