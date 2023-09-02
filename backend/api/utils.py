from django.http import HttpResponse


def download_file_response(ingredients_list):
    buy_list = ['Чтобы приготовить все блюда из корзины необходимо:\n']
    for item in ingredients_list:
        buy_list.append(f'{item["ingredient__name"]} - {item["amount"]} '
                        f'{item["ingredient__measurement_unit"]}\n')

    filename = "buylist.txt"
    content = ''.join(buy_list)
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response
