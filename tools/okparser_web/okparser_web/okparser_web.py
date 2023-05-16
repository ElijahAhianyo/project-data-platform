"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from okparser_web.states import State
from okparser_web.pages import index, new, existing

import pynecone as pc

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(new)
app.add_page(existing)
app.compile()
