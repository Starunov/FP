from views import Home, Examples, Contacts


routes = {
    '/': Home(),
    '/examples/': Examples(),
    '/contacts/': Contacts(),
}
