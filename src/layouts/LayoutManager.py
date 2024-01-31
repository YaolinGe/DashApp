from dash_bootstrap_components import Container
from layouts.BaseLayout import BaseLayout
from layouts.NavBarLayout import update_nav_bar


class LayoutManager:
    @staticmethod
    def update_page_layout(nav_bar_content: Container, view_port_content: Container) -> Container:
        base_layout = BaseLayout()
        base_layout.create_nav_bar(nav_bar_content)
        base_layout.create_view_port(view_port_content)
        return base_layout.update_layout()
