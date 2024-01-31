import dash_bootstrap_components as dbc


def update_nav_bar(activate_page: str = "Home"):
    return (
        dbc.Container(
            dbc.Row(
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                children="Home",
                                active=True if activate_page == "Home" else False,
                                href="/"
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                children="EDA",
                                href="/eda",
                                active=True if activate_page == "EDA" else False
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
