from django.shortcuts import redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):

        returnUrl = request.META['PATH_INFO']
        if not request.session.get('customer_id'):
            print("return url 1: ", returnUrl)
            return redirect(f'login?return_url={returnUrl}')
        response = get_response(request)
        return response

    return middleware