from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from common.views import CommonMixin
from orders.forms import OrderForm


class OrderCreateView(CommonMixin, CreateView):
    """Представление для создания заказа"""
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:create')
    title = 'Store - оформление заказа'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
