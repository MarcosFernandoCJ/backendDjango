from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users, Roles, UserRoles

def assign_role_view(request):
    users = Users.objects.all()
    roles = Roles.objects.all()

    # Obtener roles asignados para cada usuario
    users_with_roles = [
        {
            "user": user,
            "roles": UserRoles.objects.filter(user=user).select_related('role')
        }
        for user in users
    ]

    if request.method == 'POST':
        if 'assign_role' in request.POST:
            # Lógica para asignar un rol
            user_id = request.POST.get('assign_role')
            role_id = request.POST.get(f'role_{user_id}')

            if role_id:
                user = Users.objects.get(id=user_id)
                role = Roles.objects.get(id=role_id)

                # Crear o actualizar el rol del usuario
                user_role, created = UserRoles.objects.get_or_create(user=user, role=role)
                if created:
                    messages.success(request, f"Role '{role.name}' assigned to user '{user.username}' successfully!")
                else:
                    messages.info(request, f"User '{user.username}' already has the role '{role.name}'.")
            else:
                messages.error(request, "Please select a role before assigning.")

        elif 'remove_role' in request.POST:
            # Lógica para remover un rol
            user_id = request.POST.get('user_id')
            role_id = request.POST.get(f'remove_role_{user_id}')

            if role_id:
                try:
                    user_role = UserRoles.objects.get(user_id=user_id, role_id=role_id)
                    user_role.delete()
                    messages.success(request, "Role removed successfully!")
                except UserRoles.DoesNotExist:
                    messages.error(request, "Role does not exist or was already removed.")
            else:
                messages.error(request, "Please select a role to remove.")

        return redirect('assign_role')  # Cambia 'assign_role' por el nombre de tu URL
    
    return render(request, 'assign_role.html', {'users_with_roles': users_with_roles, 'roles': roles})
