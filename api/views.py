import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexPageView(TemplateView):

    """Отображение главной страницы с товарами"""

    template_name = "api/index.html"

    def get_context_data(self, **kwargs):
        items = Item.objects.all()
        description = super(IndexPageView, self).get_context_data(**kwargs)
        description.update({
            "items": items,
        })
        return description


class ItemPageView(TemplateView):

    """Отображение выбранного товара для покупки"""

    template_name = "api/item.html"

    def get_context_data(self, **kwargs):
        id_item = self.kwargs.get("pk")
        items = Item.objects.get(pk=id_item)
        description = super(ItemPageView, self).get_context_data(**kwargs)
        description.update({
            "items": items,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return description


class CheckoutSessionView(View):

    """Осуществление покупки товара"""

    def post(self, request, *args, **kwargs):
        id_item = self.kwargs["pk"]
        items = Item.objects.get(id=id_item)
        checkout = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': items.price * 100,
                        'product_data': {
                            'name': items.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "id": items.id
            },
            mode='payment',
            success_url='http://127.0.0.1:8000/',
            cancel_url='http://127.0.0.1:8000/',
        )
        return JsonResponse({
            'id': checkout.id
        })
