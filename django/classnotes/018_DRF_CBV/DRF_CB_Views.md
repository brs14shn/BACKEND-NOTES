
# API View 

REST framework provides an APIView class, which subclasses Django's View class. Using the APIView class is pretty much the same as using a regular View class, as usual, the incoming request is dispatched to an appropriate handler method such as .get() or .post(). 

- For more information about [API View](https://www.django-rest-framework.org/api-guide/views/#class-based-views)

@api_view decorator: 
    Decorator that converts a function-based view into an APIView subclass.
    Takes a list of allowed methods for the view as an argument.

```python
class TodoList(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):

    def get_obj(self, pk):
        return get_object_or_404(Todo, pk=pk)

        # get_object_or_404 : Calls get() on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception.

    def get(self, request, pk):
        todo = self.get_obj(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_obj(pk)
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_obj(pk)
        todo.delete()
        data = {
            "message": "Todo succesfully deleted."
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
```

# Genericapi View 

### GenericAPIView
One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views. Some Basic Attributes and Methods.



Attributes :

    - queryset
    - serializer_class
    - lookup_field
    - lookup_url_kwarg

Methods :

    - get_queryset(self) : Returns the queryset that should be used for list views, and that should be used as the base for lookups in detail views. Defaults to returning the queryset specified by the queryset attribute.

    - get_object(self) : Returns an object instance that should be used for detail views. Defaults to using the lookup_field parameter to filter the base queryset.

Save and deletion hooks:

    - perform_create(self, serializer)
    - perform_update(self, serializer)
    - perform_destroy(self, instance)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

- For more information about [GenericAPIView Attributes and Methods]( https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)



### MIXINS : 

The mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly. This allows for more flexible composition of behavior.

The mixin classes can be imported from rest_framework.mixins.

- ListModelMixin
    - list method
- CreateModelMixin
    - create method
- RetrieveModelMixin
    - retrieve method
- UpdateModelMixin
    - update method
- DestroyModelMixin
    - destroy method

```python

from rest_framework import mixins
from rest_framework.generics import GenericAPIView


class TodoList(mixins.ListModelMixin, mixins.CreateModelMixin,  GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

## Concrete Views 
- Full list of concrete views [Documents]( https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes)


```python
class TodoListCreate(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "id"  
```

## ViewSets 

- Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. 

- Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.

There are two main advantages of using a ViewSet class over using a View class.

 - Repeated logic can be combined into a single class. In the above example, we only need to specify the queryset once, and it'll be used across multiple views.
 - By using routers, we no longer need to deal with wiring up the URL conf ourselves.

Both of these come with a trade-off. Using regular views and URL confs is more explicit and gives you more control. ViewSets are helpful if you want to get up and running quickly, or when you have a large API and you want to enforce a consistent URL configuration throughout.

- Viewsets [Documents]( https://www.django-rest-framework.org/api-guide/viewsets/#api-reference )




```python
class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

```

### Routers
REST framework adds support for automatic URL routing to Django, and provides you with a simple, quick and consistent way of wiring your view logic to a set of URLs.
- prefix : The URL prefix to use for this set of routes.
- viewset : The viewset class.
- basename : default is model name from queryset attribute

```python
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', TodoMVS)


path('', include(router.urls))

# urlpatterns += router.urls
```

Routing for extra actions  [Documents-Routers]( https://www.django-rest-framework.org/api-guide/routers/#routing-for-extra-actions)

Marking extra actions for routing  [Documents-Viewsets]( https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing)

```python
from rest_framework.decorators import action

class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(methods=["GET"], detail=False)
    def todo_count(self, request):
        todo_count = Todo.objects.filter(done=False).count()
        count = {
            'undo-todos': todo_count
        }
        return Response(count)
```