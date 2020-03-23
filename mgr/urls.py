from django.urls import path

from mgr import sign_in_out, table

urlpatterns = [
    path('signin', sign_in_out.signin),
    path('userinfo', sign_in_out.userinfo),
    path('signout', sign_in_out.signout),
    path('list_table', table.list_table),
    path('modify_table', table.modify_table),
    path('create_table', table.create_table),
    path('delete_table', table.delete_table),
]
