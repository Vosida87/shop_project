from typing import Any


class CommonMixin():
    title = None

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super(CommonMixin, self).get_context_data(**kwargs)
        context["title"] = self.title
        return context
