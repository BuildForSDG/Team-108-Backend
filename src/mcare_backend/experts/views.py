from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets

from experts.serializers import (
        ExpertClassSerializer
    )

from experts.models import ExpertClass


class ExpertClassViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Expertprofile instances.
    """

    serializer_class = ExpertClassSerializer
    queryset = ExpertClass.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action
        if (action == 'update'):
            # todo handle error when this fails
            active_class = ExpertClass.objects.get(
                id=self.kwargs['pk']
            )
            # if expert is creating a new class modules
            # get the class title and article  from the front end
            # then create the class. also add to its profile
            try:
                class_module_title = self.request.data['class_module_title']
                class_module_article = self.request.data[
                    'class_module_article'
                ]
                active_class.class_modules.create(
                    title=class_module_title,
                    article=class_module_article
                )
                active_class.save()
            except ObjectDoesNotExist:
                pass
        return context
