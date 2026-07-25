from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated and request.user.userprofile.role == "ADMIN"
        )


class IsRRHH(BasePermission):

    def has_permission(self, request, view):

        return request.user.is_authenticated and request.user.userprofile.role == "RRHH"


class IsContabilidad(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.userprofile.role == "CONTABILIDAD"
        )
