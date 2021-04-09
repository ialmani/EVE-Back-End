# from rest_framework import permissions
#
#
# class OnlySponsorsPermission(permissions.BasePermission):
#     message = 'You are not authorized to access this page.'
#
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and (
#             request.user.is_sponsor())
