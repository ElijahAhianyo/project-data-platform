import pynecone as pc
from okparser_web.states import NewOKHState


class YamlEditor(pc.Component):
    library = "@focus-reactive/react-yaml"
    tag = "YamlEditor"
    text: pc.Var[str]


yaml_editor = YamlEditor.create


def new() -> pc.Component:
    return pc.vstack(
            pc.text("Enter OKH"),
            yaml_editor(
            text = NewOKHState.okh_template
        ),
        pc.button("Generate")
    )
    # return pc.center(
    #     pc.vstack(
    #         pc.editable(
    #             pc.editable_preview(),
    #             pc.editable_input(),
    #             # pc.code_block(
    #             #     NewOKHState.okh_template,
    #             #     language="yaml",
    #             #     show_line_numbers=True,
    #             # ),
    #             value=NewOKHState.okh_template,
    #             # on_change=EditableState.set_uppertext,
    #             width="100%",
    #         ),
    #         spacing="1.5em",
    #         font_size="2em",
    #     ),
    #     padding_top="10%",
    # )
