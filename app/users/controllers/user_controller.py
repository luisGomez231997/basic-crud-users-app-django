"""Imports"""
from typing import Union
from datetime import datetime
from users.serializers.user_serializer import (
    CustomUser, CustomUserSerializer, make_password)


class UserController(object):
    """UserController class: make the logical operations in the view class."""

    def __init__(self) -> None:
        super().__init__()

    def format_dates(self, date:str) -> datetime:
        datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")

    def load_json_users(self, data) -> bool:
        try:
            for user in data:
                new_user = CustomUser.objects.create(
                        name = user["Nombres"],
                        first_last_name= user["Apellido 1"],
                        second_last_name = user["Apellido 2"],
                        identity_document_number = user["Cédula"],
                        date_of_birth = self.format_dates(user["Fecha de Nacimiento"]),
                        gender = user["Género"],
                        date_of_creation = self.format_dates(user["Fecha de Ingreso"]),
                        employed_number = user["Número de empleado"],
                        occupation = user["Cargo"],
                        boss = user["Jefe"],
                        zone = user["Zona"],
                        municipe = user["Municipio"],
                        department = user["Departamento"],
                        sells = user["Ventas 2019"],
                        email = user["Email"],
                        image = user["Imágen"],
                        cell_phone = user["Celular"],
                        password= make_password(user["Contraseña"])
                )
                new_user.save()
            return True
        except:
            return False
    
    def create_bulk(self, data: dict) -> Union[bool, str]:
        try:
            for user in data:
                new_user = CustomUser.objects.create(**user)
                new_serialized_user = CustomUserSerializer(new_user)
                if not new_serialized_user.is_valid:
                    return False
            return True
        except:
            return new_serialized_user.error_messages

    def get_employed_info(self, employed_number: int) -> dict:
        user: CustomUser = CustomUser.objects.get(
            employed_number__iexact=employed_number)
        if user != None:
            serialized_employeds: list = []
            if user.occupation == "Ejecutivo Comercial":
                total_sells: int = user.sells
                employeds: list = CustomUser.objects.filter(
                    boss=user.employed_number)
                for employed in employeds:
                    total_sells += employed.sells
                    serialized_employeds.append(
                        CustomUserSerializer(employed).data)
                return {
                    'users': CustomUserSerializer(user).data,
                    'total_sells': total_sells,
                    'employeds': serialized_employeds
                }
            else:
                return {
                    'users': CustomUserSerializer(user).data,
                    'total_sells': user.sells,
                    'employeds': serialized_employeds
                }
        else:
            return {}
