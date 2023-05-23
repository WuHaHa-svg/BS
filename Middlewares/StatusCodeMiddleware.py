from django.http import JsonResponse


class StatusCodeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        status_code = response.status_code

        # 根据不同的状态码返回不同的响应
        if status_code == 400:
            return JsonResponse({'error': 'Bad Request'}, status=status_code)
        elif status_code == 401:
            return JsonResponse({'error': 'Unauthorized'}, status=status_code)
        elif status_code == 403:
            return JsonResponse({'error': 'Forbidden'}, status=status_code)
        elif status_code == 404:
            return JsonResponse({'error': 'Not Found'}, status=status_code)
        elif status_code == 500:
            return JsonResponse({'error': 'Internal Server Error'}, status=status_code)

        return response
