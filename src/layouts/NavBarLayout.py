import dash_bootstrap_components as dbc
from dash import html


def update_nav_bar(activate_page: str = "Home"):
    return (
        dbc.Container(
            dbc.Row(
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                children=
                                [
                                    html.I(className="bi bi-house me-2"),
                                    html.Span("Home")
                                ],
                                href="/",
                                active=True if activate_page == "Home" else False,
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                children=[
                                    html.I(className="bi bi-alarm me-2"),
                                    html.Span("Review")
                                ],
                                href="/review",
                                active=True if activate_page == "Review" else False
                            )
                        ),
                    ],
                    vertical="md",
                    pills=True,
                    style={
                        "fontSize": 16,
                    }
                )
            )
        )
    )
