import pynecone as pc


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Generate OKH", size="4xl"),
            pc.hstack(
                pc.container(
                    pc.link(

                        "upload existing",
                        border="0.1em solid",
                        padding="0.5em",
                        border_radius="0.5em",
                        _hover={
                            "color": "rgb(107,99,246)",
                        },
                        href="/existing",
                    ),
                    pc.link(
                        "Create new",
                        border="0.1em solid",
                        padding="0.5em",
                        margin_left="2.5em",
                        border_radius="0.5em",
                        _hover={
                            "color": "rgb(107,99,246)",
                        },
                        href="/new"
                    ),
                ),
                padding_top="20%",
                # margin="0.3em",
                margin_right="4.5em",
                spacing="1.5em",
                font_size="2em",
            ),
            padding_top="10%",
            padding_right="10%"
        ),

        # padding_top="10%",
    )
