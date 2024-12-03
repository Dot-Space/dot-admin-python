from typing import Callable, Type, Dict, List

from rest_framework.viewsets import GenericViewSet
from rest_framework.serializers import Serializer
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.request import clone_request, Request
from rest_framework.metadata import SimpleMetadata
from django.core.exceptions import PermissionDenied
from django.http import Http404

from dot_admin.filters.utils import get_filter_options


class ExpandedMetaData(SimpleMetadata):
    """
    Расширенный класс генерации схемы для option request
    """

    def determine_metadata(self, request: Type[Request], view: Type[GenericViewSet]) -> Dict[any, any]:
        """
        Get option scheme from ViewSet
        """
        metadata = {
            "name": view.get_view_name(),
            "description": view.get_view_description(),
            "renders": [renderer.media_type for renderer in view.renderer_classes],
            "parses": [parser.media_type for parser in view.parser_classes],
        }
        if hasattr(view, 'get_serializer'):
            actions = self.determine_actions(request, view)
            if actions:
                metadata['actions'] = actions
                metadata['action_funcs'] = self.determine_action_functions(view)
                metadata['filters'] = get_filter_options(view.queryset.model, True) if view.queryset is not None else {}
        return metadata
    
    def determine_actions(self, request: Type[Request], view: Type[GenericViewSet]) -> Dict[any, any]:
        """
        For generic class based views we return information about
        the fields that are accepted for 'PUT', 'POST' and 'GET' methods.
        """
        actions = {}
        for method in {'PUT', 'POST', 'GET'} & set(view.allowed_methods):
            view.request = clone_request(request, method)
            try:
                # Test global permissions
                if hasattr(view, 'check_permissions'):
                    view.check_permissions(view.request)
                # Test object permissions
                if method == 'PUT' and hasattr(view, 'get_object'):
                    view.get_object()
            except (exceptions.APIException, PermissionDenied, Http404):
                pass
            else:
                # If user has appropriate permissions for the view, include
                # appropriate metadata about the fields that should be supplied.
                serializer = view.get_serializer()
                actions[method] = self.get_serializer_info(serializer)
            finally:
                view.request = request

        return actions

    def determine_action_functions(self, view: Type[GenericViewSet]) -> Dict[str, Dict[str, Dict[any, any]]]:
        """
        Генерация схем для action view функций в model viewset
        """
        action_map: Dict[str, Dict[any, any]] = {}

        for class_var_name, value in view.__class__.__dict__.items():
            splitted_var_name: List[str] = class_var_name.split('_')

            if not self._is_action_serializer_var(splitted_var_name):
                continue
            splitted_var_name.pop(len(splitted_var_name) - 1)

            func_name: str = self._get_function_name(splitted_var_name)

            if not (serializers_map := action_map.get(func_name)):
                serializers_map = {}

            if splitted_var_name[0] == 'request':
                serializers_map['POST'] = self._get_serializer_info(value)
            elif splitted_var_name[0] == 'response':
                serializers_map['GET'] = self._get_serializer_info(value)
            else:
                serializers_map['GET/POST'] = self._get_serializer_info(value)

            action_map[func_name] = serializers_map

        return action_map

    @staticmethod
    def _is_action_serializer_var(splitted_var_name: List[str]) -> bool:
        """
        Validate serializer class alias variable
        """
        if len(splitted_var_name) <= 1:
            return False
        serializer_marker = splitted_var_name[len(splitted_var_name) - 1]
        if serializer_marker != 'serializer':
            return False
        
        return True
    
    @staticmethod
    def _get_function_name(splitted_name: List[str]) -> str:
        """
        Get name of action func from serializer class alias variable name
        """
        format_string: Callable[[List[str]], str] = lambda splitted_name: '_'.join(splitted_name)

        if (
            splitted_name[0] == 'request' or
            splitted_name[0] == 'response'
        ):
            return format_string(splitted_name[1:len(splitted_name)])
        
        return format_string(splitted_name)
    
    def _get_serializer_info(self, serializer: Type[Serializer]) -> Dict[str, Dict[any, any]]:
        """
        Given an instance of a serializer, return a dictionary of metadata
        about its fields.
        """
        if hasattr(serializer, 'child'):
            # If this is a `ListSerializer` then we want to examine the
            # underlying child serializer instance instead.
            serializer = serializer.child
        return {
            field_name: self.get_field_info(field)
            for field_name, field in serializer().get_fields().items()
            # оверврайтнуто так как возвращает .fields возвращает кэшированный аттрибут
            if not isinstance(field, serializers.HiddenField)
        }
