def register_routes(routes, app):
    '''register route by giving view, endpoint and url.'''
    for r_t in routes:
        view_func = r_t[1].as_view(r_t[2])
        app.add_url_rule(r_t[0], view_func=view_func, methods=['GET', 'POST'])


