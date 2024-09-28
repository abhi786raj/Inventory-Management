from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import logging
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer


# Get the custom logger
logger = logging.getLogger('api')


class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        item_id = self.kwargs['pk']
        cache_key = f'item_{item_id}'

        item = cache.get(cache_key)
        if item is None:
            try:
                item = super().get_object()
                cache.set(cache_key, item, timeout=60 * 5)  # Cache it for 5 minutes
                logger.info(f'Cache miss for item_id {item_id}. Fetching from database.')
            except Exception as e:
                logger.error(f'Error fetching item_id {item_id}: {e}')
                raise  # Re-raise the exception after logging
        else:
            logger.info(f'Cache hit for item_id {item_id}. Retrieved from cache.')

        return item
