from rest_framework.routers import Route, DefaultRouter

class CustomRouter(DefaultRouter):
    """
    Custom router used for mapping request to different methods.
    """

    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        Route(
            url=r'^{prefix}/$',
            mapping={'post': 'create'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/$',
            mapping={'put': 'update'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'detail'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'delete': 'destroy'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'patch': 'partial_update'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]